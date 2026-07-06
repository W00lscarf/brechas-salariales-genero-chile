# Misma ocupación, distinto salario

## La brecha de género que la composición no explica: evidencia desde microdatos públicos y propuestas de política para Chile

*Policy paper elaborado a partir de los resultados del repositorio [`brechas-salariales-genero-chile`](https://github.com/W00lscarf/brechas-salariales-genero-chile). Todos los cálculos son reproducibles con datos públicos y código abierto (notebooks 01-09).*

**Julio 2026**

---

## Resumen ejecutivo

- Con microdatos públicos de la Encuesta Suplementaria de Ingresos (ESI 2018-2024) y CASEN (2022 y 2024), estimamos que las mujeres ocupadas en Chile ganan en promedio **22-26% menos** que los hombres por su trabajo principal, según fuente y período.
- Controlando simultáneamente por edad, educación, horas trabajadas, año y **ocupación exacta a 4 dígitos CIUO-08** (354 categorías, el control más fino posible con datos públicos chilenos), la brecha ajustada es **-15.3%**. Las horas trabajadas (28.7%) y la ocupación granular (17.0%) son los dos mayores factores de composición identificados, pero la mayoría del diferencial —**en torno a dos tercios**— permanece sin explicar por composición.
- **La penalización por maternidad es identificable y significativa**: dentro de la misma ocupación exacta, una mujer con hijos gana un **7.8% adicional menos** (p<0.001) que lo que la brecha general ya le descuenta, mientras que para los hombres tener hijos se asocia a un *premio* salarial (+5.0%). El costo se concentra en mujeres casadas o convivientes.
- Al aislar el efecto sexo ocupación por ocupación, **90 de 227 ocupaciones muestran brecha estadísticamente significativa — 89 en contra de las mujeres y solo una a favor, dentro de lo esperable por azar**. Tras la corrección por comparaciones múltiples, 66 ocupaciones sobreviven FDR y 30 el criterio de Bonferroni — **todas en contra de las mujeres; ninguna a favor**. Las brechas "pro-mujer" que aparecen en comparaciones simples no sobreviven el ajuste por composición ni el control de incertidumbre estadística.
- Los resultados sobreviven una **batería de robustez** (sección 7): especificación en salario por hora (-11.1%), restricción a asalariados formales que cotizan (-12.0%), edad prima 25-59 (-14.9%), recorte de outliers (-13.0%) y tres vectores de referencia en la descomposición. La **especificación máxima** — todos los controles disponibles simultáneamente, incluyendo sector público/privado y formalidad — arroja **-15.6%**: agregar controles no reduce la brecha. La más severa está entre trabajadores independientes (-25.5%); la más baja, en el sector público (-9.8%), donde las escalas salariales la comprimen pero no la eliminan.
- La brecha **no golpea parejo**: es el doble en los hogares de menor nivel socioeconómico (-21.2%) que en los de mayor (-11.2%), y tiene **forma de U** a lo largo de la distribución salarial — piso pegajoso y techo de cristal simultáneos (sección 4.8). Es también un problema de desigualdad: castiga más donde cada punto de ingreso vale más.
- Estos resultados indican que la brecha chilena es mayoritariamente un problema de **retornos desiguales** (lo que se paga a iguales características) y no solo de **composición** (dónde trabajan hombres y mujeres). Las políticas deben calibrarse a ese diagnóstico: transparencia salarial con reporte de brechas ajustadas, reforma del artículo 203 del Código del Trabajo (sala cuna), corresponsabilidad parental efectiva y expansión de la oferta pública de cuidado.

---

## 1. Introducción

La participación laboral femenina en Chile ronda el 53%, unos 18 puntos por debajo de la masculina (INE, 2024), y las mujeres que sí participan ganan sistemáticamente menos. La magnitud reportada de esa brecha varía según la definición: el indicador de la OCDE —que compara medianas de ingreso entre asalariados a jornada completa— arroja cifras en torno a un dígito alto para Chile, mientras que definiciones más amplias (medias sobre todos los ocupados, incluyendo independientes y jornadas parciales) la sitúan por sobre el 20%, consistente con el promedio mundial ponderado por factores que estima la OIT (2018) en torno al 19%.

Para el diseño de políticas, la magnitud importa menos que la **descomposición**: ¿cuánto de la brecha se debe a que hombres y mujeres trabajan en distintas ocupaciones, sectores y jornadas (*composición*), y cuánto a que características idénticas se remuneran distinto según el sexo (*retornos*)? La respuesta determina el instrumento. Si la brecha fuera principalmente composición, las políticas eficaces serían las de desegregación ocupacional (orientación vocacional, pipelines STEM, cuotas). Si es principalmente retornos, se requieren instrumentos que actúen sobre la fijación de salarios: transparencia, fiscalización, negociación y redistribución de los costos del cuidado.

Este documento aporta a esa discusión con una ventaja metodológica poco frecuente en el debate público chileno: el uso de la ocupación a **4 dígitos de la clasificación CIUO-08** disponible en CASEN, que permite comparar salarios dentro de la misma ocupación específica (médico especialista con médico especialista, técnico en enfermería con técnico en enfermería), en lugar de las ~9 categorías amplias que permiten las encuestas de empleo habituales. La crítica estándar a las estimaciones de brecha "ajustada" —que el residuo no explicado sería un artefacto de controles ocupacionales demasiado gruesos— se puede someter a prueba directa. Hasta donde conocemos, los estudios chilenos publicados y los boletines oficiales de brecha salarial trabajan con agrupaciones ocupacionales amplias (1 dígito CIUO o grandes grupos); no identificamos estimaciones publicadas de brechas dentro de la ocupación a 4 dígitos con inferencia estadística y datos de acceso abierto para Chile.

Este ejercicio se sitúa, además, cerca del **techo de lo estimable con datos abiertos en el país**: los diseños que la literatura internacional utiliza para ir más lejos —datos administrativos vinculados empleador-empleado, estudios de eventos en torno al nacimiento del primer hijo— requieren fuentes que en Chile existen solo de forma parcial y bajo acceso restringido (los registros del Seguro de Cesantía, usados por ejemplo en Sánchez, Finot y Villena-Roldán, 2020, cubren únicamente al sector privado formal asalariado; los datos tributarios del SII y los paneles EPS y ELPI tienen restricciones análogas de acceso o cobertura). Esa restricción de infraestructura de datos es, en sí misma, parte del diagnóstico de este documento (recomendación R5).

Los resultados están disponibles en un repositorio público con código y datos de acceso abierto, lo que permite a cualquier investigador o servicio público replicar, auditar y extender las estimaciones.

---

## 2. Marco teórico

### 2.1 Capital humano y la ecuación de salarios

El punto de partida canónico es la función de ingresos de Mincer (1974), que modela el logaritmo del salario como función de la escolaridad y la experiencia potencial. En ese marco, una brecha de género sería atribuible a diferencias en acumulación de capital humano. La evidencia contemporánea descarta esa explicación para las economías de ingreso medio y alto: las mujeres jóvenes igualan o superan a los hombres en escolaridad — patrón que confirmamos para Chile, donde la educación *juega en contra* de la brecha observada (las ocupadas están, en promedio, más educadas que los ocupados).

### 2.2 Descomposición composición/retornos

Oaxaca (1973) y Blinder (1973) formalizaron la descomposición del diferencial salarial en una parte **explicada** por diferencias en características promedio (educación, horas, ocupación) y una parte **no explicada**, atribuible a retornos distintos por sexo sobre las mismas características. Blau y Kahn (2017), en la revisión más citada de esta literatura, documentan para Estados Unidos que el capital humano convencional dejó de explicar la brecha, y que los factores dominantes pasaron a ser la ocupación, la industria y el componente no explicado.

Dos advertencias de interpretación acompañan a esta metodología y aplican a nuestros resultados: (i) el componente "no explicado" no es sinónimo de discriminación — incluye cualquier variable omitida que correlacione con el sexo; (ii) el componente "explicado" tampoco es necesariamente *no discriminatorio* — la segregación ocupacional puede ser, en sí misma, resultado de barreras y normas (Bertrand, Goldin y Katz, 2010).

### 2.3 Segregación ocupacional y el problema de la granularidad

Petersen y Morgan (1995) mostraron para Estados Unidos que, al comparar dentro de la misma ocupación *y establecimiento*, la brecha se reduce drásticamente: la mayor parte del diferencial operaría vía segregación — a qué trabajos y empresas acceden hombres y mujeres. Card, Cardoso y Kline (2016) refinaron el diagnóstico con datos administrativos portugueses: las mujeres se concentran en firmas que pagan menos y capturan una fracción menor de las rentas de la firma en la negociación.

Esta literatura genera una predicción testeable para Chile: **si la brecha ajustada chilena fuera principalmente un artefacto de controles ocupacionales gruesos, debería desplomarse al controlar por ocupación a 4 dígitos.** Nuestro diseño somete a prueba exactamente esa hipótesis (sección 4.2).

Goldin (2014) aporta el mecanismo complementario: buena parte de la brecha residual dentro de ocupaciones se concentra en trabajos con retornos convexos a las horas — los "trabajos codiciosos" (*greedy jobs*) que pagan desproporcionadamente la disponibilidad total y penalizan la flexibilidad, que las mujeres demandan más por la asignación asimétrica del cuidado (Goldin, 2021).

### 2.4 La penalización por maternidad

La literatura de *child penalties* con estudios de eventos muestra que el nacimiento del primer hijo abre una brecha de ingresos persistente entre madres y padres: alrededor de 20% en el largo plazo en Dinamarca (Kleven, Landais y Søgaard, 2019) y sustancialmente mayor en América Latina (Kleven, Landais y Leite-Mariante, 2024). Cortés y Pan (2023) concluyen que los hijos son hoy el factor individual más importante detrás de las brechas de género restantes en los mercados laborales desarrollados. Bertrand, Goldin y Katz (2010) documentan el mecanismo en profesionales de alto ingreso: brecha casi nula al egreso, que se expande tras la llegada de los hijos vía interrupciones y reducción de horas — de las madres, no de los padres.

### 2.5 Discriminación de gustos y estadística

Los modelos clásicos de discriminación por preferencias (Becker, 1957) y discriminación estadística (Phelps, 1972; Arrow, 1973) predicen diferenciales de trato ante productividad idéntica. No podemos identificar discriminación directamente con datos observacionales, pero el diseño de la sección 4.5 —efecto sexo estimado dentro de cada ocupación exacta, neto de edad, educación, horas, hijos y estado civil— acota el espacio de explicaciones alternativas de manera considerablemente más exigente que las estimaciones convencionales.

---

## 3. Datos y metodología

### 3.1 Fuentes

| Fuente | Período | Uso |
|---|---|---|
| **ESI** (INE), microdatos públicos | 2018-2024 | Brecha bruta y ajustada anual; descomposición Oaxaca-Blinder con proxy de hijos en el hogar |
| **CASEN** (Ministerio de Desarrollo Social), microdatos públicos | 2022, 2024 | Ocupación CIUO-08 a 4 dígitos; pregunta directa de fecundidad (`s5`); estado civil (`ecivil`) |

Ambas encuestas tienen diseño muestral complejo. Todas las estimaciones usan los **factores de expansión** oficiales (WLS ponderado) y errores estándar **cluster-robustos por conglomerado muestral × año** (`varunit`), siguiendo la recomendación estándar para encuestas de hogares. El ingreso analizado es el del trabajo principal (`ytrabajocor` en CASEN), en logaritmo. CASEN 2017 se excluye del análisis granular porque codifica ocupación en CIUO-88, clasificación no comparable con la CIUO-08 de 2022/2024.

### 3.2 Muestra analítica (CASEN)

Ocupados con ingreso positivo y ocupación válida: **176.542 personas** (2022+2024 combinados), en 444 códigos ocupacionales distintos. Se excluyen los registros con horas semanales inválidas (código -88, "no sabe", y valores sobre 112 horas), lo que deja una muestra analítica de **174.924 personas**; 354 códigos ocupacionales alcanzan n≥30. Para los análisis por ocupación específica se exige además **≥20 hombres y ≥20 mujeres** por celda, lo que deja **227 ocupaciones**.

### 3.3 Estrategia empírica

1. **Regresión minceriana con dos niveles de granularidad.** Misma especificación (`log ingreso ~ mujer + edad + edad² + educación + horas + año`), cambiando únicamente el control ocupacional: 1 dígito CIUO (~9 categorías, lo que permite la ESI) versus 4 dígitos (354 categorías). La diferencia entre ambos coeficientes de `mujer` aísla el aporte puro de la granularidad.
2. **Descomposición de Oaxaca-Blinder ponderada**, agrupando las contribuciones por familia de variable (educación, edad, horas, ocupación, hijos, estado civil, año), para rankear qué controles explican más de la brecha total.
3. **Interacciones mujer×hijos y mujer×estado civil**, con la pregunta directa de fecundidad de CASEN (a diferencia de la ESI, que exige aproximar maternidad por composición del hogar).
4. **Modelo de interacción completa `mujer × ocupación`** sobre las 227 ocupaciones: los controles comunes se estiman con toda la muestra (~149.000 observaciones) y el efecto sexo se deja variar libremente por ocupación. El efecto por ocupación se recupera como combinación lineal de coeficientes, con varianza calculada desde la matriz de covarianza cluster-robusta. Este diseño es más eficiente que estimar 227 regresiones separadas con 50-100 casos cada una.
5. **Batería de robustez** (sección 7): salario por hora, tres vectores de referencia de Oaxaca-Blinder, edad prima, recorte de outliers, y separación por formalidad (asalariados formales/informales/independientes, vía categoría ocupacional `o15`, contrato firmado `o19` y cotización previsional `o32`).

### 3.4 Reproducibilidad

Código completo, figuras y tablas derivadas en el repositorio; los microdatos se descargan gratuitamente de los sitios oficiales del INE y del Observatorio Social del MDS. Ningún dato es de acceso restringido.

---

## 4. Resultados

### 4.1 La brecha bruta apenas se mueve con los controles convencionales (ESI)

Con microdatos ESI 2018-2024 (pooled), la brecha bruta de ingreso medio del trabajo principal es **-22.7%**. Controlando por edad, edad², educación, horas, categoría ocupacional (1 dígito) y sector: **-20.7%** (IC 95%: -21.4 a -20.0). La descomposición de Oaxaca-Blinder con estado civil e hijos (proxy de hogar) explica el **23.1%** del diferencial; el **76.9% queda sin explicar**. La brecha ajustada y la bruta se mueven casi en paralelo durante los 7 años de la serie: no hay evidencia de que la brecha chilena sea un artefacto de composición del mercado laboral.

### 4.2 La prueba de granularidad: la segregación fina explica una parte real, pero minoritaria

La crítica de Petersen y Morgan aplicada a Chile — ¿desaparece la brecha al comparar ocupaciones exactas? — se responde con CASEN:

| Especificación (idéntica salvo el control ocupacional) | Brecha ajustada | R² |
|---|---|---|
| Ocupación **amplia** (1 dígito, ~9 categorías — equivalente ESI) | **-20.9%** (IC95: -21.7 a -20.0) | 0.488 |
| Ocupación **granular** (4 dígitos, 354 categorías) | **-15.3%** (IC95: -16.2 a -14.4) | 0.537 |
| **Diferencia** | **+5.6 pp** | |

La granularidad importa: una parte real de lo que las estimaciones convencionales reportan como "no explicado" es **segregación ocupacional fina** — dentro de "Profesionales", los hombres se concentran en las especialidades mejor pagadas. Pero la brecha no se desploma: **-15.3% persiste comparando la misma ocupación exacta**. Incluso dentro de ocupaciones idénticas: médicos especialistas -20%, técnicos de enfermería -13%, enfermeros -3%.

### 4.3 Ranking de factores: qué explica la brecha y cuánto

Descomposición de Oaxaca-Blinder sobre la brecha total de 22.6% (CASEN 2022+2024), con y sin controles de familia:

| Factor | Sin hijos/estado civil | Con hijos/estado civil |
|---|---|---|
| Horas trabajadas | **+28.7%** | **+27.8%** |
| Ocupación (4 dígitos) | **+17.0%** | **+14.2%** |
| Estado civil | — | +1.8% |
| Tiene hijos | — | -1.4% |
| Edad | -1.1% | -2.0% |
| Educación | **-10.8%** | **-10.9%** |
| Año | -0.4% | -0.4% |
| **No explicado** | **66.6%** | **70.9%** |

Tres lecturas de política se desprenden de esta tabla:

1. **Las horas trabajadas son el mayor factor de composición identificado (~29% de la brecha), seguidas de la segregación ocupacional fina (~17%)** — entre ambas dan cuenta de casi toda la parte explicada.
2. **La educación protege**: las ocupadas chilenas están mejor educadas que los ocupados; si solo importara el capital humano, ganarían *más*.
3. **Hijos y estado civil casi no aportan a la parte explicada** — hombres y mujeres no difieren tanto en composición familiar promedio. Su efecto opera por otra vía (sección 4.4).

### 4.4 La penalización por maternidad: un efecto de retornos, no de composición

Interacción mujer×hijos y mujer×estado civil, controlando ocupación exacta, educación, edad, horas y año (n=174.719):

| Término | Efecto sobre el ingreso | p-valor |
|---|---|---|
| Mujer (brecha base) | -12.3% | <0.001 |
| Tiene hijos (efecto para hombres) | **+5.0%** | <0.001 |
| **Mujer × tiene hijos** | **-7.8%** | **<0.001** |
| Mujer × soltera (vs. casada/conviviente) | +5.3% | <0.001 |

El contraste es nítido: **la paternidad se asocia a un premio salarial; la maternidad, a una penalización adicional** por sobre la brecha que ya afecta a toda mujer — exactamente el patrón que la literatura internacional de *child penalties* documenta con datos administrativos (Kleven et al., 2019; Cortés y Pan, 2023). Notablemente, con datos ESI (sin ocupación granular) esta interacción no era estadísticamente significativa: la granularidad ocupacional fue la que permitió identificarla, lo que sugiere que parte de la penalización por maternidad en Chile opera *dentro* de las ocupaciones y no solo a través de la selección hacia ocupaciones peor pagadas.

Este hallazgo también resuelve la aparente paradoja de la tabla anterior: agregar hijos y estado civil *sube* el "no explicado" (66.6% → 70.9%) porque la descomposición solo asigna al componente explicado las diferencias de composición promedio — y la penalización por maternidad es una diferencia de **retorno** (el mismo hijo impacta distinto según el sexo del progenitor), no de composición.

### 4.5 Aislando el efecto sexo ocupación por ocupación

El resultado central del análisis. Con el modelo de interacción completa (efecto sexo específico a cada una de las 227 ocupaciones, neto de edad, educación, horas, hijos, estado civil y año):

- **90 de 227 ocupaciones (39.6%) presentan brecha ajustada estadísticamente significativa (p<0.05): 89 en contra de las mujeres y solo 1 a favor** (conductores de buses y trolebuses, +15.1%, p=0.029) — exactamente lo que se esperaría del azar, dado que con 227 contrastes simultáneos ~11 falsos positivos son esperables a p<0.05.
- **Tras la corrección por comparaciones múltiples el resultado se depura**: 66 ocupaciones sobreviven la corrección FDR de Benjamini-Hochberg (q<0.05) y 30 sobreviven incluso el criterio de Bonferroni, el más conservador disponible — la totalidad, sin excepción, en contra de las mujeres (la brecha "a favor" en buses no sobrevive: p-FDR=0.08).
- Las aparentes ventajas femeninas de las comparaciones simples se desvanecen al ajustar por composición: joyería pasa de +58.6% crudo a -5.5% ajustado (no significativo); música (+37.9%) y traducción (+47.5%) tampoco son significativas ajustadas (p>0.27; celdas de 51 a 143 casos).
- La correlación entre brecha cruda y ajustada es 0.79: el orden se conserva, el promedio se modera (-17.8% → -14.8%).

![Brecha cruda vs ajustada por ocupación](../notebooks/outputs/figures/ranking_ajustado_vs_crudo.png)

La distribución completa (227 ocupaciones, con brecha cruda, ajustada, p-valor corregido por FDR y tamaños muestrales) está publicada como dato abierto en [`ranking_brecha_ocupacion_ajustada.csv`](../notebooks/outputs/data/ranking_brecha_ocupacion_ajustada.csv).

### 4.6 Síntesis del diagnóstico

| Componente de la brecha (22.6% total) | Magnitud aproximada | ¿Qué es? |
|---|---|---|
| Horas trabajadas | ~29% | Composición/preferencias restringidas |
| Segregación ocupacional fina | ~17% | Composición: dónde trabajan |
| Educación | negativa (protege) | Composición |
| Retornos desiguales (incl. penalización por maternidad) | **~2/3** | Cómo se paga a iguales características |

El problema chileno es, predominantemente, de **retornos**: características idénticas se remuneran distinto según el sexo, con la maternidad como el mecanismo identificable más claro dentro de ese residuo.

### 4.7 La lectura de "elecciones": qué queda de ella

La interpretación más frecuente para restar urgencia a la brecha salarial es atribuirla a **decisiones libres de las mujeres** — de carrera, de horas, de sector, de familia. El diseño de este trabajo está deliberadamente orientado a someter cada versión de esa lectura a prueba directa:

| La objeción: "es producto de elecciones..." | Prueba aplicada | Resultado |
|---|---|---|
| *...de ocupación: eligen oficios peor pagados* | Control por ocupación exacta a 4 dígitos (354 categorías) | La brecha se reduce (-20.9% → -15.3%) pero **persiste dentro de la misma ocupación exacta** |
| *...de horas: trabajan menos* | Control de horas + especificación en salario por hora | **-11.1% por hora trabajada**, misma ocupación |
| *...de régimen: prefieren empleos informales o flexibles* | Separación y control por formalidad (contrato, cotización, categoría) | Composición casi idéntica por sexo; **-12.0% entre asalariados formales** |
| *...de sector: optan por el sector público, más compatible* | Separación público/privado | **-9.8% incluso dentro del sector público**, con sus escalas regladas |
| *...familiares: priorizan los hijos sobre la carrera* | Interacción mujer×hijos, mujer×estado civil | **El mismo hijo se asocia a +5.0% para él y -7.8% adicional para ella.** Una "elección familiar" simétrica no produce efectos asimétricos por sexo |
| *...educativas: invierten menos en capital humano o estudian en peores instituciones* | Control por nivel educativo y por tipo de institución de educación superior | Juega al revés: las ocupadas están **más** educadas (contribución -10.3%), y el tipo de institución no mueve el coeficiente. Entre universitarios con tipo de institución controlado: -10.6% |
| *...geográficas: viven en mercados laborales distintos* | Efectos fijos de región (16) y zona urbano/rural | La brecha queda en **-15.7%** — una décima más que sin geografía |
| *"Es un artefacto estadístico"* | FDR/Bonferroni, outliers, forma funcional, referencias de la descomposición | El patrón sobrevive todas las correcciones |

Y la prueba de síntesis: la **especificación máxima** — que descuenta simultáneamente todas las "elecciones" observables — no reduce la brecha, la deja en -15.6%.

Dos vías de escape permanecen abiertas, y conviene nombrarlas con honestidad. Primero, la **experiencia laboral efectiva**: la edad captura experiencia *potencial*, no trayectorias reales — si las mujeres acumulan menos años efectivos por interrupciones de carrera, parte del residuo lo reflejaría (aunque esas interrupciones son, precisamente, la penalización por maternidad operando por otro canal, no una preferencia). Segundo, el **sorting entre firmas y la negociación** (Card, Cardoso y Kline, 2016), inobservable sin datos administrativos vinculados. Ninguna de las dos rescata la lectura de "elecciones libres": la primera es en gran medida consecuencia de la asignación asimétrica del cuidado que este trabajo documenta (el efecto asimétrico de los hijos), y la segunda es un mecanismo de mercado, no una preferencia. A esto se suma que, por el problema de sobre-control (sección 2.2), estas estimaciones son **pisos**: si la segregación ocupacional o las horas son a su vez elecciones restringidas por normas y barreras, parte de lo "explicado" también es discriminación.

### 4.8 ¿Para quién es más grande la brecha? Gradiente socioeconómico y forma de U

La brecha promedio esconde una heterogeneidad de primera importancia para la focalización de políticas (notebook 09, sección 6). Por **nivel socioeconómico del hogar** — medido con el ingreso del *resto* del hogar per cápita, para evitar el sesgo mecánico de que el menor ingreso de las mujeres empuje a sus hogares hacia abajo — la brecha ajustada exhibe un gradiente nítido:

| Corte | Brecha ajustada |
|---|---|
| NSE del hogar: Bajo | **-21.2%** |
| NSE: Medio-bajo | -17.0% |
| NSE: Medio-alto | -15.6% |
| NSE: Alto | **-11.2%** |
| Educación básica | -21.2% |
| Educación media | -19.1% |
| Técnica superior | -16.9% |
| Universitaria | **-8.4%** |
| Posgrado | **-14.6%** |

(El quintil oficial `qaut` muestra el mismo gradiente: Q1 -22.3% → Q4 -10.5%.)

Tres lecturas de política:

1. **La brecha de género es también un problema de desigualdad.** Es el doble en los hogares de menor NSE que en los de mayor NSE — castiga más exactamente donde cada punto porcentual de ingreso vale más en bienestar, y donde la mujer tiene menos poder de negociación individual. Las políticas de brecha salarial suelen diseñarse pensando en profesionales de altos ingresos; estos datos indican que la urgencia distributiva está en la base.
2. **El rebote en posgrado** (-14.6%, frente a -8.4% de las universitarias sin posgrado) es una señal de techo de cristal: las mujeres más calificadas del país enfrentan una brecha casi el doble que las universitarias.
3. **A lo largo de la distribución salarial, la brecha tiene forma de U** (regresión cuantílica con controles completos: en torno a -15% en el decil inferior, -12% en la mediana, -16% en el decil superior): Chile exhibe **piso pegajoso y techo de cristal simultáneamente**, el patrón que Albrecht, Björklund y Vroman (2003) documentaron para Suecia y Arulampalam, Booth y Bryan (2007) para Europa. La implicancia es que no hay un instrumento único: en la base operan la fiscalización, el salario mínimo y la formalización; en la cima, la transparencia salarial, los criterios objetivos de promoción y la corresponsabilidad.

![Brecha por cuantil](../notebooks/outputs/figures/brecha_por_cuantil.png)

---

## 5. Marco institucional vigente y sus límites

Chile ratificó el Convenio 100 de la OIT (igualdad de remuneración) en 1971. El instrumento interno principal es la **Ley 20.348 (2009)**, que incorporó el artículo 62 bis al Código del Trabajo: derecho a la igualdad de remuneraciones entre hombres y mujeres que presten "un mismo trabajo". Su diseño presenta tres debilidades documentadas: exige identidad de funciones (no trabajo de igual valor, el estándar OIT), radica la carga de reclamar en la trabajadora individual mediante un procedimiento interno previo, y carece de un mecanismo de reporte que haga observables las brechas. El volumen de denuncias y sanciones ha sido marginal desde su entrada en vigencia.

El **artículo 203 del Código del Trabajo** obliga a financiar sala cuna solo a los empleadores con **20 o más trabajadoras**. Al gravar la contratación femenina en el margen, la norma genera exactamente la distorsión que la teoría predice: Prada, Rucci y Urzúa (2015) documentan que el costo se traslada a menores salarios de contratación de las mujeres en las firmas afectadas. El proyecto de sala cuna universal que corrige este diseño lleva años en tramitación legislativa.

La **Ley 20.545 (2011)** extendió el postnatal parental a 24 semanas con semanas transferibles al padre; el uso paterno ha sido persistentemente inferior al 1%, lo que en la práctica consolida la asignación asimétrica del cuidado que la literatura identifica como el motor de la penalización por maternidad.

---

## 6. Recomendaciones de política

Las recomendaciones se ordenan por el componente de la brecha sobre el que actúan, siguiendo el diagnóstico de la sección 4.6.

### R1. Transparencia salarial obligatoria con brechas ajustadas por ocupación *(actúa sobre: retornos)*

Obligación legal para empresas sobre un umbral de tamaño de calcular y reportar periódicamente su brecha salarial de género **por categoría ocupacional comparable**, con difusión a trabajadores y sindicatos. La evidencia causal de alto estándar es favorable: la ley danesa de reporte redujo la brecha en torno a un 13% relativo, principalmente moderando el crecimiento salarial masculino, sin efectos negativos de empleo (Bennedsen, Simintzi, Tsoutsoura y Wolfenzon, 2022); la transparencia en universidades canadienses la redujo del orden de 20-30% (Baker, Halberstam, Kroft, Mas y Messacar, 2023). Cullen (2024) resume las condiciones de diseño que evitan efectos adversos sobre la negociación individual. La transparencia debe incluir además la **negociabilidad y los rangos salariales de cada cargo**: mostrar referencias salariales del mercado elimina la brecha de peticiones que explica gran parte del diferencial en contrataciones (Roussille, 2024), y explicitar que el salario es negociable elimina la diferencia por sexo en la propensión a negociar (Leibbrandt y List, 2015). La evidencia local apunta en la misma dirección: en el sector público chileno, donde la remuneración se rige por escalas y grados de conocimiento público, la brecha ajustada es menor que en el privado (-9.8% vs -12.7%, sección 7) — aunque el remanente indica que la transparencia debe cubrir el total de la remuneración (asignaciones, bonos, ascensos), no solo el sueldo base. Complemento legislativo: reformar el art. 62 bis para adoptar el estándar de "trabajo de igual valor" e invertir la carga de la prueba una vez constatada una brecha injustificada en el reporte.

### R2. Sala cuna universal: eliminar el umbral de 20 trabajadoras *(actúa sobre: retornos y participación)*

Sustituir la obligación individual del empleador por un **financiamiento colectivo** (cotización pareja por trabajador, de ambos sexos, o financiamiento fiscal), desacoplando el costo del cuidado infantil de la decisión de contratar mujeres. Es la reforma con la falla de diseño más claramente documentada del sistema actual (Prada, Rucci y Urzúa, 2015) y con el mayor consenso técnico transversal.

### R3. Corresponsabilidad efectiva: cuota paterna intransferible *(actúa sobre: retornos — penalización por maternidad)*

Rediseñar el postnatal parental incorporando **semanas exclusivas del padre no transferibles** (se pierden si no se usan), el instrumento que la evidencia internacional asocia a aumentos sustanciales del uso paterno y a la redistribución persistente del trabajo de cuidado (Patnaik, 2019, para la cuota de Quebec). Dado nuestro hallazgo de que la penalización chilena se concentra en mujeres casadas/convivientes con hijos, redistribuir el costo esperado del cuidado entre ambos progenitores ataca directamente el mecanismo señalizador que la genera.

### R4. Expansión de oferta pública de cuidado y jornada escolar extendida *(actúa sobre: horas y participación)*

La evaluación experimental chilena disponible muestra que el acceso a cuidado después de la jornada escolar aumenta significativamente el empleo materno (Martínez y Perticará, 2017). Dado que las horas trabajadas explican ~29% de la brecha — el mayor factor de composición identificado — y que la restricción horaria es asimétrica por sexo, la expansión de cuidado infantil y de jornada extendida tiene efecto doble: participación y convergencia de horas.

### R5. Estadística pública de brechas ajustadas *(infraestructura de política)*

Que el INE y el MDS publiquen regularmente brechas salariales **ajustadas por ocupación CIUO a 4 dígitos** — este trabajo demuestra que es factible con los datos ya recolectados — y que la ESI incorpore la codificación ocupacional a 4 dígitos en sus microdatos públicos. Sin medición granular oficial, el debate público seguirá anclado en brechas brutas que mezclan composición y retornos, y las brechas "favorables a mujeres" de celdas pequeñas seguirán usándose como contraejemplo sin sustento estadístico.

En la misma línea, establecer **protocolos estables de acceso para investigación a los registros administrativos vinculados** (Seguro de Cesantía, datos previsionales y tributarios, debidamente anonimizados): son la única vía para estudiar los canales de firma (sorting y negociación) y los efectos dinámicos de la maternidad que ni este trabajo ni ninguna encuesta de hogares de corte transversal puede identificar. La experiencia comparada (Dinamarca, Portugal) muestra que las contribuciones más influyentes de la última década en esta agenda descansan sobre esa infraestructura de datos.

### R6. Desegregación ocupacional: necesaria pero no suficiente *(actúa sobre: composición)*

Los programas de orientación vocacional temprana y acceso de mujeres a ocupaciones de alta remuneración (y de hombres a ocupaciones de cuidado) atacan el segundo mayor factor de composición identificado (~17%). La advertencia empírica de este trabajo: **aun eliminando completamente la segregación ocupacional fina, más del 80% de la brecha permanecería**. La desegregación debe acompañar —no sustituir— a los instrumentos R1-R3.

---

## 7. Análisis de robustez

Los resultados centrales fueron sometidos a la batería de robustez que un proceso de revisión exigiría (notebook 09 del repositorio). La brecha ajustada con ocupación granular bajo cada especificación:

| Especificación | Brecha ajustada | n |
|---|---|---|
| Baseline: ingreso mensual + control de horas, todos los ocupados | **-15.3%** | 174.924 |
| **Especificación máxima**: todos los controles simultáneos (ocupación 4d, hijos, estado civil, categoría/sector, cotización; 375 parámetros) | **-15.6%** | 174.719 |
| Máxima + efectos fijos de región (16) y zona urbano/rural | -15.7% | 174.719 |
| Máxima + geografía + tipo de institución de educación superior (CFT/IP/universidades) | -15.6% | 174.719 |
| Solo universitarios y posgraduados, con tipo de institución, región y zona | **-10.6%** | 46.532 |
| Edad prima (25-59 años) | -14.9% | 135.471 |
| Ingreso recortado (percentiles 1-99) | -13.0% | 171.481 |
| Solo jornada completa (40-45 horas semanales) | -12.9% | 110.716 |
| Solo asalariados formales (cotizan previsión) | **-12.0%** | 110.098 |
| Solo asalariados con contrato escrito firmado | -11.9% | 110.721 |
| Formalidad como control (categoría ocupacional + cotización) | -15.2% | 174.924 |
| Salario por hora (en vez de mensual + control de horas) | **-11.1%** | 174.924 |
| Solo asalariados del sector público | **-9.8%** | 27.222 |
| Solo asalariados del sector privado | -12.7% | 98.163 |
| Solo trabajadores independientes (cuenta propia y empleadores) | **-25.5%** | 44.697 |

Siete conclusiones de robustez:

1. **La brecha ajustada nunca se acerca a cero — y agregar controles no la reduce**: el rango completo (excluyendo el caso extremo de independientes) va de -11% a -16%. La **especificación máxima**, con todos los controles disponibles simultáneamente, arroja -15.6% — *más* que el baseline, porque varios controles (educación, formalidad, sector público) capturan composición que favorece a las mujeres; al descontarla, el diferencial atribuible al sexo queda más expuesto. En la descomposición final con todas las familias, la composición explica 27.4% y el 72.6% queda sin explicar. La restricción a jornada completa (40-45 horas, el tramo de la jornada legal) deja la brecha en -12.9%: la heterogeneidad horaria no explica ni una quinta parte del diferencial.
2. **¿Formal con formal?** La comparación restringida a asalariados formales —el mismo universo que cubren los datos administrativos del Seguro de Cesantía— arroja -12.0%. Y la composición por formalidad casi no difiere por sexo en la muestra de ocupados con ingreso (asalariados: 74.6% de los hombres vs 77.7% de las mujeres; cotización: 73.3% vs 72.5%): la brecha no es un artefacto de mezclar universos. Incluida como **control** en la muestra completa (categoría ocupacional + cotización), la formalidad apenas mueve el coeficiente de sexo (-15.3% → -15.2%), pese a ser un fuerte predictor del nivel de ingreso (cotizar se asocia a +30%; cuenta propia, a -19%); en la descomposición, su aporte compositivo es levemente negativo (-1.7%), como el de la educación. El hallazgo nuevo es de heterogeneidad — **la brecha más severa está entre independientes (-25.5%)**, el segmento sin contrato ni fiscalización posible, lo que acota el alcance de los instrumentos regulatorios clásicos (R1) y refuerza el rol de los instrumentos de cuidado (R2-R4), que operan sobre todos los regímenes de empleo.
3. **El *index number problem* de Oaxaca-Blinder no altera el diagnóstico**: bajo referencia masculina, femenina o pooled (Neumark, 1988), el ranking de factores es idéntico (horas primero, ocupación granular segundo, educación en contra); el componente no explicado varía entre 49% y 71% pero nunca baja de aproximadamente la mitad de la brecha.
4. **El patrón unidireccional por ocupación sobrevive al cambio de especificación**: en salario por hora, 41 ocupaciones sobreviven FDR (40 en contra de mujeres) y 16 sobreviven Bonferroni (todas en contra). La única excepción pro-mujer bajo FDR (conductoras de taxis, +13.1% por hora) refleja la dilución horaria de los conductores hombres, que trabajan jornadas extremas — bajo Bonferroni ninguna ocupación favorece a las mujeres en ninguna especificación.
5. En salario por hora la brecha es menor que en ingreso mensual (-11.1% vs -15.3%): parte de la brecha mensual refleja directamente la menor cantidad de horas remuneradas de las mujeres — coherente con el peso de las horas en la descomposición y con el diagnóstico de Goldin (2014).
6. **El sector público comprime la brecha, pero no la elimina.** Las mujeres están sobrerrepresentadas en el empleo público (56.1% de ese segmento; concentra el 19.0% del empleo femenino vs el 11.0% del masculino), y la brecha ajustada ahí es menor que en el privado: **-9.8% vs -12.7%** (diferencia marginalmente significativa; interacción mujer×público, p=0.078). El patrón es coherente con remuneraciones regidas por escalas y grados públicos — evidencia local a favor de la transparencia salarial (R1) — pero el -9.8% remanente indica que las escalas no bastan: asignaciones, horas extraordinarias y velocidad de ascenso quedan fuera de su alcance.
7. **Ni la geografía ni la calidad de la educación superior explican la brecha.** Los efectos fijos de región y zona urbano/rural dejan el coeficiente en -15.7%, y el tipo de institución de educación superior — que sí predice con fuerza el nivel de ingreso (universidades CRUCH y estatales se asocian a ~+20% sobre un CFT, a igualdad de todo lo demás) — lo deja en -15.6%. La prueba más fina: **solo entre universitarios y posgraduados**, con tipo de institución, región, zona, ocupación exacta, horas, familia y formalidad controladas, la brecha es **-10.6%**. Nota de datos: CASEN solo registra el *nombre* de la institución para quienes estudian actualmente; para los titulados solo el tipo — el control ideal (efectos fijos por institución×carrera) requiere los registros SIES/Mineduc vinculados a ingresos, otro insumo para R5.

![Robustez de especificaciones](../notebooks/outputs/figures/robustez_especificaciones.png)

---

## 8. ¿Qué hay dentro del 72% no explicado? Mecanismos con evidencia causal

El 72.6% que la especificación máxima deja sin explicar no es una caja negra ni un sinónimo automático de "preferencias inobservables". La literatura internacional —con diseños experimentales y datos administrativos que Chile no tiene— ha identificado y cuantificado sus componentes principales:

**8.1 La brecha de peticiones (*ask gap*).** Roussille (2024) documenta, en una plataforma de contratación donde los candidatos publican su pretensión salarial, que las mujeres piden en torno a 3% menos por el mismo perfil — y esa diferencia de *petición* da cuenta de prácticamente toda la brecha en las ofertas finales. El hallazgo de política es notable: cuando la plataforma comenzó a mostrar la mediana salarial de mercado para cada perfil, la brecha de peticiones (y con ella la de ofertas) prácticamente desapareció. En la misma línea, Leibbrandt y List (2015) muestran que cuando la negociabilidad del salario es ambigua los hombres negocian más, y que explicitar "salario negociable" elimina la diferencia. Exley, Niederle y Vesterlund (2020) advierten el reverso: empujar a las mujeres a negociar más no siempre les conviene, porque el castigo por pedir difiere según el sexo — el problema es el *entorno* de negociación, no una deficiencia femenina que corregir.

**8.2 Sobretiempo y flexibilidad: el mecanismo dentro de la ocupación.** Bolotnyy y Emanuel (2022) estudian el caso más limpio disponible: operadores de buses y trenes de Boston — mismo cargo, mismo sindicato, misma tarifa horaria por contrato. Los hombres terminan ganando más porque aceptan más sobretiempo (especialmente el de última hora, mejor pagado) y las mujeres eligen configuraciones horarias compatibles con el cuidado. Es la versión micro del diagnóstico de Goldin (2014) sobre la no-linealidad de los retornos a las horas. Nuestros propios datos muestran la huella de ese mecanismo: las horas son el mayor factor observable de la descomposición (23.3%), y el único caso "pro-mujer" que sobrevive FDR (conductoras de taxi, en salario por hora) refleja precisamente jornadas masculinas extremas que diluyen el precio-hora.

**8.3 Competencia, riesgo y personalidad.** Niederle y Vesterlund (2007) muestran experimentalmente que, a igual desempeño, el doble de hombres elige compensación por torneo; Buser, Niederle y Oosterbeek (2014) documentan que esa disposición predice la elección de carrera — es decir, alimenta la *composición* ocupacional, no solo el residuo. Croson y Gneezy (2009) y Bertrand (2011) revisan las diferencias de preferencias (riesgo, competencia, actitudes sociales); Mueller y Plug (2006) y Heckman, Stixrud y Urzúa (2006) muestran que los atributos de personalidad y las habilidades no cognitivas afectan los salarios. Pero la conclusión agregada de Blau y Kahn (2017) es aleccionadora: **estos factores explican una porción pequeña a moderada de la brecha** — relevante, pero lejos de agotar el residuo. Y una parte de esas "preferencias" es a su vez endógena a normas y expectativas, no un rasgo exógeno.

**8.4 Firmas y negociación.** Card, Cardoso y Kline (2016), con datos administrativos portugueses: la combinación de sorting hacia firmas que pagan menores premios y menor captura de rentas en la negociación explica en torno a un quinto de la brecha. Este canal es completamente invisible para nuestros datos (no observamos el empleador) y queda, por construcción, dentro de nuestro 72%.

**8.5 La dinámica de la maternidad.** Cortés y Pan (2023) concluyen que los hijos son hoy el principal factor detrás de las brechas restantes en países desarrollados; Kleven et al. (2019, 2024) cuantifican penalizaciones de largo plazo en torno al 20% en Dinamarca y sustancialmente mayores en América Latina. Nuestro coeficiente mujer×hijos (-7.8% transversal) es la huella estática de ese proceso dinámico: la penalización se acumula con los años posteriores al nacimiento, algo que un corte transversal solo puede subestimar.

**Implicancia para Chile.** Ninguno de estos mecanismos es medible hoy con datos públicos chilenos: CASEN y ESI no incluyen módulos de negociación salarial, historia laboral efectiva ni atributos socioemocionales, y la ELPI mide lo socioemocional solo en cuidadores principales de niños pequeños (mayoritariamente mujeres), lo que impide comparar entre sexos. Esto convierte el 72% en un argumento adicional para la recomendación R5: **módulos breves de negociación** (¿negoció su remuneración al ser contratado?, ¿ha pedido un aumento?, ¿el salario era presentado como negociable?) **e historia laboral** en las encuestas existentes tienen costo marginal bajo y abrirían la caja negra local. Mientras tanto, la lectura correcta del residuo no es "diferencias de preferencias inabordables", sino un conjunto de mecanismos con nombre, evidencia y — cada uno — un instrumento de política asociado: transparencia de rangos y negociabilidad (8.1), diseño del sobretiempo y la flexibilidad (8.2), corresponsabilidad en el cuidado (8.5).

---

## 9. Limitaciones

- **Identificación.** Los datos son observacionales y de corte transversal; los coeficientes describen asociaciones condicionales, no efectos causales. El componente "no explicado" acota pero no identifica discriminación.
- **Selección.** La participación laboral femenina es ~18 pp menor; si las mujeres que participan están positivamente seleccionadas en productividad, nuestras brechas *subestiman* el diferencial poblacional. No aplicamos correcciones de selección (Heckman) para mantener la transparencia del pipeline.
- **Sin dimensión de firma.** No observamos el empleador, por lo que el canal de sorting entre firmas y negociación (Card, Cardoso y Kline, 2016) queda dentro del residuo. Datos administrativos vinculados (Seguro de Cesantía, SII) permitirían cerrarlo; su apertura para investigación es en sí misma una recomendación.
- **Maternidad como stock, no como evento.** La pregunta `s5` de CASEN mide haber tenido hijos, no el evento del nacimiento; un estudio de eventos tipo Kleven et al. (2019) exige datos longitudinales. Los paneles chilenos existentes (EPS, ELPI) y los registros del Seguro de Cesantía permitirían aproximarlo, pero ninguno está disponible como dato abierto de propósito general — un estudio de eventos de penalización por maternidad con datos administrativos chilenos sigue siendo, hasta donde conocemos, una vacante en la literatura local.
- **Ingreso autorreportado** y ruptura de clasificador ocupacional (CIUO-88 vs CIUO-08) que impide extender la serie granular antes de 2022.

---

## 10. Referencias

**Literatura académica**

- Albrecht, J., Björklund, A. y Vroman, S. (2003). "Is There a Glass Ceiling in Sweden?". *Journal of Labor Economics*, 21(1).
- Arrow, K. (1973). "The Theory of Discrimination". En O. Ashenfelter y A. Rees (eds.), *Discrimination in Labor Markets*. Princeton University Press.
- Arulampalam, W., Booth, A. y Bryan, M. (2007). "Is There a Glass Ceiling over Europe? Exploring the Gender Pay Gap across the Wage Distribution". *ILR Review*, 60(2).
- Baker, M., Halberstam, Y., Kroft, K., Mas, A. y Messacar, D. (2023). "Pay Transparency and the Gender Gap". *American Economic Journal: Applied Economics*, 15(2).
- Becker, G. (1957). *The Economics of Discrimination*. University of Chicago Press.
- Bennedsen, M., Simintzi, E., Tsoutsoura, M. y Wolfenzon, D. (2022). "Do Firms Respond to Gender Pay Gap Transparency?". *Journal of Finance*, 77(4).
- Bertrand, M. (2011). "New Perspectives on Gender". En O. Ashenfelter y D. Card (eds.), *Handbook of Labor Economics*, vol. 4B. Elsevier.
- Bertrand, M., Goldin, C. y Katz, L. (2010). "Dynamics of the Gender Gap for Young Professionals in the Financial and Corporate Sectors". *American Economic Journal: Applied Economics*, 2(3).
- Blau, F. y Kahn, L. (2017). "The Gender Wage Gap: Extent, Trends, and Explanations". *Journal of Economic Literature*, 55(3).
- Blinder, A. (1973). "Wage Discrimination: Reduced Form and Structural Estimates". *Journal of Human Resources*, 8(4).
- Bolotnyy, V. y Emanuel, N. (2022). "Why Do Women Earn Less Than Men? Evidence from Bus and Train Operators". *Journal of Labor Economics*, 40(2).
- Buser, T., Niederle, M. y Oosterbeek, H. (2014). "Gender, Competitiveness, and Career Choices". *Quarterly Journal of Economics*, 129(3).
- Card, D., Cardoso, A.R. y Kline, P. (2016). "Bargaining, Sorting, and the Gender Wage Gap: Quantifying the Impact of Firms on the Relative Pay of Women". *Quarterly Journal of Economics*, 131(2).
- Cortés, P. y Pan, J. (2023). "Children and the Remaining Gender Gaps in the Labor Market". *Journal of Economic Literature*, 61(4).
- Croson, R. y Gneezy, U. (2009). "Gender Differences in Preferences". *Journal of Economic Literature*, 47(2).
- Cullen, Z. (2024). "Is Pay Transparency Good?". *Journal of Economic Perspectives*, 38(1).
- Exley, C., Niederle, M. y Vesterlund, L. (2020). "Knowing When to Ask: The Cost of Leaning In". *Journal of Political Economy*, 128(3).
- Goldin, C. (2014). "A Grand Gender Convergence: Its Last Chapter". *American Economic Review*, 104(4).
- Goldin, C. (2021). *Career and Family: Women's Century-Long Journey toward Equity*. Princeton University Press.
- Heckman, J., Stixrud, J. y Urzúa, S. (2006). "The Effects of Cognitive and Noncognitive Abilities on Labor Market Outcomes and Social Behavior". *Journal of Labor Economics*, 24(3).
- Kleven, H., Landais, C. y Leite-Mariante, G. (2024). "The Child Penalty Atlas". *Review of Economic Studies*.
- Kleven, H., Landais, C. y Søgaard, J.E. (2019). "Children and Gender Inequality: Evidence from Denmark". *American Economic Journal: Applied Economics*, 11(4).
- Leibbrandt, A. y List, J. (2015). "Do Women Avoid Salary Negotiations? Evidence from a Large-Scale Natural Field Experiment". *Management Science*, 61(9).
- Martínez, C. y Perticará, M. (2017). "Childcare Effects on Maternal Employment: Evidence from Chile". *Journal of Development Economics*, 126.
- Mincer, J. (1974). *Schooling, Experience, and Earnings*. NBER / Columbia University Press.
- Mueller, G. y Plug, E. (2006). "Estimating the Effect of Personality on Male and Female Earnings". *ILR Review*, 60(1).
- Niederle, M. y Vesterlund, L. (2007). "Do Women Shy Away from Competition? Do Men Compete Too Much?". *Quarterly Journal of Economics*, 122(3).
- Oaxaca, R. (1973). "Male-Female Wage Differentials in Urban Labor Markets". *International Economic Review*, 14(3).
- Patnaik, A. (2019). "Reserving Time for Daddy: The Consequences of Fathers' Quotas". *Journal of Labor Economics*, 37(4).
- Perticará, M. y Bueno, I. (2009). "A New Approach to Gender Wage Gaps in Chile". *Revista CEPAL*, 99.
- Petersen, T. y Morgan, L. (1995). "Separate and Unequal: Occupation-Establishment Sex Segregation and the Gender Wage Gap". *American Journal of Sociology*, 101(2).
- Phelps, E. (1972). "The Statistical Theory of Racism and Sexism". *American Economic Review*, 62(4).
- Prada, M.F., Rucci, G. y Urzúa, S. (2015). "The Effect of Mandated Child Care on Female Wages in Chile". NBER Working Paper 21080.
- Roussille, N. (2024). "The Central Role of the Ask Gap in Gender Pay Inequality". *Quarterly Journal of Economics*, 139(3).
- Sánchez, R., Finot, J. y Villena-Roldán, B. (2020). "Gender Wage Gap and Firm Market Power: Evidence from Chile". IZA Discussion Paper 13856.

**Fuentes oficiales y datos**

- Instituto Nacional de Estadísticas (INE). *Encuesta Suplementaria de Ingresos*, microdatos 2018-2024.
- Ministerio de Desarrollo Social y Familia. *Encuesta CASEN*, microdatos 2022 y 2024. Observatorio Social.
- OCDE. *Gender wage gap* (indicador, base de datos de empleo).
- OIT (2018). *Informe Mundial sobre Salarios 2018/19: ¿Qué hay detrás de la brecha salarial de género?*
- Ley 20.348 (2009), Ley 20.545 (2011); Código del Trabajo, artículos 62 bis y 203.

---

*Este documento se genera desde un pipeline reproducible. Los notebooks 01-08 del repositorio contienen todos los cálculos citados; las tablas por ocupación están disponibles como CSV en [`notebooks/outputs/data/`](../notebooks/outputs/data/).*
