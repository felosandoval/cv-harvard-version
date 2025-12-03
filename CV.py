import json
import os
from typing import List, Dict

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.units import cm

# Estilos tipo Harvard Business
estilo_normal = ParagraphStyle("Normal", fontName="Times-Roman", fontSize=11, leading=14)
estilo_negrita = ParagraphStyle("Negrita", parent=estilo_normal, fontName="Times-Bold")
estilo_cursiva = ParagraphStyle("Cursiva", parent=estilo_normal, fontName="Times-Italic")
estilo_titulo = ParagraphStyle("Titulo", parent=estilo_negrita, fontSize=18, alignment=TA_CENTER, spaceAfter=12)
estilo_subtitulo = ParagraphStyle("Subtitulo", parent=estilo_cursiva, alignment=TA_CENTER)
estilo_seccion = ParagraphStyle("Seccion", parent=estilo_negrita, fontSize=12, spaceBefore=14, spaceAfter=6, uppercase=True)
estilo_subseccion = ParagraphStyle("Subseccion", parent=estilo_negrita, fontSize=11, spaceBefore=6, spaceAfter=4)
estilo_fecha = ParagraphStyle("Fecha", parent=estilo_cursiva, alignment=TA_RIGHT)


def leer_json(ruta_json: str) -> Dict:
    with open(ruta_json, "r", encoding="utf-8") as f:
        return json.load(f)


def encabezado_es(data: Dict) -> List:
    contenido = []
    p = data["español"]["principal"]
    contacto = p["contacto"]
    contenido.append(Paragraph(p["nombre"], estilo_titulo))
    contenido.append(Paragraph(p["titulo"], estilo_subtitulo))
    contenido.append(Paragraph(p["ubicacion"], estilo_subtitulo))
    contenido.append(Paragraph(f'Correo: <a href="mailto:{contacto.get("correo", "")}">{contacto.get("correo", "")}</a> | Tel: <a href="tel:{contacto.get("telefono", "")}">{contacto.get("telefono", "")}</a>', estilo_subtitulo))
    contenido.append(Paragraph(f'<a href="{contacto.get("linkedin", "")}"><font color="blue">linkedin.com/in/felosandoval</font></a> | <a href="{contacto.get("github", "")}"><font color="blue">GitHub.com/felosandoval</font></a>', estilo_subtitulo))
    contenido.append(Spacer(1, 16))
    return contenido


def perfil_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("PERFIL PROFESIONAL", estilo_seccion))
    contenido.append(Paragraph(
        data["español"].get("perfil_profesional", ""),
        ParagraphStyle("JustifiedProfile", parent=estilo_normal, alignment=TA_JUSTIFY)
    ))
    return contenido


def educacion_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("EDUCACIÓN", estilo_seccion))
    for edu in data["español"].get("educacion", []):
        contenido.append(Table([[Paragraph(f'<b>{edu.get("institucion", "")}</b>', estilo_normal), Paragraph(edu.get("periodo", ""), estilo_fecha)]]))
        if edu.get("detalle"):
            contenido.append(Paragraph(edu.get("detalle"), estilo_normal))
    return contenido


def experiencia_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("EXPERIENCIA PROFESIONAL", estilo_seccion))
    for exp in data["español"].get("experiencia_laboral", []):
        contenido.append(Table([[Paragraph(f'<b>{exp.get("empresa", "")}</b><br/>{exp.get("cargo", "")}', estilo_normal), Paragraph(exp.get("periodo", ""), estilo_fecha)]]))
        for logro in exp.get("logros", []):
            contenido.append(Paragraph(f'• {logro}', ParagraphStyle("Indented", parent=estilo_normal, leftIndent=15)))
    return contenido


def certificaciones_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("CERTIFICACIONES", estilo_seccion))
    filas = []
    for cert in data["español"].get("certificaciones", []):
        filas.append([Paragraph(f'<b>{cert.get("institucion", "")}</b>', ParagraphStyle("ReducedSpace", parent=estilo_normal, spaceAfter=2, spaceBefore=2)), ""]) 
        link = cert.get("link", "")
        link_html = f'(<a href="{link}"><font color="blue">link</font></a>)' if link else ""
        filas.append([Paragraph(f'{cert.get("certificacion", "")} {link_html}', ParagraphStyle("ReducedSpace", parent=estilo_normal, spaceAfter=2, spaceBefore=2)), Paragraph(cert.get("anio", ""), estilo_fecha)])
    if filas:
        contenido.append(Table(filas))
    return contenido


def habilidades_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("HABILIDADES", estilo_seccion))
    contenido.append(Paragraph("TÉCNICAS", estilo_subseccion))
    tecnicas = data["español"].get("habilidades", {}).get("tecnicas", [])
    contenido.append(Paragraph("• " + "<br/>• ".join(tecnicas), estilo_normal))
    contenido.append(Paragraph("IDIOMAS", estilo_subseccion))
    idiomas = data["español"].get("habilidades", {}).get("idiomas", [])
    for item in idiomas:
        contenido.append(Paragraph(f'• {item.get("idioma", "")}: {item.get("nivel", "")}', estilo_normal))
    return contenido


def info_adicional_es(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("INFORMACIÓN ADICIONAL", estilo_seccion))
    info = data["español"].get("informacion_adicional", {})
    contenido.append(Paragraph(f'Nacionalidad: {info.get("nacionalidad", "")}', estilo_normal))
    contenido.append(Paragraph(f'Fecha de nacimiento: {info.get("fecha_nacimiento", "")}', estilo_normal))
    contenido.append(Paragraph(f'RUT: {info.get("rut", "")}', estilo_normal))
    contenido.append(Paragraph(f'Licencia de conducir: {info.get("licencia_conducir", "")}', estilo_normal))
    return contenido


def construir_contenido_es(data: Dict) -> List:
    contenido = []
    contenido += encabezado_es(data)
    contenido += perfil_es(data)
    contenido += educacion_es(data)
    contenido += experiencia_es(data)
    contenido += certificaciones_es(data)
    contenido += habilidades_es(data)
    contenido += info_adicional_es(data)
    return contenido


# English content builders
def header_en(data: Dict) -> List:
    contenido = []
    p = data["inglés"]["principal"]
    contact = p["contact"]
    contenido.append(Paragraph(p["name"], estilo_titulo))
    contenido.append(Paragraph(p["degree"], estilo_subtitulo))
    contenido.append(Paragraph(p["location"], estilo_subtitulo))
    contenido.append(Paragraph(f'Email: <a href="mailto:{contact.get("email", "")}">{contact.get("email", "")}</a> | Phone: <a href="tel:{contact.get("phone", "")}">{contact.get("phone", "")}</a>', estilo_subtitulo))
    contenido.append(Paragraph(f'<a href="{contact.get("linkedin", "")}"><font color="blue">linkedin.com/in/felosandoval</font></a> | <a href="{contact.get("github", "")}"><font color="blue">GitHub.com/felosandoval</font></a>', estilo_subtitulo))
    contenido.append(Spacer(1, 16))
    return contenido


def profile_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("PROFESSIONAL PROFILE", estilo_seccion))
    contenido.append(Paragraph(
        data["inglés"].get("professional_summary", ""),
        ParagraphStyle("JustifiedProfile", parent=estilo_normal, alignment=TA_JUSTIFY)
    ))
    return contenido


def education_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("EDUCATION", estilo_seccion))
    for edu in data["inglés"].get("education", []):
        contenido.append(Table([[Paragraph(f'<b>{edu.get("institution", "")}</b>', estilo_normal), Paragraph(edu.get("period", ""), estilo_fecha)]]))
        if edu.get("detail"):
            contenido.append(Paragraph(edu.get("detail"), estilo_normal))
    return contenido


def experience_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("PROFESSIONAL EXPERIENCE", estilo_seccion))
    for exp in data["inglés"].get("work_experience", []):
        contenido.append(Table([[Paragraph(f'<b>{exp.get("company", "")}</b><br/>{exp.get("role", "")}', estilo_normal), Paragraph(exp.get("period", ""), estilo_fecha)]]))
        for ach in exp.get("achievements", []):
            contenido.append(Paragraph(f'• {ach}', ParagraphStyle("Indented", parent=estilo_normal, leftIndent=15)))
    return contenido


def certifications_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("CERTIFICATIONS", estilo_seccion))
    filas = []
    for cert in data["inglés"].get("certifications", []):
        filas.append([Paragraph(f'<b>{cert.get("organization", "")}</b>', ParagraphStyle("ReducedSpace", parent=estilo_normal, spaceAfter=2, spaceBefore=2)), ""]) 
        link = cert.get("link", "")
        link_html = f'(<a href="{link}"><font color="blue">link</font></a>)' if link else ""
        filas.append([Paragraph(f'{cert.get("certification", "")} {link_html}', ParagraphStyle("ReducedSpace", parent=estilo_normal, spaceAfter=2, spaceBefore=2)), Paragraph(cert.get("year", ""), estilo_fecha)])
    if filas:
        contenido.append(Table(filas))
    return contenido


def skills_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("SKILLS", estilo_seccion))
    contenido.append(Paragraph("TECHNICAL", estilo_subseccion))
    tecnicas = data["inglés"].get("skills", {}).get("technical", [])
    contenido.append(Paragraph("• " + "<br/>• ".join(tecnicas), estilo_normal))
    contenido.append(Paragraph("LANGUAGES", estilo_subseccion))
    idiomas = data["inglés"].get("skills", {}).get("languages", [])
    for item in idiomas:
        contenido.append(Paragraph(f'• {item.get("language", "")}: {item.get("level", "")}', estilo_normal))
    return contenido


def additional_info_en(data: Dict) -> List:
    contenido = []
    contenido.append(Paragraph("ADDITIONAL INFORMATION", estilo_seccion))
    info = data["inglés"].get("additional_information", {})
    contenido.append(Paragraph(f'Nationality: {info.get("nationality", "")}', estilo_normal))
    contenido.append(Paragraph(f'Date of Birth: {info.get("date_of_birth", "")}', estilo_normal))
    contenido.append(Paragraph(f'ID: {info.get("id", "")}', estilo_normal))
    contenido.append(Paragraph(f"Driver's License: {info.get("driver_license", "")}", estilo_normal))
    return contenido


def build_content_en(data: Dict) -> List:
    contenido = []
    contenido += header_en(data)
    contenido += profile_en(data)
    contenido += education_en(data)
    contenido += experience_en(data)
    contenido += certifications_en(data)
    contenido += skills_en(data)
    contenido += additional_info_en(data)
    return contenido


def generar_pdf(contenido: List, ruta_salida: str):
    documento = SimpleDocTemplate(ruta_salida, pagesize=A4,
                                  rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    documento.build(contenido)


def main():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_base, "cv_data.json")
    data = leer_json(ruta_json)

    ruta_es = "CV.pdf"
    ruta_en = "CV_EN.pdf"

    contenido_es = construir_contenido_es(data)
    generar_pdf(contenido_es, ruta_es)
    print("✅ CV en español generado correctamente.")

    # Insert page break for English section only in its own document where needed
    contenido_en = build_content_en(data)
    generar_pdf(contenido_en, ruta_en)
    print("✅ CV in English generated successfully.")


if __name__ == "__main__":
    main()
