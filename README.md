# Brechas Salariales de Género en Chile: un análisis multidimensional 🇨🇱

> *En Chile, las mujeres ganan en promedio menos que los hombres — pero ¿cuánto de esa brecha se explica por dónde trabajan, cuánto estudiaron, cuántas horas trabajan o cuántos años tienen? ¿Y cuánto queda sin explicación?*

Este proyecto descompone la brecha salarial de género en Chile en dos etapas: primero con **datos agregados oficiales** del SIMEL-INE (indicadores públicos vía API, sin autenticación), y luego con **microdatos individuales** de la Encuesta Suplementaria de Ingresos (ESI 2018-2024), que permiten una regresión multivariable real.

---

## Marco metodológico

La brecha salarial observada mezcla dos fenómenos distintos:

1. **Composición** — diferencias en características observables (educación, sector, horas, ocupación, edad)
2. **Discriminación residual** — la parte que persiste después de controlar todo lo anterior

Los notebooks 01-05 exploran la brecha con datos agregados SIMEL (máximo 2 variables cruzadas simultáneamente — el techo real de ese tipo de datos). El notebook 06 rompe ese techo usando **microdatos individuales**, estimando una regresión tipo Mincer que controla por edad, edad², educación, horas trabajadas, categoría ocupacional y sector **al mismo tiempo**. El notebook 07 suma estado civil y presencia de hijos en el hogar, y aplica una **descomposición de Oaxaca-Blinder** para cuantificar qué porcentaje de la brecha total se explica por cada factor específico.

### Convención de signo (importante)

El indicador SIMEL/ESI usado es:

```
Brecha (%) = (Ingreso_Mujeres - Ingreso_Hombres) / Ingreso_Hombres × 100
```

**Negativo = las mujeres ganan menos** (la situación habitual). Positivo = las mujeres ganan más (ocurre en algunos grupos específicos, ej. electricidad).

---

## App interactiva

`app.py` es una app **Streamlit** que deja explorar cómo se mueve la brecha al activar controles, uno por uno o todos a la vez: edad, educación, horas trabajadas, categoría ocupacional, sector económico, zona rural/urbana, estado civil, hijos en el hogar y año. Muestra el ingreso promedio predicho para un hombre y una mujer "típicos" bajo el modelo activo, y un gráfico con el historial de brechas probadas en la sesión.

```bash
streamlit run app.py
```

La app funciona en **dos modos**, detectados automáticamente:

- **Precalculado (por defecto / despliegue en la nube):** lee `app_data/resultados_precalculados.json`, que contiene las 512 combinaciones posibles de los 9 controles (2⁹), ya calculadas con la metodología de los notebooks 06-07 (WLS ponderado, errores estándar cluster-robustos). No requiere los microdatos ESI — por eso la app puede desplegarse públicamente (ej. Streamlit Community Cloud) sin necesitar los CSV de 100+ MB que no se versionan en este repositorio.
- **En vivo (desarrollo local):** si existe una carpeta `ESI/` con los microdatos al mismo nivel que este repositorio, la app ajusta cada regresión en tiempo real sobre los datos reales en lugar de usar el archivo precalculado.

Para regenerar el archivo precalculado (por ejemplo, si se agregan más años de ESI):

```bash
python precalcular.py   # ~60-90 minutos, requiere ../ESI/
```

---

## Estructura del proyecto

```
brechas-salariales-genero-chile/
├── app.py                                  ← app interactiva (Streamlit)
├── precalcular.py                          ← genera app_data/resultados_precalculados.json
├── app_data/
│   └── resultados_precalculados.json      ← 512 combinaciones de controles ya calculadas
├── notebooks/
│   ├── 01_descarga_api.ipynb              ← descarga los 10 datasets SIMEL de brecha salarial
│   ├── 02_brecha_multidimensional.ipynb   ← brecha por educación, sector, edad (datos agregados)
│   ├── 03_evolucion_regional.ipynb        ← convergencia temporal + heatmap regional + benchmark OCDE
│   ├── 04_brecha_ajustada.ipynb           ← ranking sector/ocupación, control por jornada, heatmap CISE×educación
│   ├── 05_serie_educacion.ipynb           ← serie 2010-2023: ¿qué niveles educativos convergen más rápido?
│   ├── 06_regresion_microdatos.ipynb      ← regresión Mincer con microdatos ESI 2018-2024 (máximo de controles)
│   └── 07_oaxaca_blinder_hijos.ipynb      ← estado civil, hijos y descomposición Oaxaca-Blinder por factor
├── data/            ← CSVs descargados de SIMEL (se regeneran ejecutando el notebook 01)
├── outputs/
│   └── figures/     ← gráficos exportados en PNG
└── requirements.txt
```

---

## Fuentes de datos

| Fuente | Qué aporta | Acceso |
|---|---|---|
| API SDMX SIMEL-INE (`DF_BGYMEDIOOCU*`, `DF_BGYHDEP*`) | Indicadores agregados de brecha por región, educación, edad, sector, ocupación, jornada y categoría ocupacional | Pública, sin autenticación, vía `simel_client.py` |
| Microdatos ESI 2018-2024 (INE, formato CSV) | Registros individuales: sexo, edad, educación, horas, categoría ocupacional, sector, ingreso del trabajo principal | Pública, descarga manual desde el sitio del INE (sección Encuesta Suplementaria de Ingresos → Bases de Datos → CSV) |

**Nota de reproducibilidad:** los CSV de microdatos ESI (~100 MB cada uno) no se versionan en este repositorio por su tamaño. Para ejecutar los notebooks 06-07, o la app interactiva en modo "en vivo", descárgalos del sitio del INE y colócalos en una carpeta `ESI/` al mismo nivel que este repositorio. La app interactiva funciona sin ellos gracias a los resultados precalculados (`app_data/`).

---

## Hallazgo principal

Con microdatos individuales (notebook 06) y controlando **simultáneamente** por edad, edad², nivel educativo, horas trabajadas, categoría ocupacional y sector económico (errores estándar con cluster-robusto por conglomerado × año, dado el diseño muestral complejo de la ESI):

- **Brecha bruta (2018-2024, pooled):** -22.7%
- **Brecha ajustada (con todos los controles):** -20.7% (IC 95%: -21.4% a -20.0%, p < 0.001)
- **Solo ~9% de la brecha bruta se explica por composición observable**

La brecha ajustada y la bruta se mueven casi juntas en los 7 años de la serie — no hay evidencia de que la brecha sea un artefacto de composición del mercado laboral.

El notebook 07 profundiza con una **descomposición de Oaxaca-Blinder**, que suma estado civil e hijos en el hogar y atribuye la brecha a cada factor específico:

- **Solo ~23% de la brecha se explica por composición** (horas, sector, educación, estado civil, hijos); **~77% queda sin explicar**
- **Horas trabajadas y sector económico** son los mayores contribuyentes a la parte explicada
- **La educación contribuye en sentido contrario**: las mujeres de la muestra están, en promedio, mejor educadas — por sí sola esa variable predeciría un ingreso *mayor* para ellas
- **La interacción mujer×hijos no es estadísticamente significativa** una vez controlado el estado civil — la penalización se concentra más en mujeres casadas/convivientes que en la presencia de hijos en sí

Es la aproximación más rigurosa posible, con datos públicos, a un componente de discriminación salarial pura.

---

## Cómo reproducir

```bash
git clone https://github.com/W00lscarf/brechas-salariales-genero-chile
cd brechas-salariales-genero-chile
pip install -r requirements.txt
jupyter lab
# Notebooks 01-05: ejecutar en orden, no requieren nada adicional (descargan datos SIMEL automáticamente)
# Notebooks 06-07: requieren descargar microdatos ESI 2018-2024 del INE y ubicarlos en ../ESI/
```

---

## Stack técnico

**Python 3.11** · pandas · numpy · matplotlib · seaborn · plotly · scipy · statsmodels · scikit-learn · patsy · streamlit · requests

---

## Licencia

MIT — libre uso con atribución.
