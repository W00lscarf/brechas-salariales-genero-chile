# -*- coding: utf-8 -*-
"""Convierte manuscript_applied_economics.md en el PDF del articulo (formato revista).

Requiere: reportlab, pypdf; Windows con Times New Roman y Courier New instaladas.
Uso:  python generar_pdf_en.py   (desde la carpeta policy_paper/)
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                 Spacer, Table, TableStyle, Image, PageBreak,
                                 KeepTogether)

BASE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(BASE, 'manuscript_applied_economics.md')
OUT = os.path.join(BASE, 'manuscript_applied_economics.pdf')

# ----------------------------- Fuentes -----------------------------
F = r'C:\Windows\Fonts'
pdfmetrics.registerFont(TTFont('TimesNR', os.path.join(F, 'times.ttf')))
pdfmetrics.registerFont(TTFont('TimesNR-B', os.path.join(F, 'timesbd.ttf')))
pdfmetrics.registerFont(TTFont('TimesNR-I', os.path.join(F, 'timesi.ttf')))
pdfmetrics.registerFont(TTFont('TimesNR-BI', os.path.join(F, 'timesbi.ttf')))
pdfmetrics.registerFont(TTFont('CourierNW', os.path.join(F, 'cour.ttf')))
registerFontFamily('TimesNR', normal='TimesNR', bold='TimesNR-B',
                   italic='TimesNR-I', boldItalic='TimesNR-BI')

# ----------------------------- Estilos -----------------------------
def st(name, **kw):
    base = dict(fontName='TimesNR', fontSize=11, leading=14.5,
                alignment=TA_JUSTIFY, spaceAfter=7)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
    'title':    st('title', fontName='TimesNR-B', fontSize=20, leading=24,
                   alignment=TA_CENTER, spaceAfter=10),
    'subtitle': st('subtitle', fontName='TimesNR', fontSize=13, leading=17,
                   alignment=TA_CENTER, spaceAfter=14),
    'meta':     st('meta', fontName='TimesNR-I', fontSize=10, leading=13,
                   alignment=TA_CENTER, spaceAfter=4),
    'h1':       st('h1', fontName='TimesNR-B', fontSize=14, leading=17,
                   alignment=TA_LEFT, spaceBefore=16, spaceAfter=8),
    'h2':       st('h2', fontName='TimesNR-B', fontSize=12, leading=15,
                   alignment=TA_LEFT, spaceBefore=12, spaceAfter=6),
    'body':     st('body'),
    'abstract': st('abstract', fontSize=10.5, leading=13.8,
                   leftIndent=0.45*inch, rightIndent=0.45*inch),
    'quote':    st('quote', fontName='TimesNR-I', leftIndent=0.4*inch,
                   rightIndent=0.4*inch, spaceBefore=6, spaceAfter=10),
    'bullet':   st('bullet', leftIndent=0.28*inch, bulletIndent=0.1*inch,
                   spaceAfter=5),
    'numitem':  st('numitem', leftIndent=0.28*inch, spaceAfter=5),
    'tcap':     st('tcap', fontName='TimesNR-B', alignment=TA_LEFT,
                   spaceBefore=10, spaceAfter=1),
    'ttitle':   st('ttitle', fontName='TimesNR-I', alignment=TA_LEFT,
                   spaceAfter=6),
    'tnote':    st('tnote', fontSize=9, leading=11.5, alignment=TA_LEFT,
                   spaceBefore=5, spaceAfter=12),
    'cell':     st('cell', fontSize=9, leading=11, alignment=TA_LEFT,
                   spaceAfter=0),
    'cellh':    st('cellh', fontName='TimesNR-B', fontSize=9, leading=11,
                   alignment=TA_LEFT, spaceAfter=0),
    'ref':      st('ref', fontSize=10, leading=12.5, alignment=TA_LEFT,
                   leftIndent=0.3*inch, firstLineIndent=-0.3*inch,
                   spaceAfter=4),
    'refhead':  st('refhead', fontName='TimesNR-B', fontSize=11,
                   alignment=TA_LEFT, spaceBefore=10, spaceAfter=6),
}

# ----------------------------- Inline markdown -----------------------------
def fmt(s):
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)                       # imagenes sueltas
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)                 # links -> texto
    s = re.sub(r'`([^`]+)`', r'<font face="CourierNW" size="8.5">\1</font>', s)
    s = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<b><i>\1</i></b>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*([^*\n]+)\*', r'<i>\1</i>', s)
    return s

def strip_md(s):
    return re.sub(r'[*`]', '', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s))

# ----------------------------- Tablas -----------------------------
def build_table(rows):
    ncols = len(rows[0])
    lens = []
    for c in range(ncols):
        lens.append(max(len(strip_md(r[c])) for r in rows if c < len(r)))
    w = [max(l, 6) ** 0.62 for l in lens]
    total = 6.7 * inch
    widths = [max(0.55 * inch, total * x / sum(w)) for x in w]
    esc = total / sum(widths)
    widths = [x * esc for x in widths]

    data = []
    for i, r in enumerate(rows):
        stl = S['cellh'] if i == 0 else S['cell']
        data.append([Paragraph(fmt(c), stl) for c in r])
    tb = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    tb.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, 0), 1, colors.black),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return tb

def parse_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

# ----------------------------- Parseo del documento -----------------------------
lines = open(MD, encoding='utf-8').read().split('\n')
story = []

# --- Portada ---
i_abs = next(i for i, l in enumerate(lines) if l.startswith('## Abstract'))
head = lines[:i_abs]
title = next(l[2:].strip() for l in head if l.startswith('# '))
autor_lineas = [l.replace('@@AUTOR@@', '').strip() for l in head if l.startswith('@@AUTOR@@')]

story.append(Spacer(1, 1.0 * inch))
story.append(Paragraph(fmt(title), S['title']))
story.append(Spacer(1, 0.3 * inch))
for al in autor_lineas:
    story.append(Paragraph(fmt(al), S['meta']))
story.append(Paragraph('July 2026', S['meta']))
story.append(Spacer(1, 0.45 * inch))

# --- Cuerpo ---
i = i_abs
n = len(lines)
in_refs = False
in_abstract = False

while i < n:
    line = lines[i].rstrip()

    if not line.strip() or line.strip() == '---':
        i += 1
        continue

    if line.startswith('@@AUTOR@@'):
        i += 1
        continue

    # Encabezados
    if line.startswith('## '):
        h = line[3:].strip()
        in_refs = h.startswith('References')
        in_abstract = h == 'Abstract'
        if h.startswith(('1. Introduction', 'References')):
            story.append(PageBreak())
        story.append(Paragraph(fmt(h), S['h1']))
        i += 1
        continue
    if line.startswith('### '):
        story.append(Paragraph(fmt(line[4:].strip()), S['h2']))
        i += 1
        continue

    # Bloque de cita (pregunta de investigacion)
    if line.startswith('> '):
        buf = []
        while i < n and lines[i].startswith('>'):
            buf.append(lines[i].lstrip('> ').strip())
            i += 1
        story.append(Paragraph(fmt(' '.join(buf)), S['quote']))
        continue

    # Caption de tabla / figura
    m = re.match(r'^\*\*(Table|Figure) (\d+)\*\*$', line.strip())
    if m:
        kind = m.group(1)
        cap = Paragraph(fmt(line.strip()), S['tcap'])
        i += 1
        ttl = Paragraph(fmt(lines[i].strip()), S['ttitle'])
        i += 1
        while i < n and not lines[i].strip():
            i += 1
        if kind == 'Table':
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                if not re.match(r'^\|[\s:\-|]+\|$', lines[i].strip()):
                    rows.append(parse_row(lines[i]))
                i += 1
            body = build_table(rows)
        else:
            img_m = re.match(r'!\[[^\]]*\]\(([^)]+)\)', lines[i].strip())
            p = os.path.normpath(os.path.join(BASE, img_m.group(1)))
            iw, ih = ImageReader(p).getSize()
            wdt = min(5.9 * inch, iw)
            body = Image(p, width=wdt, height=wdt * ih / iw)
            body.hAlign = 'LEFT'
            i += 1
        while i < n and not lines[i].strip():
            i += 1
        note = Paragraph(fmt(lines[i].strip()), S['tnote'])
        i += 1
        story.append(KeepTogether([cap, ttl, body, note]))
        continue

    # Sub-encabezados de referencias
    if in_refs and re.match(r'^\*\*[^*]+\*\*$', line.strip()):
        story.append(Paragraph(fmt(line.strip()), S['refhead']))
        i += 1
        continue

    # Vinetas
    if line.startswith('- '):
        txt = line[2:].strip()
        i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(('- ', '#', '|', '>', '**Table', '**Figure')) and not re.match(r'^\d+\. ', lines[i]):
            txt += ' ' + lines[i].strip()
            i += 1
        if in_refs:
            story.append(Paragraph(fmt(txt), S['ref']))
        else:
            story.append(Paragraph(fmt(txt), S['bullet'], bulletText='•'))
        continue

    # Items numerados
    mnum = re.match(r'^(\d+)\. (.*)$', line)
    if mnum:
        txt = line
        i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(('- ', '#', '|', '>')) and not re.match(r'^\d+\. ', lines[i]):
            txt += ' ' + lines[i].strip()
            i += 1
        story.append(Paragraph(fmt(txt), S['numitem']))
        continue

    # Parrafo normal (acumula hasta linea en blanco)
    buf = [line.strip()]
    i += 1
    while i < n and lines[i].strip() and not lines[i].startswith(('#', '- ', '|', '>')) \
            and not re.match(r'^\d+\. ', lines[i]) \
            and not re.match(r'^\*\*(Table|Figure) \d+\*\*$', lines[i].strip()):
        buf.append(lines[i].strip())
        i += 1
    text = ' '.join(buf)
    style = S['abstract'] if in_abstract and not text.startswith('**Keywords') \
        and not text.startswith('**JEL') else S['body']
    story.append(Paragraph(fmt(text), style))

# ----------------------------- Documento -----------------------------
RUNNING_HEAD = 'SAME OCCUPATION, DIFFERENT PAY'

def on_page(canv, doc):
    canv.saveState()
    canv.setFont('TimesNR', 9)
    pn = canv.getPageNumber()
    canv.drawRightString(7.5 * inch, 10.45 * inch, str(pn))
    if pn > 1:
        canv.drawString(1 * inch, 10.45 * inch, RUNNING_HEAD)
    canv.restoreState()

doc = BaseDocTemplate(OUT, pagesize=letter,
                      leftMargin=1 * inch, rightMargin=1 * inch,
                      topMargin=0.9 * inch, bottomMargin=0.9 * inch,
                      title='Same Occupation, Different Pay: The Gender Gap That '
                            'Composition Does Not Explain',
                      author='W00lscarf',
                      subject='Gender wage gap in Chile — working paper',
                      creator='Reproducible pipeline (reportlab)')
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=on_page)])
doc.build(story)

from pypdf import PdfReader
r = PdfReader(OUT)
print(f'OK: {OUT}')
print(f'Paginas: {len(r.pages)}  |  Tamano: {os.path.getsize(OUT):,} bytes')
