"""
Brecha salarial interactiva — activa controles y observa cómo se mueve la brecha.

Ejecutar con:  streamlit run app.py
Requiere los microdatos ESI 2018-2024 (CSV) en una carpeta `ESI/` al mismo
nivel que este repositorio (ver README.md, sección "Fuentes de datos").
"""
import os
import numpy as np
import pandas as pd
import patsy
import statsmodels.formula.api as smf
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Brecha salarial interactiva", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_ESI = os.path.join(BASE_DIR, "..", "ESI")

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


@st.cache_data(show_spinner="Cargando microdatos ESI 2018-2024 (una sola vez)...")
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
    'Edad':                 'edad + edad2',
    'Educación':            "C(nivel_grp)",
    'Horas trabajadas':     'habituales',
    'Categoría ocupacional': "C(categoria_ocupacion)",
    'Sector económico':     "C(b14_rev4cl_caenes)",
    'Rural / Urbano':       "C(rural)",
    'Estado civil':         "C(estado_civil_grp)",
    'Tiene hijos':          'tiene_hijos',
    'Año':                  "C(anio)",
}


@st.cache_data(show_spinner=False)
def ajustar_modelo(activos, _muestra):
    terminos = ' + '.join(CONTROLES[c] for c in activos)
    formula = f'log_ingreso ~ mujer' + (f' + {terminos}' if terminos else '')
    modelo = smf.wls(formula, data=_muestra, weights=_muestra['fact_cal_esi']).fit(
        cov_type='cluster', cov_kwds={'groups': _muestra['cluster_id']})

    y, X = patsy.dmatrices(formula, _muestra, return_type='dataframe')
    w = _muestra['fact_cal_esi'].values
    xbar = np.average(X, axis=0, weights=w)
    beta = modelo.params.reindex(X.columns).values

    idx_mujer = list(X.columns).index('mujer')
    x_hombre, x_mujer = xbar.copy(), xbar.copy()
    x_hombre[idx_mujer], x_mujer[idx_mujer] = 0, 1

    ingreso_hombre = np.exp(np.dot(x_hombre, beta))
    ingreso_mujer = np.exp(np.dot(x_mujer, beta))

    coef_mujer = modelo.params['mujer']
    ic = modelo.conf_int().loc['mujer']
    return {
        'brecha_pct': (np.exp(coef_mujer) - 1) * 100,
        'ic_bajo': (np.exp(ic[0]) - 1) * 100,
        'ic_alto': (np.exp(ic[1]) - 1) * 100,
        'p_valor': modelo.pvalues['mujer'],
        'ingreso_hombre': ingreso_hombre,
        'ingreso_mujer': ingreso_mujer,
        'r2': modelo.rsquared,
        'n': int(modelo.nobs),
    }


st.title("¿Cuánto se achica la brecha salarial al agregar controles?")
st.caption(
    "Datos reales: microdatos de la Encuesta Suplementaria de Ingresos (INE), 2018-2024. "
    "Activa variables como controles estadísticos y observa cómo se mueve la brecha entre "
    "hombres y mujeres."
)

if not os.path.isdir(RUTA_ESI):
    st.error(
        f"No se encontró la carpeta de microdatos ESI en `{RUTA_ESI}`. "
        "Descarga los CSV 2018-2024 desde el sitio del INE y colócalos en una carpeta "
        "`ESI/` al mismo nivel que este repositorio (ver README.md)."
    )
    st.stop()

muestra = cargar_panel()

if 'historial' not in st.session_state:
    st.session_state.historial = []

col_visual, col_controles = st.columns([2, 1], gap="large")

with col_controles:
    st.subheader("Variables disponibles")
    st.caption("Arrastra... bueno, en esta versión: actívalas con un click. 👇")
    activos = []
    for nombre in CONTROLES:
        if st.checkbox(nombre, key=f"chk_{nombre}"):
            activos.append(nombre)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Activar todos", use_container_width=True):
            for nombre in CONTROLES:
                st.session_state[f"chk_{nombre}"] = True
            st.rerun()
    with c2:
        if st.button("Limpiar todo", use_container_width=True):
            for nombre in CONTROLES:
                st.session_state[f"chk_{nombre}"] = False
            st.session_state.historial = []
            st.rerun()

resultado = ajustar_modelo(tuple(activos), muestra)

clave_historial = (len(activos), round(resultado['brecha_pct'], 2))
if not st.session_state.historial or st.session_state.historial[-1][:2] != clave_historial:
    st.session_state.historial.append((len(activos), round(resultado['brecha_pct'], 2), tuple(activos)))

with col_visual:
    brecha = resultado['brecha_pct']
    color_brecha = "#c0392b" if brecha < -15 else "#e67e22" if brecha < -5 else "#27ae60"

    fig_personas = go.Figure()
    fig_personas.add_annotation(text="👨", x=0.25, y=0.55, showarrow=False, font=dict(size=90))
    fig_personas.add_annotation(text="👩", x=0.75, y=0.55, showarrow=False, font=dict(size=90))
    fig_personas.add_annotation(
        text=f"${resultado['ingreso_hombre']:,.0f}", x=0.25, y=0.05, showarrow=False,
        font=dict(size=22, color="#2e86c1"))
    fig_personas.add_annotation(
        text=f"${resultado['ingreso_mujer']:,.0f}", x=0.75, y=0.05, showarrow=False,
        font=dict(size=22, color="#c0392b"))
    fig_personas.update_xaxes(visible=False, range=[0, 1])
    fig_personas.update_yaxes(visible=False, range=[0, 1])
    fig_personas.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10),
                                plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_personas, use_container_width=True)

    st.markdown(
        f"<h1 style='text-align:center;color:{color_brecha};margin-top:-20px;'>"
        f"{brecha:.1f}%</h1>"
        f"<p style='text-align:center;color:gray;margin-top:-15px;'>"
        f"brecha salarial (mujeres vs. hombres) · IC 95%: {resultado['ic_bajo']:.1f}% a "
        f"{resultado['ic_alto']:.1f}% · n = {resultado['n']:,}</p>",
        unsafe_allow_html=True,
    )

    n_activos = len(activos)
    if n_activos == 0:
        st.info("**Brecha bruta** — sin ningún control activo. Es la diferencia cruda de ingreso medio.")
    elif n_activos == len(CONTROLES):
        st.success(
            "**Brecha con el máximo de controles activos.** Esta es la aproximación más "
            "rigurosa a la brecha \"no explicada\" (discriminación) que permiten estos datos."
        )
    else:
        st.warning(f"**{n_activos} de {len(CONTROLES)} controles activos.**")

    st.subheader("Cómo se ha movido la brecha en esta sesión")
    hist_df = pd.DataFrame(st.session_state.historial, columns=['n_controles', 'brecha', 'controles'])
    hist_df['paso'] = range(1, len(hist_df) + 1)
    fig_hist = go.Figure()
    fig_hist.add_trace(go.Scatter(
        x=hist_df['paso'], y=hist_df['brecha'], mode='lines+markers',
        line=dict(color='#8e44ad', width=3), marker=dict(size=9),
        text=[f"{n} control(es)" for n in hist_df['n_controles']],
        hovertemplate="%{text}<br>Brecha: %{y:.1f}%<extra></extra>",
    ))
    fig_hist.add_hline(y=0, line_dash="dash", line_color="gray")
    fig_hist.update_layout(
        height=260, margin=dict(l=10, r=10, t=10, b=10),
        yaxis_title="Brecha (%)", xaxis_title="Combinaciones probadas en esta sesión",
        xaxis=dict(dtick=1),
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.divider()
with st.expander("¿Qué significan los números?"):
    st.markdown(
        """
- **Brecha (%)**: `(ingreso mujeres − ingreso hombres) / ingreso hombres × 100`. Negativo = las mujeres
  ganan menos (la situación habitual en Chile).
- **Sin controles activos** → brecha bruta: la diferencia de ingreso medio sin ajustar por nada.
- **Con controles activos** → brecha ajustada: la diferencia que persiste entre una mujer y un hombre
  **con las mismas características** en las variables activadas (misma edad, educación, horas, etc.).
- Los íconos muestran el ingreso mensual promedio predicho para un hombre y una mujer "típicos" bajo
  el modelo actual — manteniendo constantes las variables activadas en su valor promedio poblacional.
- Los errores estándar consideran el diseño muestral complejo de la ESI (cluster por conglomerado y año).
        """
    )
    st.caption(
        "Metodología idéntica a la usada en los notebooks 06 y 07 de este repositorio: "
        "regresión tipo Mincer con errores estándar cluster-robustos, ponderada por el factor "
        "de expansión de la encuesta (fact_cal_esi)."
    )
