# Brechas Salariales de Género en Chile: un análisis multidimensional 🇨🇱

> *En Chile, las mujeres ganan en promedio menos que los hombres — pero ¿cuánto de esa brecha se explica por dónde trabajan, cuánto estudiaron o cuántos años tienen? ¿Y cuánto es simplemente discriminación?*

Este proyecto descompone la brecha salarial de género en Chile usando datos de la **Encuesta Suplementaria de Ingresos (ESI)** disponibles vía la API SDMX del SIMEL-INE, con cobertura nacional y regional desde 2010.

---

## Marco metodológico

La brecha salarial observada mezcla dos fenómenos distintos:

1. **Composición** — diferencias en características observables (educación, sector, horas, ocupación)
2. **Discriminación residual** — la parte que persiste después de controlar todo lo anterior

Este análisis aplica una **descomposición de Oaxaca-Blinder** para separar ambos componentes, respondiendo: *¿qué parte de la brecha desaparecería si hombres y mujeres tuvieran las mismas características?*

---

## Dimensiones de análisis

| Dataset SIMEL | Pregunta específica |
|---------------|---------------------|
| `DF_BGYMEDIOOCU` | ¿Cuál es la brecha por región y cómo evoluciona? |
| `DF_BGYMEDIOOCU_EDU` | ¿Más educación reduce la brecha o la amplía? |
| `DF_BGYMEDIOOCU_EDAD` | ¿En qué etapa de la vida es mayor la brecha? |
| `DF_BGYMEDIOOCU_RAMA` | ¿Qué sectores tienen la mayor y menor brecha? |
| `DF_BGYMEDIOOCU_CIUO` | ¿Cómo varía por grupo ocupacional? |
| `DF_BGYMEDIOOCU_TRAMOHORA` | ¿El trabajo a tiempo parcial amplifica la brecha? |
| `DF_BGYMEDIOOCU_CISE` | ¿Empleadas vs. independientes — quién enfrenta mayor brecha? |
| `DF_BGYHDEP_CISE_EDU` | Brecha en ingreso **por hora** según educación |
| `DF_BGYHDEP_CISE_EDAD` | Brecha en ingreso por hora según edad |
| `DF_BGREIMPROMSP` | Brecha en remuneración imponible (sistema de pensiones) |

---

## Hallazgos anticipados (hipótesis)

- La brecha es **mayor en los extremos educativos**: sin educación formal y con posgrado.
- Las mujeres con hijos pequeños enfrentan la mayor penalización salarial (*motherhood penalty*).
- La brecha **regional** es más pronunciada en zonas con economía extractiva (minería, pesca).
- El trabajo a tiempo parcial, mayoritariamente femenino, explica una fracción relevante de la brecha.

---

## Estructura del proyecto

```
brechas-salariales-genero-chile/
├── notebooks/
│   ├── 01_descarga_api.ipynb          ← descarga todos los datasets SIMEL
│   ├── 02_brecha_multidimensional.ipynb ← análisis por EDU, EDAD, RAMA, CIUO
│   ├── 03_evolucion_temporal.ipynb    ← tendencias 2010–2023 por región
│   ├── 04_descomposicion_oaxaca.ipynb ← Oaxaca-Blinder con datos ESI
│   └── 05_visualizaciones.ipynb       ← figuras publicables
├── src/
│   ├── oaxaca.py                      ← implementación descomposición
│   └── plots.py                       ← visualizaciones reutilizables
├── outputs/
│   ├── figures/
│   └── tables/
└── requirements.txt
```

---

## Cómo reproducir

```bash
git clone https://github.com/W00lscarf/brechas-salariales-genero-chile
cd brechas-salariales-genero-chile
pip install -r requirements.txt
jupyter lab
# Ejecutar en orden: 01 → 05
```

---

## Stack técnico

**Python 3.11** · pandas · numpy · matplotlib · seaborn · plotly · statsmodels · requests

---

## Nota metodológica

Los valores negativos en `DF_BGYMEDIOOCU_*` representan la brecha favorable a mujeres (situación atípica que también se analiza). Los valores positivos — la mayoría — representan el porcentaje en que el ingreso masculino supera al femenino:

```
Brecha = (Ingreso_H - Ingreso_M) / Ingreso_H × 100
```

---

## Licencia

MIT — libre uso con atribución.
