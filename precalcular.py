"""
Precalcula la brecha salarial ajustada para las 512 combinaciones posibles de
controles (2^9), usando los microdatos ESI 2018-2024. El resultado se guarda en
app_data/resultados_precalculados.json y es lo que consume app.py en producción
(evita depender de los CSV de microdatos, que no se versionan por su tamaño).

Ejecutar UNA VEZ localmente (con la carpeta ../ESI/ disponible):
    python precalcular.py

Tarda aproximadamente 60-90 minutos (512 regresiones WLS con errores
cluster-robustos sobre ~250,000 registros).
"""
import itertools
import json
import os
import time

import numpy as np
import pandas as pd
import patsy
import statsmodels.formula.api as smf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_ESI = os.path.join(BASE_DIR, "..", "ESI")
RUTA_SALIDA = os.path.join(BASE_DIR, "app_data", "resultados_precalculados.json")

ARCHIVOS = {
    2018: "esi-2018-personas.csv", 2019: "esi-2019-personas.csv",
    2020: "esi-2020-personas.csv", 2021: "esi_2021.csv",
    2022: "esi_2022.csv", 2023: "esi_2023.csv", 2024: "esi_2024 (1).csv",
}
COLS = ['sexo', 'edad', 'nivel', 'categoria_ocupacion', 'categoria_ocupacional',
        'b14_rev4cl_caenes', 'habituales', 'ing_t_p', 'fact_cal_esi', 'conglomerado',
        'id_identificacion', 'parentesco', 'est_conyugal', 'tipo']
RENAME = {'categoria_ocupacional': 'categoria_ocupacion'}
NIVEL_GRUPO = {
    0: 'Sin educ.', 1: 'Sin educ.', 2: 'Sin educ.',
    3: 'Básica', 4: 'Media', 5: 'Media', 6: 'Media',
    7: 'Técnica sup.', 8: 'Técnica sup.',
    9: 'Universitaria', 10: 'Universitaria',
    11: 'Posgrado', 12: 'Posgrado', 14: 'Media',
}


def grupo_civil(x):
    if x in (1, 2):
        return 'Casado/Conviviente'
    if x == 3:
        return 'Soltero/a'
    if x in (4, 5, 6):
        return 'Otro'
    return np.nan


def cargar_panel():
    frames = []
    for anio, fname in ARCHIVOS.items():
        ruta = os.path.join(RUTA_ESI, fname)
        df = pd.read_csv(ruta, usecols=lambda c: c in COLS, low_memory=False, encoding='latin-1')
        df = df.rename(columns=RENAME)
        df = df.loc[:, ~df.columns.duplicated()]
        df['anio'] = anio
        df['hogar_id'] = df['anio'].astype(str) + '_' + df['id_identificacion'].astype(str)
        frames.append(df)
    panel = pd.concat(frames, ignore_index=True)

    hogares_con_hijos = panel[panel['parentesco'] == 4]['hogar_id'].unique()
    panel['tiene_hijos'] = panel['hogar_id'].isin(hogares_con_hijos).astype(int)
    panel['estado_civil_grp'] = panel['est_conyugal'].map(grupo_civil)
    panel['rural'] = np.where(panel['tipo'] == 3, 'Rural', 'Urbano')

    muestra = panel[
        (panel['ing_t_p'] > 0) & (panel['habituales'].between(1, 98)) &
        (panel['nivel'].isin(NIVEL_GRUPO.keys())) & (panel['categoria_ocupacion'].between(1, 7)) &
        (panel['b14_rev4cl_caenes'].between(1, 21)) & (panel['sexo'].isin([1, 2])) &
        (panel['estado_civil_grp'].notna())
    ].copy()

    muestra['mujer'] = (muestra['sexo'] == 2).astype(int)
    muestra['nivel_grp'] = muestra['nivel'].map(NIVEL_GRUPO)
    muestra['log_ingreso'] = np.log(muestra['ing_t_p'])
    muestra['edad2'] = muestra['edad'] ** 2
    muestra['categoria_ocupacion'] = muestra['categoria_ocupacion'].astype(int).astype(str)
    muestra['b14_rev4cl_caenes'] = muestra['b14_rev4cl_caenes'].astype(int).astype(str)
    muestra['cluster_id'] = muestra['anio'].astype(str) + '_' + muestra['conglomerado'].astype(str)
    return muestra


CONTROLES = {
    'Edad':                  'edad + edad2',
    'Educación':             "C(nivel_grp)",
    'Horas trabajadas':      'habituales',
    'Categoría ocupacional': "C(categoria_ocupacion)",
    'Sector económico':      "C(b14_rev4cl_caenes)",
    'Rural / Urbano':        "C(rural)",
    'Estado civil':          "C(estado_civil_grp)",
    'Tiene hijos':           'tiene_hijos',
    'Año':                   "C(anio)",
}


def ajustar_modelo(activos, muestra):
    terminos = ' + '.join(CONTROLES[c] for c in activos)
    formula = 'log_ingreso ~ mujer' + (f' + {terminos}' if terminos else '')
    modelo = smf.wls(formula, data=muestra, weights=muestra['fact_cal_esi']).fit(
        cov_type='cluster', cov_kwds={'groups': muestra['cluster_id']})

    y, X = patsy.dmatrices(formula, muestra, return_type='dataframe')
    w = muestra['fact_cal_esi'].values
    xbar = np.average(X, axis=0, weights=w)
    beta = modelo.params.reindex(X.columns).values

    idx_mujer = list(X.columns).index('mujer')
    x_hombre, x_mujer = xbar.copy(), xbar.copy()
    x_hombre[idx_mujer], x_mujer[idx_mujer] = 0, 1

    ingreso_hombre = float(np.exp(np.dot(x_hombre, beta)))
    ingreso_mujer = float(np.exp(np.dot(x_mujer, beta)))
    coef_mujer = modelo.params['mujer']
    ic = modelo.conf_int().loc['mujer']

    return {
        'brecha_pct': float((np.exp(coef_mujer) - 1) * 100),
        'ic_bajo': float((np.exp(ic[0]) - 1) * 100),
        'ic_alto': float((np.exp(ic[1]) - 1) * 100),
        'p_valor': float(modelo.pvalues['mujer']),
        'ingreso_hombre': ingreso_hombre,
        'ingreso_mujer': ingreso_mujer,
        'r2': float(modelo.rsquared),
        'n': int(modelo.nobs),
    }


def clave(subset):
    return '|'.join(sorted(subset)) if subset else '__ninguno__'


def main():
    print('Cargando microdatos ESI 2018-2024...')
    muestra = cargar_panel()
    print(f'Muestra analítica: {len(muestra):,} personas')

    nombres = list(CONTROLES.keys())
    todas_combinaciones = []
    for r in range(len(nombres) + 1):
        todas_combinaciones.extend(itertools.combinations(nombres, r))
    print(f'Total de combinaciones a calcular: {len(todas_combinaciones)}')

    resultados = {}
    if os.path.exists(RUTA_SALIDA):
        with open(RUTA_SALIDA, 'r', encoding='utf-8') as f:
            resultados = json.load(f)
        print(f'Reanudando: {len(resultados)} combinaciones ya calculadas previamente.')

    os.makedirs(os.path.dirname(RUTA_SALIDA), exist_ok=True)
    t_inicio = time.time()
    for i, combo in enumerate(todas_combinaciones):
        k = clave(combo)
        if k in resultados:
            continue
        resultados[k] = ajustar_modelo(list(combo), muestra)
        if (i + 1) % 10 == 0 or (i + 1) == len(todas_combinaciones):
            with open(RUTA_SALIDA, 'w', encoding='utf-8') as f:
                json.dump(resultados, f, ensure_ascii=False, indent=0)
            transcurrido = time.time() - t_inicio
            print(f'[{i+1}/{len(todas_combinaciones)}] guardado. '
                  f'Transcurrido: {transcurrido/60:.1f} min')

    with open(RUTA_SALIDA, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=0)
    print(f'\nListo. {len(resultados)} combinaciones guardadas en {RUTA_SALIDA}')


if __name__ == '__main__':
    main()
