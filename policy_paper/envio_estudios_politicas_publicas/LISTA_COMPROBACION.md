# Lista de comprobación — Envío a Revista Estudios de Políticas Públicas (U. de Chile)

## Contenido de esta carpeta

| Archivo | Descripción |
|---|---|
| `manuscrito_epp.docx` | **El archivo de envío** (Word, 12 pt, espaciado simple, tablas y figuras integradas) |
| `manuscrito_epp.md` | Fuente del manuscrito (se regenera el .docx con `python generar_docx_epp.py`) |
| `generar_docx_epp.py` | Conversor Markdown → Word |
| `figura1_ranking_ajustado_vs_crudo.png` | Figura 1 para adjuntar por separado (lo exige la revista) |
| `figura2_brecha_por_cuantil.png` | Figura 2 para adjuntar por separado |
| `figura3_robustez_especificaciones.png` | Figura 3 para adjuntar por separado |

## Requisitos de la revista — verificados ✔

- [x] Formato Word (.docx)
- [x] Español; texto con espaciado simple, 12 puntos, cursivas (no subrayado)
- [x] Extensión: 10.313 palabras incluyendo referencias (límite: 12.000)
- [x] Título en español (94 caracteres) y en inglés (95 caracteres); límite 100
- [x] Resumen en español (194 palabras) y abstract en inglés (168); límite 200
- [x] Cinco palabras clave en español y en inglés
- [x] Tablas y figuras con título, numeradas consecutivamente, integradas en el texto y con fuente de procedencia ("Fuente: elaboración propia a partir de CASEN 2022 y 2024")
- [x] Figuras también adjuntas como archivos separados (PNG, 150 dpi)
- [x] Citas en texto: (Autor, año); dos autores con "y"; tres o más con "et al."
- [x] Sección final "Referencias bibliográficas" en el formato de la revista (título del artículo entre comillas, revista en cursiva, `vol(num): páginas` donde se dispone de páginas verificadas)
- [x] Sin notas al pie usadas para referencias
- [x] Trabajo original e inédito, no sometido a otra revista (el working paper en el repositorio de GitHub es un preprint; ver nota abajo)
- [x] **Autor:** *Nicolás Guerrero Herrera*, Investigador independiente (confirmado). Figura en el bloque de autoría, centrado bajo los títulos.
- [x] **Firma normalizada para OJS** (formato de la revista): **`Guerrero-Herrera, Nicolás`**. Ingrésala así en los metadatos del envío.
- [x] **Afiliación:** Investigador independiente (confirmada).
- [x] **Correo:** n.icolashrra@gmail.com (personal, coherente con autoría independiente).

## Pendientes que solo tú puedes completar ✍

1. **ORCID (obligatorio).** Si no tienes, se crea gratis en https://orcid.org (5 minutos). Se ingresa en los metadatos del envío en OJS.
2. **Registro e inicio de sesión** en el portal OJS de la revista, y carga del manuscrito + figuras. Firma normalizada: `Guerrero-Herrera, Nicolás`.
3. **Declaración de autoría única** y consentimiento con la versión final (parte del formulario OJS).
4. **Agradecimientos / financiamiento**: si no hay financiamiento, no se agrega la sección. Si algún fondo aplicara, usar el formato ANID normalizado de las directrices.
5. **Nota sobre el preprint**: el manuscrito circula como working paper en GitHub. En los "comentarios al editor" del envío conviene declararlo: "Una versión de trabajo (preprint) está disponible en el repositorio público del proyecto; el manuscrito no ha sido publicado en ninguna revista ni está sometido a otra revista."

## Pendientes editoriales menores (opcionales antes de enviar)

- **Páginas de referencias**: ~25 referencias de revista aún no llevan rango de páginas (solo se incluyeron las verificadas: Blau y Kahn; Blinder; Croson y Gneezy; Goldin 2014; Kleven et al. 2019; Mueller y Plug; Neumark; Niederle y Vesterlund; Ñopo 2008; Oaxaca; Petersen y Morgan; Phelps; Sánchez et al.). Completar el resto verificando contra las revistas — puedo hacerlo con búsqueda web en una sesión.
- **Separador decimal**: el manuscrito usa punto decimal (-15.3%). Si el equipo editorial prefiere coma (-15,3%), es una transformación mecánica que puedo aplicar.
- El anonimato del manuscrito: la versión actual no incluye nombre de autor (los metadatos van en OJS). Si la revista pide una portada con datos del autor en el archivo, agregarla al inicio.
