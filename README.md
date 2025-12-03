# CV Harvard – Generador de CV en Español e Inglés

Este repositorio permite generar tu CV en formato estilo Harvard (PDF) a partir de un archivo JSON con tus datos, en dos idiomas: español e inglés.

## Requisitos
- Python 3.10+
- Paquete `reportlab`

Instalación de dependencias:
```
pip install reportlab
```

## Estructura
- `CV.py`: Script principal que lee datos desde `cv_data.json` y genera dos PDFs.
- `cv_data.json`: Archivo con tus datos en español e inglés.
- `VERSIONES/`: Carpeta donde se guardan los PDFs generados (puedes cambiar la ruta en `CV.py`).

## Cómo usar
1. Clona este repositorio.
2. Abre y completa `cv_data.json` con tu información.
3. Ejecuta el script:
```
python CV.py
```
Esto generará:
- `CVFelipeSandovalCornejo.pdf` (Español)
- `CVFelipeSandovalCornejo_EN.pdf` (Inglés)

Si deseas usar otro archivo de datos, reemplaza el nombre en `CV.py` (variable `ruta_json`) o solicita una versión con argumento `--data`.

## Formato del JSON (`cv_data.json`)
El archivo contiene dos secciones: `español` e `inglés`. Cada una incluye:
- Datos principales (nombre, título/degree, ubicación/location, contacto/contact)
- Perfil/Professional Summary
- Educación/Education
- Experiencia/Work Experience
- Certificaciones/Certifications
- Habilidades/Skills
- Información adicional/Additional Information

Puedes usar como referencia `cv_data_base.json`.

## Prompt para IA (rellenar `cv_data.json`)
Copia y pega este prompt en tu asistente de IA favorito. Adjunta tu CV actual en PDF y pide que complete el JSON respetando esta estructura.

```
Quiero transformar mi CV a formato Harvard usando un JSON.
Adjunto mi CV en PDF. Completa un archivo `cv_data.json` con esta estructura exacta:

{
  "español": {
    "principal": {
      "nombre": "",
      "titulo": "",
      "ubicacion": "",
      "contacto": { "correo": "", "telefono": "", "linkedin": "", "github": "" }
    },
    "perfil_profesional": "",
    "educacion": [ { "institucion": "", "periodo": "", "detalle": "" } ],
    "experiencia_laboral": [ { "empresa": "", "cargo": "", "periodo": "", "logros": [""] } ],
    "certificaciones": [ { "institucion": "", "certificacion": "", "link": "", "anio": "" } ],
    "habilidades": { "tecnicas": [""], "idiomas": [ { "idioma": "", "nivel": "" } ] },
    "informacion_adicional": { "nacionalidad": "", "fecha_nacimiento": "", "rut": "", "licencia_conducir": "" }
  },
  "inglés": {
    "principal": {
      "name": "",
      "degree": "",
      "location": "",
      "contact": { "email": "", "phone": "", "linkedin": "", "github": "" }
    },
    "professional_summary": "",
    "education": [ { "institution": "", "period": "", "detail": "" } ],
    "work_experience": [ { "company": "", "role": "", "period": "", "achievements": [""] } ],
    "certifications": [ { "organization": "", "certification": "", "link": "", "year": "" } ],
    "skills": { "technical": [""], "languages": [ { "language": "", "level": "" } ] },
    "additional_information": { "nationality": "", "date_of_birth": "", "id": "", "driver_license": "" }
  }
}

Reglas:
- Rellena ambos idiomas.
- Usa textos concisos y profesionales.
- Mantén los campos en español en español y los campos en inglés en inglés.
- Para las fechas usa el mismo formato del PDF enviado.
- Para links, incluye URL cuando exista.
- No cambies nombres de campos ni la estructura.
```

## Personalización de rutas
En `CV.py` puedes modificar `ruta_es` y `ruta_en` para definir dónde se guardan los PDFs.

## Contribuciones
Este es un repositorio público. Aceptamos PRs que:
- Mejoren la compatibilidad multiplataforma.
- Agreguen CLI (`--data`, `--lang`) manteniendo simplicidad.
- Corrijan estilos y tipografías manteniendo el formato Harvard.

## Licencia
Uso personal y educativo. Evita subir datos sensibles de terceros.# CV Harvard Version

Generate professional Harvard-style CVs in Spanish and English from a single JSON data file.

## Overview
- Single script: `CV.py` reads `cv_data.json` (same structure used in `cv_data_felo.json`).
- Outputs two PDFs:
  - `CVFelipeSandovalCornejo.pdf` (Spanish)
  - `CVFelipeSandovalCornejo_EN.pdf` (English)
- Styling and section order follow the Harvard layout defined in the script.

## Folder Structure
```
cv-harvard-version/
  CV.py
  cv_data_base.json   # schema reference
  cv_data.json        # your data (create this file)
```

## 1) Prepare your `cv_data.json`
Use `cv_data_base.json` as a template. Create a new file named `cv_data.json` with your data, keeping the same keys and structure for both `español` and `inglés` sections.

### JSON Schema (simplified)
- `español.principal`: `nombre`, `titulo`, `ubicacion`, `contacto` (`correo`, `telefono`, `linkedin`, `github`)
- `español.perfil_profesional`: string
- `español.educacion`: list of `{institucion, periodo, detalle}`
- `español.experiencia_laboral`: list of `{empresa, cargo, periodo, logros[]}`
- `español.certificaciones`: list of `{institucion, certificacion, link, anio}`
- `español.habilidades`: `tecnicas[]`, `idiomas[]` with `{idioma, nivel}`
- `español.informacion_adicional`: `{nacionalidad, fecha_nacimiento, rut, licencia_conducir}`
- `inglés.principal`: `name`, `degree`, `location`, `contact` (`email`, `phone`, `linkedin`, `github`)
- `inglés.professional_summary`: string
- `inglés.education`: list of `{institution, period, detail}`
- `inglés.work_experience`: list of `{company, role, period, achievements[]}`
- `inglés.certifications`: list of `{organization, certification, link, year}`
- `inglés.skills`: `technical[]`, `languages[]` with `{language, level}`
- `inglés.additional_information`: `{nationality, date_of_birth, id, driver_license}`

## 2) Optional: Use AI to fill `cv_data.json`
If you have your current CV as a PDF or text, you can ask an AI to convert it to this JSON. Provide your PDF and the following prompt:

```
You are given my CV. Convert it into a JSON that matches exactly this schema with two sections: "español" and "inglés". Do not invent data. Use the closest translation for the English section. Keep arrays where the schema uses arrays. Keep keys and nesting identical. If some fields are missing, leave empty strings. Include links when available.

Schema examples:
- español.principal: nombre, titulo, ubicacion, contacto { correo, telefono, linkedin, github }
- español.perfil_profesional: string
- español.educacion: [ { institucion, periodo, detalle } ]
- español.experiencia_laboral: [ { empresa, cargo, periodo, logros: ["..."] } ]
- español.certificaciones: [ { institucion, certificacion, link, anio } ]
- español.habilidades: tecnicas: ["..."], idiomas: [ { idioma, nivel } ]
- español.informacion_adicional: { nacionalidad, fecha_nacimiento, rut, licencia_conducir }
- inglés.principal: name, degree, location, contact { email, phone, linkedin, github }
- inglés.professional_summary: string
- inglés.education: [ { institution, period, detail } ]
- inglés.work_experience: [ { company, role, period, achievements: ["..."] } ]
- inglés.certifications: [ { organization, certification, link, year } ]
- inglés.skills: technical: ["..."], languages: [ { language, level } ]
- inglés.additional_information: { nationality, date_of_birth, id, driver_license }

Return only valid JSON in UTF-8, no comments.
```

Save the AI result into `cv_data.json` at the repository root (`cv-harvard-version/`).

## 3) Install dependencies
This project uses `reportlab`.

```cmd
pip install reportlab
```

## 4) Generate your PDFs
Run the script from the project folder. By default it looks for `cv_data_felo.json`. To use your file, rename it to `cv_data.json` or adapt the path inside `CV.py`.

```cmd
cd "g:\My Drive\(4) INFORMÁTICA\CÓDIGOS\PYTHON\CV\cv-harvard-version"
python CV.py
```

Outputs:
- `G:\My Drive\(3) DOCS\TRABAJO\CV\VERSIONES\CVFelipeSandovalCornejo.pdf`
- `G:\My Drive\(3) DOCS\TRABAJO\CV\VERSIONES\CVFelipeSandovalCornejo_EN.pdf`

## Notes
- Links in certifications are optional; if missing, the entry is rendered without a link.
- Keep the JSON keys exactly as in `cv_data_base.json` to avoid layout issues.
- This is a public repository: anyone can clone, prepare their own `cv_data.json`, and generate their CVs.
