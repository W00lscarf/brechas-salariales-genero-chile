# Brechas Salariales de Género en Chile: un análisis multidimensional 🇨🇱

> *En Chile, las mujeres ganan en promedio menos que los hombres — pero ¿cuánto de esa brecha se explica por dónde trabajan, cuánto estudiaron, cuántas horas trabajan o cuántos años tienen? ¿Y cuánto queda sin explicación?*

Este proyecto descompone la brecha salarial de género en Chile en dos etapas: primero con **datos agregados oficiales** del SIMEL-INE (indicadores públicos vía API, sin autenticación), y luego con **microdatos individuales** de la Encuesta Suplementaria de Ingresos (ESI 2018-2024), que permiten una regresión multivariable real.

📄 **Los hallazgos completos, con marco teórico, metodología y recomendaciones de política, están sintetizados en el [policy paper](policy_paper/README.md)** — *"Misma ocupación, distinto salario: la brecha de género que la composición no explica"*.

---

## Marco metodológico

La brecha salarial observada mezcla dos fenómenos distintos:

1. **Composición** — diferencias en características observables (educación, sector, horas, ocupación, edad)
2. **Discriminación residual** — la parte que persiste después de controlar todo lo anterior

Los notebooks 01-05 exploran la brecha con datos agregados SIMEL (máximo 2 variables cruzadas simultáneamente — el techo real de ese tipo de datos). El notebook 06 rompe ese techo usando **microdatos individuales**, estimando una regresión tipo Mincer que controla por edad, edad², educación, horas trabajadas, categoría ocupacional y sector **al mismo tiempo**. El notebook 07 suma estado civil y presencia de hijos en el hogar, y aplica una **descomposición de Oaxaca-Blinder** para cuantificar qué porcentaje de la brecha total se explica por cada factor específico. El notebook 08 pone a prueba si el "residuo no explicado" depende de la resolución de la ocupación: usa microdatos de **CASEN** (que sí tiene ocupación a 4 dígitos CIUO, algo que la ESI no ofrece) para comparar controlar por ocupación amplia vs. ocupación exacta.

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
├── policy_paper/
│   └── README.md                          ← policy paper: marco teórico, metodología, resultados y propuestas
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
│   ├── 07_oaxaca_blinder_hijos.ipynb      ← estado civil, hijos y descomposición Oaxaca-Blinder por factor
│   └── 08_ocupacion_granular_casen.ipynb  ← CASEN 2022+2024: ¿la brecha se achica con ocupación a 4 dígitos?
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
| Microdatos CASEN 2022 y 2024 (Ministerio de Desarrollo Social, formato Stata) | Registros individuales con **ocupación a 4 dígitos CIUO-08** (356 categorías con muestra suficiente, frente a las ~9 de la ESI) | Pública, descarga manual desde el [Observatorio Social](https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen) |

**Nota de reproducibilidad:** los CSV de microdatos ESI (~100 MB cada uno) y las bases CASEN en Stata (hasta 1.6 GB) no se versionan en este repositorio por su tamaño. Para ejecutar los notebooks 06-07 descarga la ESI en `../ESI/`; para el notebook 08 descarga CASEN 2022 y 2024 en `../CASEN/` (misma carpeta que usa el proyecto hermano `empleabilidad-formacion-casen-chile`). La app interactiva funciona sin ninguna de las dos gracias a los resultados precalculados (`app_data/`).

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

**El notebook 08 responde una pregunta pendiente: ¿el residuo no explicado se debe a que "ocupación" estaba definida de forma muy amplia?** Usando CASEN 2022+2024 (que sí tiene ocupación a 4 dígitos CIUO-08, algo que la ESI no ofrece), se comparan dos regresiones idénticas salvo por el nivel de detalle ocupacional:

- **Control por ocupación amplia (1 dígito, ~9 categorías — equivalente a la ESI):** brecha ajustada -24.4%
- **Control por ocupación granular (4 dígitos, 356 categorías):** brecha ajustada -17.6%
- **Diferencia: 6.8 puntos porcentuales** — una parte real del "residuo no explicado" de los notebooks 06-07 es segregación ocupacional fina (ej. que los hombres se concentren en las especialidades mejor pagadas dentro de "Profesionales"), no solo discriminación en sentido estricto
- Aun así, **-17.6% sigue siendo una brecha grande sin explicar**, incluso comparando la misma ocupación exacta (ej. médicos generales: -12%, médicos especialistas: -20%, enfermeros: -3%, técnicos de enfermería: -13%)

El mismo notebook incluye un **ranking de 229 rubros específicos** (ocupaciones CIUO-08 a 4 dígitos, con al menos 20 hombres y 20 mujeres en la muestra) de menor a mayor brecha. Ejemplos de los extremos: "Conductores de camiones pesados" e "Ingenieros químicos" muestran brecha favorable a mujeres (+6.6% y +12.6%); "Cosmetólogos y especialistas en tratamiento de belleza" y "Avicultores" muestran las brechas más severas en contra de mujeres (-67% y -56%).

Una **descomposición de Oaxaca-Blinder** (misma metodología del notebook 07, ponderada por el factor de expansión `expr` de CASEN) rankea qué controles explican más de la brecha total:

| Control | % de la brecha explicado |
|---|---|
| **Ocupación (4 dígitos)** | **+22.2%** — el mayor factor, por lejos |
| Horas trabajadas | +12.7% |
| Educación | -10.7% (juega en sentido contrario: mujeres más educadas en promedio) |
| Edad | -1.6% |
| Año | -0.4% |
| **No explicado** | **77.8%** |

Ni siquiera el control más fino disponible en datos públicos chilenos logra explicar la mayoría de la brecha — pero sí confirma con precisión que la segregación ocupacional fina es el principal factor de composición identificado, muy por delante de horas y educación.

**¿Y si sumamos hijos y estado civil a la ocupación granular?** CASEN pregunta directamente `s5` ("¿cuántos hijos ha tenido?") a hombres y mujeres por igual — a diferencia de la ESI, donde el notebook 07 tuvo que aproximar "tiene hijos" con la composición del hogar. Repitiendo la interacción del notebook 07 pero ahora con ocupación a 4 dígitos controlada:

- **La interacción mujer×hijos es estadísticamente significativa aquí (-9.7%, p<0.001)** — a diferencia del notebook 07 (datos ESI), donde no lo era. Hay una penalización por maternidad real, no solo un efecto que pasa por estado civil.
- Ser soltera **atenúa** la brecha frente a ser casada/conviviente (+5.9%, p<0.001): la penalización más severa recae sobre **mujeres casadas o convivientes con hijos**.
- Pero en la descomposición de Oaxaca-Blinder, esto **no reduce el "no explicado"** — sube levemente de 77.8% a 82.2%. La razón: hombres y mujeres no difieren tanto en proporción de personas con hijos o en distribución de estado civil (poca diferencia de *composición*), así que el efecto es de *retorno* (el mismo hijo o el mismo estado civil pesa distinto en el salario de cada sexo) y queda absorbido en el residuo, no en la parte explicada.

En otras palabras: agregar hijos y estado civil no "explica más" brecha en el sentido contable de Oaxaca-Blinder, pero sí le pone nombre a una parte del residuo — una penalización por maternidad concentrada en mujeres casadas/convivientes, detectable solo gracias a controlar ocupación a nivel granular.

**¿Cuánto de la brecha por ocupación sobrevive al aislar el efecto sexo lo más posible?** El ranking de 229 ocupaciones (arriba) es crudo: solo compara ingresos promedio por sexo dentro de cada ocupación. Para aislar el efecto sexo, se ajustó un solo modelo con interacción `mujer × ocupación` (más edad, educación, horas, hijos, estado civil y año), donde los controles comunes se estiman con toda la muestra combinada (~151 mil personas) y solo el efecto sexo varía libremente por ocupación:

- **102 de 229 ocupaciones (44.5%) muestran una brecha ajustada estadísticamente significativa (p<0.05) — y las 102 son en contra de las mujeres.** El resultado resiste correcciones por comparaciones múltiples: 76 sobreviven la corrección FDR de Benjamini-Hochberg y 33 incluso Bonferroni — todas en contra.
- **Cero ocupaciones muestran una brecha significativamente favorable a mujeres.** Los casos "pro-mujer" del ranking crudo (joyeros +58.7%, músicos +41.0%, traductores +36.3%) tienen muestras chicas (n entre 55 y 148) y su ventaja aparente no se distingue del azar (p>0.2 en todos los casos) una vez que se contabiliza correctamente la incertidumbre estadística.
- La correlación entre brecha cruda y ajustada es 0.79: el orden general se mantiene, pero el promedio baja levemente (-17.7% a -16.7%) al controlar composición.

La evidencia sólida —la que resiste el control estadístico— apunta consistentemente en una sola dirección: en contra de las mujeres.

---

## Cómo reproducir

```bash
git clone https://github.com/W00lscarf/brechas-salariales-genero-chile
cd brechas-salariales-genero-chile
pip install -r requirements.txt
jupyter lab
# Notebooks 01-05: ejecutar en orden, no requieren nada adicional (descargan datos SIMEL automáticamente)
# Notebooks 06-07: requieren descargar microdatos ESI 2018-2024 del INE y ubicarlos en ../ESI/
# Notebook 08: requiere descargar microdatos CASEN 2022 y 2024 y ubicarlos en ../CASEN/
```

---

## Stack técnico

**Python 3.11** · pandas · numpy · matplotlib · seaborn · plotly · scipy · statsmodels · scikit-learn · patsy · streamlit · requests

---

## Licencia

MIT — libre uso con atribución.
