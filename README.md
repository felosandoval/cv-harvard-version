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