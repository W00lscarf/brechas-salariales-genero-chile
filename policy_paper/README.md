# Misma ocupación, distinto salario

## La brecha de género que la composición no explica: evidencia desde microdatos públicos y propuestas de política para Chile

*Policy paper elaborado a partir de los resultados del repositorio [`brechas-salariales-genero-chile`](https://github.com/W00lscarf/brechas-salariales-genero-chile). Todos los cálculos son reproducibles con datos públicos y código abierto (notebooks 01-08).*

**Julio 2026**

---

## Resumen ejecutivo

- Con microdatos públicos de la Encuesta Suplementaria de Ingresos (ESI 2018-2024) y CASEN (2022 y 2024), estimamos que las mujeres ocupadas en Chile ganan en promedio **22-26% menos** que los hombres por su trabajo principal, según fuente y período.
- Controlando simultáneamente por edad, educación, horas trabajadas, año y **ocupación exacta a 4 dígitos CIUO-08** (356 categorías, el control más fino posible con datos públicos chilenos), la brecha ajustada es **-17.6%**. La ocupación granular explica más que ningún otro factor observable (**~22% de la brecha total**), pero la mayoría del diferencial —**cerca del 80%**— permanece sin explicar por composición.
- **La penalización por maternidad es identificable y significativa**: dentro de la misma ocupación exacta, una mujer con hijos gana un **9.7% adicional menos** (p<0.001) que lo que la brecha general ya le descuenta, mientras que para los hombres tener hijos se asocia a un *premio* salarial (+6.3%). El costo se concentra en mujeres casadas o convivientes.
- Al aislar el efecto sexo ocupación por ocupación, **102 de 229 ocupaciones muestran brecha estadísticamente significativa — las 102 en contra de las mujeres; ninguna a favor**. El resultado es robusto a correcciones por comparaciones múltiples (76 ocupaciones sobreviven la corrección FDR y 33 el criterio de Bonferroni; todas en contra). Las brechas "pro-mujer" que aparecen en comparaciones simples no sobreviven el control de incertidumbre estadística.
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

Ocupados con ingreso positivo y ocupación válida: **176.542 personas** (2022+2024 combinados), en 444 códigos ocupacionales distintos, de los cuales 356 tienen n≥30. Para los análisis por ocupación específica se exige además **≥20 hombres y ≥20 mujeres** por celda, lo que deja **229 ocupaciones**.

### 3.3 Estrategia empírica

1. **Regresión minceriana con dos niveles de granularidad.** Misma especificación (`log ingreso ~ mujer + edad + edad² + educación + horas + año`), cambiando únicamente el control ocupacional: 1 dígito CIUO (~9 categorías, lo que permite la ESI) versus 4 dígitos (356 categorías). La diferencia entre ambos coeficientes de `mujer` aísla el aporte puro de la granularidad.
2. **Descomposición de Oaxaca-Blinder ponderada**, agrupando las contribuciones por familia de variable (educación, edad, horas, ocupación, hijos, estado civil, año), para rankear qué controles explican más de la brecha total.
3. **Interacciones mujer×hijos y mujer×estado civil**, con la pregunta directa de fecundidad de CASEN (a diferencia de la ESI, que exige aproximar maternidad por composición del hogar).
4. **Modelo de interacción completa `mujer × ocupación`** sobre las 229 ocupaciones: los controles comunes se estiman con toda la muestra (~151.000 observaciones) y el efecto sexo se deja variar libremente por ocupación. El efecto por ocupación se recupera como combinación lineal de coeficientes, con varianza calculada desde la matriz de covarianza cluster-robusta. Este diseño es más eficiente que estimar 229 regresiones separadas con 50-100 casos cada una.

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
| Ocupación **amplia** (1 dígito, ~9 categorías — equivalente ESI) | **-24.4%** (IC95: -25.2 a -23.6) | 0.449 |
| Ocupación **granular** (4 dígitos, 356 categorías) | **-17.6%** (IC95: -18.5 a -16.7) | 0.508 |
| **Diferencia** | **+6.8 pp** | |

La granularidad importa: una parte real de lo que las estimaciones convencionales reportan como "no explicado" es **segregación ocupacional fina** — dentro de "Profesionales", los hombres se concentran en las especialidades mejor pagadas. Pero la brecha no se desploma: **-17.6% persiste comparando la misma ocupación exacta**. Incluso dentro de ocupaciones idénticas: médicos especialistas -20%, técnicos de enfermería -13%, enfermeros -3%.

### 4.3 Ranking de factores: qué explica la brecha y cuánto

Descomposición de Oaxaca-Blinder sobre la brecha total de 22.5% (CASEN 2022+2024), con y sin controles de familia:

| Factor | Sin hijos/estado civil | Con hijos/estado civil |
|---|---|---|
| Ocupación (4 dígitos) | **+22.2%** | **+18.9%** |
| Horas trabajadas | +12.7% | +12.3% |
| Estado civil | — | +2.1% |
| Tiene hijos | — | -1.7% |
| Edad | -1.6% | -2.6% |
| Educación | **-10.7%** | **-10.9%** |
| Año | -0.4% | -0.4% |
| **No explicado** | **77.8%** | **82.2%** |

Tres lecturas de política se desprenden de esta tabla:

1. **La segregación ocupacional fina es el mayor factor de composición identificado** (~1/5 de la brecha), muy por delante de las horas (~1/8).
2. **La educación protege**: las ocupadas chilenas están mejor educadas que los ocupados; si solo importara el capital humano, ganarían *más*.
3. **Hijos y estado civil casi no aportan a la parte explicada** — hombres y mujeres no difieren tanto en composición familiar promedio. Su efecto opera por otra vía (sección 4.4).

### 4.4 La penalización por maternidad: un efecto de retornos, no de composición

Interacción mujer×hijos y mujer×estado civil, controlando ocupación exacta, educación, edad, horas y año (n=176.326):

| Término | Efecto sobre el ingreso | p-valor |
|---|---|---|
| Mujer (brecha base) | -13.7% | <0.001 |
| Tiene hijos (efecto para hombres) | **+6.3%** | <0.001 |
| **Mujer × tiene hijos** | **-9.7%** | **<0.001** |
| Mujer × soltera (vs. casada/conviviente) | +5.9% | <0.001 |

El contraste es nítido: **la paternidad se asocia a un premio salarial; la maternidad, a una penalización adicional** por sobre la brecha que ya afecta a toda mujer — exactamente el patrón que la literatura internacional de *child penalties* documenta con datos administrativos (Kleven et al., 2019; Cortés y Pan, 2023). Notablemente, con datos ESI (sin ocupación granular) esta interacción no era estadísticamente significativa: la granularidad ocupacional fue la que permitió identificarla, lo que sugiere que parte de la penalización por maternidad en Chile opera *dentro* de las ocupaciones y no solo a través de la selección hacia ocupaciones peor pagadas.

Este hallazgo también resuelve la aparente paradoja de la tabla anterior: agregar hijos y estado civil *sube* el "no explicado" (77.8% → 82.2%) porque la descomposición solo asigna al componente explicado las diferencias de composición promedio — y la penalización por maternidad es una diferencia de **retorno** (el mismo hijo impacta distinto según el sexo del progenitor), no de composición.

### 4.5 Aislando el efecto sexo ocupación por ocupación

El resultado central del análisis. Con el modelo de interacción completa (efecto sexo específico a cada una de las 229 ocupaciones, neto de edad, educación, horas, hijos, estado civil y año):

- **102 de 229 ocupaciones (44.5%) presentan brecha ajustada estadísticamente significativa (p<0.05).**
- **Las 102 son en contra de las mujeres. Ninguna ocupación presenta brecha significativa a favor.**
- **El resultado resiste la corrección por comparaciones múltiples.** Con 229 contrastes simultáneos se esperarían ~11 falsos positivos por azar a p<0.05; sin embargo, 76 ocupaciones sobreviven la corrección FDR de Benjamini-Hochberg (q<0.05) y 33 sobreviven incluso el criterio de Bonferroni, el más conservador disponible — en todos los casos, la totalidad de las significativas es en contra de las mujeres.
- Las aparentes ventajas femeninas de las comparaciones simples (joyería +59%, música +41%, traducción +36%) provienen de celdas pequeñas (n entre 55 y 148) y no se distinguen del azar (p>0.2) al contabilizar la incertidumbre.
- La correlación entre brecha cruda y ajustada es 0.79: el orden se conserva, el promedio se modera levemente (-17.7% → -16.7%).

![Brecha cruda vs ajustada por ocupación](../notebooks/outputs/figures/ranking_ajustado_vs_crudo.png)

La distribución completa (229 ocupaciones, con brecha cruda, ajustada, p-valor y tamaños muestrales) está publicada como dato abierto en [`ranking_brecha_ocupacion_ajustada.csv`](../notebooks/outputs/data/ranking_brecha_ocupacion_ajustada.csv).

### 4.6 Síntesis del diagnóstico

| Componente de la brecha (22.5% total) | Magnitud aproximada | ¿Qué es? |
|---|---|---|
| Segregación ocupacional fina | ~1/5 | Composición: dónde trabajan |
| Horas trabajadas | ~1/8 | Composición/preferencias restringidas |
| Educación | negativa (protege) | Composición |
| Retornos desiguales (incl. penalización por maternidad) | **~4/5** | Cómo se paga a iguales características |

El problema chileno es, predominantemente, de **retornos**: características idénticas se remuneran distinto según el sexo, con la maternidad como el mecanismo identificable más claro dentro de ese residuo.

---

## 5. Marco institucional vigente y sus límites

Chile ratificó el Convenio 100 de la OIT (igualdad de remuneración) en 1971. El instrumento interno principal es la **Ley 20.348 (2009)**, que incorporó el artículo 62 bis al Código del Trabajo: derecho a la igualdad de remuneraciones entre hombres y mujeres que presten "un mismo trabajo". Su diseño presenta tres debilidades documentadas: exige identidad de funciones (no trabajo de igual valor, el estándar OIT), radica la carga de reclamar en la trabajadora individual mediante un procedimiento interno previo, y carece de un mecanismo de reporte que haga observables las brechas. El volumen de denuncias y sanciones ha sido marginal desde su entrada en vigencia.

El **artículo 203 del Código del Trabajo** obliga a financiar sala cuna solo a los empleadores con **20 o más trabajadoras**. Al gravar la contratación femenina en el margen, la norma genera exactamente la distorsión que la teoría predice: Prada, Rucci y Urzúa (2015) documentan que el costo se traslada a menores salarios de contratación de las mujeres en las firmas afectadas. El proyecto de sala cuna universal que corrige este diseño lleva años en tramitación legislativa.

La **Ley 20.545 (2011)** extendió el postnatal parental a 24 semanas con semanas transferibles al padre; el uso paterno ha sido persistentemente inferior al 1%, lo que en la práctica consolida la asignación asimétrica del cuidado que la literatura identifica como el motor de la penalización por maternidad.

---

## 6. Recomendaciones de política

Las recomendaciones se ordenan por el componente de la brecha sobre el que actúan, siguiendo el diagnóstico de la sección 4.6.

### R1. Transparencia salarial obligatoria con brechas ajustadas por ocupación *(actúa sobre: retornos)*

Obligación legal para empresas sobre un umbral de tamaño de calcular y reportar periódicamente su brecha salarial de género **por categoría ocupacional comparable**, con difusión a trabajadores y sindicatos. La evidencia causal de alto estándar es favorable: la ley danesa de reporte redujo la brecha en torno a un 13% relativo, principalmente moderando el crecimiento salarial masculino, sin efectos negativos de empleo (Bennedsen, Simintzi, Tsoutsoura y Wolfenzon, 2022); la transparencia en universidades canadienses la redujo del orden de 20-30% (Baker, Halberstam, Kroft, Mas y Messacar, 2023). Cullen (2024) resume las condiciones de diseño que evitan efectos adversos sobre la negociación individual. Complemento legislativo: reformar el art. 62 bis para adoptar el estándar de "trabajo de igual valor" e invertir la carga de la prueba una vez constatada una brecha injustificada en el reporte.

### R2. Sala cuna universal: eliminar el umbral de 20 trabajadoras *(actúa sobre: retornos y participación)*

Sustituir la obligación individual del empleador por un **financiamiento colectivo** (cotización pareja por trabajador, de ambos sexos, o financiamiento fiscal), desacoplando el costo del cuidado infantil de la decisión de contratar mujeres. Es la reforma con la falla de diseño más claramente documentada del sistema actual (Prada, Rucci y Urzúa, 2015) y con el mayor consenso técnico transversal.

### R3. Corresponsabilidad efectiva: cuota paterna intransferible *(actúa sobre: retornos — penalización por maternidad)*

Rediseñar el postnatal parental incorporando **semanas exclusivas del padre no transferibles** (se pierden si no se usan), el instrumento que la evidencia internacional asocia a aumentos sustanciales del uso paterno y a la redistribución persistente del trabajo de cuidado (Patnaik, 2019, para la cuota de Quebec). Dado nuestro hallazgo de que la penalización chilena se concentra en mujeres casadas/convivientes con hijos, redistribuir el costo esperado del cuidado entre ambos progenitores ataca directamente el mecanismo señalizador que la genera.

### R4. Expansión de oferta pública de cuidado y jornada escolar extendida *(actúa sobre: horas y participación)*

La evaluación experimental chilena disponible muestra que el acceso a cuidado después de la jornada escolar aumenta significativamente el empleo materno (Martínez y Perticará, 2017). Dado que las horas trabajadas explican ~12% de la brecha y que la restricción horaria es asimétrica por sexo, la expansión de cuidado infantil y de jornada extendida tiene efecto doble: participación y convergencia de horas.

### R5. Estadística pública de brechas ajustadas *(infraestructura de política)*

Que el INE y el MDS publiquen regularmente brechas salariales **ajustadas por ocupación CIUO a 4 dígitos** — este trabajo demuestra que es factible con los datos ya recolectados — y que la ESI incorpore la codificación ocupacional a 4 dígitos en sus microdatos públicos. Sin medición granular oficial, el debate público seguirá anclado en brechas brutas que mezclan composición y retornos, y las brechas "favorables a mujeres" de celdas pequeñas seguirán usándose como contraejemplo sin sustento estadístico.

En la misma línea, establecer **protocolos estables de acceso para investigación a los registros administrativos vinculados** (Seguro de Cesantía, datos previsionales y tributarios, debidamente anonimizados): son la única vía para estudiar los canales de firma (sorting y negociación) y los efectos dinámicos de la maternidad que ni este trabajo ni ninguna encuesta de hogares de corte transversal puede identificar. La experiencia comparada (Dinamarca, Portugal) muestra que las contribuciones más influyentes de la última década en esta agenda descansan sobre esa infraestructura de datos.

### R6. Desegregación ocupacional: necesaria pero no suficiente *(actúa sobre: composición)*

Los programas de orientación vocacional temprana y acceso de mujeres a ocupaciones de alta remuneración (y de hombres a ocupaciones de cuidado) atacan el mayor factor de composición identificado (~22%). La advertencia empírica de este trabajo: **aun eliminando completamente la segregación ocupacional fina, cerca del 80% de la brecha permanecería**. La desegregación debe acompañar —no sustituir— a los instrumentos R1-R3.

---

## 7. Limitaciones

- **Identificación.** Los datos son observacionales y de corte transversal; los coeficientes describen asociaciones condicionales, no efectos causales. El componente "no explicado" acota pero no identifica discriminación.
- **Selección.** La participación laboral femenina es ~18 pp menor; si las mujeres que participan están positivamente seleccionadas en productividad, nuestras brechas *subestiman* el diferencial poblacional. No aplicamos correcciones de selección (Heckman) para mantener la transparencia del pipeline.
- **Sin dimensión de firma.** No observamos el empleador, por lo que el canal de sorting entre firmas y negociación (Card, Cardoso y Kline, 2016) queda dentro del residuo. Datos administrativos vinculados (Seguro de Cesantía, SII) permitirían cerrarlo; su apertura para investigación es en sí misma una recomendación.
- **Maternidad como stock, no como evento.** La pregunta `s5` de CASEN mide haber tenido hijos, no el evento del nacimiento; un estudio de eventos tipo Kleven et al. (2019) exige datos longitudinales. Los paneles chilenos existentes (EPS, ELPI) y los registros del Seguro de Cesantía permitirían aproximarlo, pero ninguno está disponible como dato abierto de propósito general — un estudio de eventos de penalización por maternidad con datos administrativos chilenos sigue siendo, hasta donde conocemos, una vacante en la literatura local.
- **Ingreso autorreportado** y ruptura de clasificador ocupacional (CIUO-88 vs CIUO-08) que impide extender la serie granular antes de 2022.

---

## 8. Referencias

**Literatura académica**

- Arrow, K. (1973). "The Theory of Discrimination". En O. Ashenfelter y A. Rees (eds.), *Discrimination in Labor Markets*. Princeton University Press.
- Baker, M., Halberstam, Y., Kroft, K., Mas, A. y Messacar, D. (2023). "Pay Transparency and the Gender Gap". *American Economic Journal: Applied Economics*, 15(2).
- Becker, G. (1957). *The Economics of Discrimination*. University of Chicago Press.
- Bennedsen, M., Simintzi, E., Tsoutsoura, M. y Wolfenzon, D. (2022). "Do Firms Respond to Gender Pay Gap Transparency?". *Journal of Finance*, 77(4).
- Bertrand, M., Goldin, C. y Katz, L. (2010). "Dynamics of the Gender Gap for Young Professionals in the Financial and Corporate Sectors". *American Economic Journal: Applied Economics*, 2(3).
- Blau, F. y Kahn, L. (2017). "The Gender Wage Gap: Extent, Trends, and Explanations". *Journal of Economic Literature*, 55(3).
- Blinder, A. (1973). "Wage Discrimination: Reduced Form and Structural Estimates". *Journal of Human Resources*, 8(4).
- Card, D., Cardoso, A.R. y Kline, P. (2016). "Bargaining, Sorting, and the Gender Wage Gap: Quantifying the Impact of Firms on the Relative Pay of Women". *Quarterly Journal of Economics*, 131(2).
- Cortés, P. y Pan, J. (2023). "Children and the Remaining Gender Gaps in the Labor Market". *Journal of Economic Literature*, 61(4).
- Cullen, Z. (2024). "Is Pay Transparency Good?". *Journal of Economic Perspectives*, 38(1).
- Goldin, C. (2014). "A Grand Gender Convergence: Its Last Chapter". *American Economic Review*, 104(4).
- Goldin, C. (2021). *Career and Family: Women's Century-Long Journey toward Equity*. Princeton University Press.
- Kleven, H., Landais, C. y Søgaard, J.E. (2019). "Children and Gender Inequality: Evidence from Denmark". *American Economic Journal: Applied Economics*, 11(4).
- Kleven, H., Landais, C. y Leite-Mariante, G. (2024). "The Child Penalty Atlas". *Review of Economic Studies*.
- Martínez, C. y Perticará, M. (2017). "Childcare Effects on Maternal Employment: Evidence from Chile". *Journal of Development Economics*, 126.
- Mincer, J. (1974). *Schooling, Experience, and Earnings*. NBER / Columbia University Press.
- Oaxaca, R. (1973). "Male-Female Wage Differentials in Urban Labor Markets". *International Economic Review*, 14(3).
- Patnaik, A. (2019). "Reserving Time for Daddy: The Consequences of Fathers' Quotas". *Journal of Labor Economics*, 37(4).
- Perticará, M. y Bueno, I. (2009). "A New Approach to Gender Wage Gaps in Chile". *Revista CEPAL*, 99.
- Petersen, T. y Morgan, L. (1995). "Separate and Unequal: Occupation-Establishment Sex Segregation and the Gender Wage Gap". *American Journal of Sociology*, 101(2).
- Phelps, E. (1972). "The Statistical Theory of Racism and Sexism". *American Economic Review*, 62(4).
- Prada, M.F., Rucci, G. y Urzúa, S. (2015). "The Effect of Mandated Child Care on Female Wages in Chile". NBER Working Paper 21080.
- Sánchez, R., Finot, J. y Villena-Roldán, B. (2020). "Gender Wage Gap and Firm Market Power: Evidence from Chile". IZA Discussion Paper 13856.

**Fuentes oficiales y datos**

- Instituto Nacional de Estadísticas (INE). *Encuesta Suplementaria de Ingresos*, microdatos 2018-2024.
- Ministerio de Desarrollo Social y Familia. *Encuesta CASEN*, microdatos 2022 y 2024. Observatorio Social.
- OCDE. *Gender wage gap* (indicador, base de datos de empleo).
- OIT (2018). *Informe Mundial sobre Salarios 2018/19: ¿Qué hay detrás de la brecha salarial de género?*
- Ley 20.348 (2009), Ley 20.545 (2011); Código del Trabajo, artículos 62 bis y 203.

---

*Este documento se genera desde un pipeline reproducible. Los notebooks 01-08 del repositorio contienen todos los cálculos citados; las tablas por ocupación están disponibles como CSV en [`notebooks/outputs/data/`](../notebooks/outputs/data/).*
