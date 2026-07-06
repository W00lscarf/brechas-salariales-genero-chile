# Brechas Salariales de Género en Chile: un análisis multidimensional 🇨🇱

> *En Chile, las mujeres ganan en promedio menos que los hombres — pero ¿cuánto de esa brecha se explica por dónde trabajan, cuánto estudiaron, cuántas horas trabajan o cuántos años tienen? ¿Y cuánto queda sin explicación?*

Este proyecto descompone la brecha salarial de género en Chile en dos etapas: primero con **datos agregados oficiales** del SIMEL-INE (indicadores públicos vía API, sin autenticación), y luego con **microdatos individuales** de la Encuesta Suplementaria de Ingresos (ESI 2018-2024), que permiten una regresión multivariable real.

📄 **Los hallazgos completos, con marco teórico, metodología y recomendaciones de política, están sintetizados en el [policy paper](policy_paper/README.md)** — *"Misma ocupación, distinto salario: la brecha de género que la composición no explica"*.

---

## Marco metodológico

La brecha salarial observada mezcla dos fenómenos distintos:

1. **Composición** — diferencias en características observables (educación, sector, horas, ocupación, edad)
2. **Discriminación residual** — la parte que persiste después de controlar todo lo anterior

Los notebooks 01-05 exploran la brecha con datos agregados SIMEL (máximo 2 variables cruzadas simultáneamente — el techo real de ese tipo de datos). El notebook 06 rompe ese techo usando **microdatos individuales**, estimando una regresión tipo Mincer que controla por edad, edad², educación, horas trabajadas, categoría ocupacional y sector **al mismo tiempo**. El notebook 07 suma estado civil y presencia de hijos en el hogar, y aplica una **descomposición de Oaxaca-Blinder** para cuantificar qué porcentaje de la brecha total se explica por cada factor específico. El notebook 08 pone a prueba si el "residuo no explicado" depende de la resolución de la ocupación: usa microdatos de **CASEN** (que sí tiene ocupación a 4 dígitos CIUO, algo que la ESI no ofrece) para comparar controlar por ocupación amplia vs. ocupación exacta. El notebook 09 somete los resultados a una batería de robustez: salario por hora, tres vectores de referencia en la descomposición, restricciones muestrales y separación por formalidad (asalariados formales/informales/independientes).

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
│   ├── 08_ocupacion_granular_casen.ipynb  ← CASEN 2022+2024: ¿la brecha se achica con ocupación a 4 dígitos?
│   └── 09_robustez.ipynb                  ← robustez: salario/hora, formalidad, sector público, geografía, institución, FDR
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
| Microdatos CASEN 2022 y 2024 (Ministerio de Desarrollo Social, formato Stata) | Registros individuales con **ocupación a 4 dígitos CIUO-08** (354 categorías con muestra suficiente, frente a las ~9 de la ESI) | Pública, descarga manual desde el [Observatorio Social](https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen) |

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

- **Control por ocupación amplia (1 dígito, ~9 categorías — equivalente a la ESI):** brecha ajustada -20.9%
- **Control por ocupación granular (4 dígitos, 354 categorías):** brecha ajustada -15.3%
- **Diferencia: 5.6 puntos porcentuales** — una parte real del "residuo no explicado" de los notebooks 06-07 es segregación ocupacional fina (ej. que los hombres se concentren en las especialidades mejor pagadas dentro de "Profesionales"), no solo discriminación en sentido estricto
- Aun así, **-15.3% sigue siendo una brecha grande sin explicar**, incluso comparando la misma ocupación exacta (ej. médicos generales: -12%, médicos especialistas: -20%, enfermeros: -3%, técnicos de enfermería: -13%)

El mismo notebook incluye un **ranking de 227 rubros específicos** (ocupaciones CIUO-08 a 4 dígitos, con al menos 20 hombres y 20 mujeres en la muestra) de menor a mayor brecha. Ejemplos de los extremos crudos: "Joyeros, orfebres y plateros" y "Traductores e intérpretes" muestran brechas favorables a mujeres (+58.6% y +47.5%) — que desaparecen al ajustar por composición (ver más abajo); "Cosmetólogos y especialistas en tratamiento de belleza" y "Avicultores" muestran las brechas más severas en contra de mujeres (-67% y -56%).

Una **descomposición de Oaxaca-Blinder** (misma metodología del notebook 07, ponderada por el factor de expansión `expr` de CASEN) rankea qué controles explican más de la brecha total:

| Control | % de la brecha explicado |
|---|---|
| **Horas trabajadas** | **+28.7%** — el mayor factor |
| **Ocupación (4 dígitos)** | **+17.0%** |
| Educación | -10.8% (juega en sentido contrario: mujeres más educadas en promedio) |
| Edad | -1.1% |
| Año | -0.4% |
| **No explicado** | **66.6%** |

Ni siquiera el control más fino disponible en datos públicos chilenos logra explicar la mayoría de la brecha — pero sí identifica con precisión los dos grandes factores de composición: las horas trabajadas y la segregación ocupacional fina, que juntas dan cuenta de casi toda la parte explicada.

**¿Y si sumamos hijos y estado civil a la ocupación granular?** CASEN pregunta directamente `s5` ("¿cuántos hijos ha tenido?") a hombres y mujeres por igual — a diferencia de la ESI, donde el notebook 07 tuvo que aproximar "tiene hijos" con la composición del hogar. Repitiendo la interacción del notebook 07 pero ahora con ocupación a 4 dígitos controlada:

- **La interacción mujer×hijos es estadísticamente significativa aquí (-7.8%, p<0.001)** — a diferencia del notebook 07 (datos ESI), donde no lo era. Hay una penalización por maternidad real, no solo un efecto que pasa por estado civil — y para los hombres, tener hijos se asocia a un *premio* de +5.0%.
- Ser soltera **atenúa** la brecha frente a ser casada/conviviente (+5.3%, p<0.001): la penalización más severa recae sobre **mujeres casadas o convivientes con hijos**.
- Pero en la descomposición de Oaxaca-Blinder, esto **no reduce el "no explicado"** — sube levemente de 66.6% a 70.9%. La razón: hombres y mujeres no difieren tanto en proporción de personas con hijos o en distribución de estado civil (poca diferencia de *composición*), así que el efecto es de *retorno* (el mismo hijo o el mismo estado civil pesa distinto en el salario de cada sexo) y queda absorbido en el residuo, no en la parte explicada.

En otras palabras: agregar hijos y estado civil no "explica más" brecha en el sentido contable de Oaxaca-Blinder, pero sí le pone nombre a una parte del residuo — una penalización por maternidad concentrada en mujeres casadas/convivientes, detectable solo gracias a controlar ocupación a nivel granular.

**¿Cuánto de la brecha por ocupación sobrevive al aislar el efecto sexo lo más posible?** El ranking de 227 ocupaciones (arriba) es crudo: solo compara ingresos promedio por sexo dentro de cada ocupación. Para aislar el efecto sexo, se ajustó un solo modelo con interacción `mujer × ocupación` (más edad, educación, horas, hijos, estado civil y año), donde los controles comunes se estiman con toda la muestra combinada (~149 mil personas) y solo el efecto sexo varía libremente por ocupación:

- **90 de 227 ocupaciones (39.6%) muestran una brecha ajustada estadísticamente significativa (p<0.05) — 89 en contra de las mujeres y solo 1 a favor** (conductores de buses, +15.1%, p=0.029), dentro de lo esperable por azar con 227 tests. Tras corregir por comparaciones múltiples, 66 sobreviven FDR de Benjamini-Hochberg y 30 incluso Bonferroni — **todas en contra de las mujeres; ninguna a favor**.
- Los casos "pro-mujer" del ranking crudo se desvanecen al ajustar por composición: joyeros pasa de +58.6% crudo a -5.5% ajustado (no significativo); músicos (+37.9%) y traductores (+47.5%) tampoco son significativos ajustados (p>0.27; muestras de 51 a 143 casos).
- La correlación entre brecha cruda y ajustada es 0.79: el orden general se mantiene, pero el promedio se modera (-17.8% a -14.8%) al controlar composición.

La evidencia sólida —la que resiste el control estadístico— apunta consistentemente en una sola dirección: en contra de las mujeres.

**El notebook 09 somete todo lo anterior a una batería de robustez** (salario por hora, tres vectores de referencia en Oaxaca-Blinder, edad prima, recorte de outliers, y separación formal/informal/independiente):

- La brecha ajustada **nunca baja de -11%** bajo ninguna especificación: -15.3% baseline, **-15.6% con la especificación máxima (todos los controles simultáneos — agregar controles no la reduce)**, -15.7% sumando región y zona urbano/rural, -15.6% sumando tipo de institución de educación superior, -14.9% edad prima, -13.0% sin outliers, -12.0% solo asalariados formales que cotizan, -11.1% en salario por hora, -10.6% solo universitarios con tipo de institución controlado
- **¿Formal con formal?** La composición por formalidad casi no difiere por sexo (asalariados: 74.6% hombres vs 77.7% mujeres) — la brecha no es un artefacto de mezclar universos. Como control en la muestra completa, la formalidad apenas mueve el coeficiente (-15.3% → -15.2%) pese a predecir fuerte el nivel de ingreso (cotizar: +30%). Pero la brecha sí es heterogénea: **entre independientes se dispara a -25.5%**, el segmento sin contrato ni fiscalización posible
- El ranking de factores de Oaxaca-Blinder (horas primero, ocupación segundo, educación en contra) es idéntico bajo las tres referencias; el "no explicado" varía de 49% a 71% según la convención, nunca por debajo de aproximadamente la mitad
- En salario por hora, bajo Bonferroni ninguna ocupación favorece significativamente a las mujeres (la única excepción bajo FDR — conductoras de taxis, +13.1%/hora — refleja las jornadas extremas de los conductores hombres, que diluyen su salario por hora)
- **Sector público vs privado**: la brecha es menor en el empleo público (-9.8% vs -12.7%; diferencia marginalmente significativa, p=0.078), coherente con remuneraciones regidas por escalas — pero persiste incluso ahí. Las mujeres están sobrerrepresentadas en el sector público (56% de ese empleo es femenino)

---

## Cómo reproducir

```bash
git clone https://github.com/W00lscarf/brechas-salariales-genero-chile
cd brechas-salariales-genero-chile
pip install -r requirements.txt
jupyter lab
# Notebooks 01-05: ejecutar en orden, no requieren nada adicional (descargan datos SIMEL automáticamente)
# Notebooks 06-07: requieren descargar microdatos ESI 2018-2024 del INE y ubicarlos en ../ESI/
# Notebooks 08-09: requieren descargar microdatos CASEN 2022 y 2024 y ubicarlos en ../CASEN/
```

---

## Stack técnico

**Python 3.11** · pandas · numpy · matplotlib · seaborn · plotly · scipy · statsmodels · scikit-learn · patsy · streamlit · requests

---

## Licencia

MIT — libre uso con atribución.
