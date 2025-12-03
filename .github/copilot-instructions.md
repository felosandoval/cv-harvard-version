# Instrucciones de Copilot para cv-harvard-version

Guía concisa para que agentes de IA trabajen productivamente en este repositorio. Sigue convenciones específicas del proyecto y mantén el contenido en español.

## Panorama General
- Propósito: Generar CV en estilo Harvard (PDF) en español e inglés a partir de un único archivo JSON.
- Punto de entrada: `CV.py` lee `cv_data.json` y construye dos documentos usando `reportlab`.
- Salidas actuales: `CV.pdf` y `CV_EN.pdf` en la raíz del repositorio.
- Maquetación: Se implementa con componentes de `reportlab.platypus` y estilos `ParagraphStyle` definidos al inicio de `CV.py`.

## Convenciones
- Idioma: Toda documentación, comentarios y nombres de archivo deben estar en español. Ver `INSTRUCCIONES.md`.
- Esquema JSON: Mantén claves y estructura exactamente como en `cv_data_base.json`/`README.md`. Dos secciones principales: `español` e `inglés`.
- Estilo tipográfico: Formato Harvard con fuentes Times y títulos de sección en mayúsculas. Preserva el orden de secciones usado en `CV.py`.
- Enlaces: Las certificaciones pueden incluir `link` opcional; renderiza hipervínculo azul solo si existe.

## Flujo de Datos y Estructura
- Entrada: `cv_data.json` con estructuras espejo para `español` e `inglés`.
- Constructores (ES): `encabezado_es`, `perfil_es`, `educacion_es`, `experiencia_es`, `certificaciones_es`, `habilidades_es`, `info_adicional_es`.
- Constructores (EN): `header_en`, `profile_en`, `education_en`, `experience_en`, `certifications_en`, `skills_en`, `additional_info_en`.
- Ensamblado: `construir_contenido_es(data)` y `build_content_en(data)` devuelven `List` de flowables para la generación de PDF.
- Escritura: `generar_pdf(contenido, ruta_salida)` crea PDFs A4 con márgenes consistentes.

## Flujos de Trabajo
- Dependencias: Python 3.10+ y `reportlab`.
- Instalación:
  - `pip install reportlab`
- Ejecución (Windows cmd):
  - `cd "g:\\My Drive\\(4) INFORMÁTICA\\CÓDIGOS\\PYTHON\\CV\\cv-harvard-version"`
  - `python CV.py`
- Salidas esperadas (`CV.py` actual):
  - `CV.pdf` (Español)
  - `CV_EN.pdf` (Inglés)

## Patrones del Proyecto
- Acceso defensivo: Usa `.get()` para campos opcionales (p. ej., `link` en certificaciones).
- Viñetas: Logros y habilidades usan `•` y sangría izquierda donde aplique.
- Títulos de sección: Usa `estilo_seccion` (mayúsculas) y `estilo_subseccion` para subsecciones.
- Texto justificado: Los perfiles usan `ParagraphStyle("JustifiedProfile", alignment=TA_JUSTIFY)`.

## Cambios Seguros
- Si cambias nombres o rutas de salida, actualiza el `README.md` y mantén comandos correctos para Windows `cmd`.
- Al añadir secciones, espeja constructores ES/EN y actualiza `construir_contenido_es` y `build_content_en` en el mismo orden.
- Compatibilidad JSON: No renombres claves; agrega nuevas claves opcionales solo si ambas lenguas las soportan y los constructores toleran su ausencia.
- Mantén documentación en español con ejemplos claros.

## Ejemplos del Código
- Certificaciones:
  - ES: Muestra institución, certificación, `(link)` opcional y `anio` alineado a la derecha.
  - EN: Muestra organización, certificación, `(link)` opcional y `year` alineado a la derecha.
- Habilidades:
  - ES: `habilidades.tecnicas[]` y `habilidades.idiomas[]` con `idioma` + `nivel`.
  - EN: `skills.technical[]` y `skills.languages[]` con `language` + `level`.

## Integraciones
- Biblioteca externa: `reportlab` (`platypus`, `Paragraph`, `Table`, `Spacer`, estilos). No hay otros servicios.
- I/O de archivos: Lee `cv_data.json` desde la raíz; ajusta `ruta_json` si agregas flags de CLI.

## Pruebas y Validación
- Comprobación rápida: Ejecuta `python CV.py` y confirma que ambos PDFs se generan sin excepciones.
- Validación de esquema: Verifica manualmente que existan las claves requeridas; los constructores dependen de las secciones principales.

## Posibles Mejoras (mantén el estilo)
- CLI: Agregar `--data` para seleccionar una ruta JSON alternativa; por defecto `cv_data.json`.
- Rutas de salida: Considera `VERSIONES/` o directorios específicos del usuario; mantén rutas amigables para Windows.

## Archivos Clave
- `CV.py`: Generación del PDF y estilos.
- `cv_data.json`: Datos del usuario en español e inglés.
- `INSTRUCCIONES.md`: Guía del repositorio en español.
- `README.md`: Uso, esquema y ejemplos de prompts para IA.
