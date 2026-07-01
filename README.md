# Brechas Salariales de Género en Chile: un análisis multidimensional 🇨🇱

> *En Chile, las mujeres ganan en promedio menos que los hombres — pero ¿cuánto de esa brecha se explica por dónde trabajan, cuánto estudiaron, cuántas horas trabajan o cuántos años tienen? ¿Y cuánto queda sin explicación?*

Este proyecto descompone la brecha salarial de género en Chile en dos etapas: primero con **datos agregados oficiales** del SIMEL-INE (indicadores públicos vía API, sin autenticación), y luego con **microdatos individuales** de la Encuesta Suplementaria de Ingresos (ESI 2018-2024), que permiten una regresión multivariable real.

---

## Marco metodológico

La brecha salarial observada mezcla dos fenómenos distintos:

1. **Composición** — diferencias en características observables (educación, sector, horas, ocupación, edad)
2. **Discriminación residual** — la parte que persiste después de controlar todo lo anterior

Los notebooks 01-05 exploran la brecha con datos agregados SIMEL (máximo 2 variables cruzadas simultáneamente — el techo real de ese tipo de datos). El notebook 06 rompe ese techo usando **microdatos individuales**, estimando una regresión tipo Mincer que controla por edad, edad², educación, horas trabajadas, categoría ocupacional y sector **al mismo tiempo**.

### Convención de signo (importante)

El indicador SIMEL/ESI usado es:

```
Brecha (%) = (Ingreso_Mujeres - Ingreso_Hombres) / Ingreso_Hombres × 100
```

**Negativo = las mujeres ganan menos** (la situación habitual). Positivo = las mujeres ganan más (ocurre en algunos grupos específicos, ej. electricidad).

---

## Estructura del proyecto

```
brechas-salariales-genero-chile/
├── notebooks/
│   ├── 01_descarga_api.ipynb              ← descarga los 10 datasets SIMEL de brecha salarial
│   ├── 02_brecha_multidimensional.ipynb   ← brecha por educación, sector, edad (datos agregados)
│   ├── 03_evolucion_regional.ipynb        ← convergencia temporal + heatmap regional + benchmark OCDE
│   ├── 04_brecha_ajustada.ipynb           ← ranking sector/ocupación, control por jornada, heatmap CISE×educación
│   ├── 05_serie_educacion.ipynb           ← serie 2010-2023: ¿qué niveles educativos convergen más rápido?
│   └── 06_regresion_microdatos.ipynb      ← regresión Mincer con microdatos ESI 2018-2024 (máximo de controles)
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

**Nota de reproducibilidad:** los CSV de microdatos ESI (~100 MB cada uno) no se versionan en este repositorio por su tamaño. Para ejecutar el notebook 06, descárgalos del sitio del INE y colócalos en una carpeta `ESI/` al mismo nivel que este repositorio (el notebook los referencia con una ruta relativa `../../ESI/`).

---

## Hallazgo principal

Con microdatos individuales (notebook 06) y controlando **simultáneamente** por edad, edad², nivel educativo, horas trabajadas, categoría ocupacional y sector económico:

- **Brecha bruta (2018-2024, pooled):** -22.7%
- **Brecha ajustada (con todos los controles):** -20.7% (IC 95%: -21.1% a -20.2%, p < 0.001)
- **Solo ~9% de la brecha bruta se explica por composición observable**

La brecha ajustada y la bruta se mueven casi juntas en los 7 años de la serie — no hay evidencia de que la brecha sea un artefacto de composición del mercado laboral. Es la aproximación más rigurosa posible, con datos públicos, a un componente de discriminación salarial pura.

---

## Cómo reproducir

```bash
git clone https://github.com/W00lscarf/brechas-salariales-genero-chile
cd brechas-salariales-genero-chile
pip install -r requirements.txt
jupyter lab
# Notebooks 01-05: ejecutar en orden, no requieren nada adicional (descargan datos SIMEL automáticamente)
# Notebook 06: requiere descargar microdatos ESI 2018-2024 del INE y ubicarlos en ../ESI/
```

---

## Stack técnico

**Python 3.11** · pandas · numpy · matplotlib · seaborn · scipy · statsmodels · scikit-learn · requests

---

## Licencia

MIT — libre uso con atribución.
