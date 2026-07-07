# -*- coding: utf-8 -*-
"""Genera las versiones en inglés de las figuras del documento de trabajo
(policy_paper/README_EN.md) a partir de los datos ya derivados por los
notebooks 08 y 09 — no requiere re-ejecutar los modelos.

Uso:  python generar_figuras_en.py   (desde la carpeta notebooks/)
"""
import json
import re
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid', font_scale=1.05)
FIG = 'outputs/figures'

# ---------------------------------------------------------------
# Figure 1: raw vs adjusted gap by occupation (nb08, section 7)
# ---------------------------------------------------------------
df = pd.read_csv('outputs/data/ranking_brecha_ocupacion_ajustada.csv', encoding='utf-8-sig')

fig, ax = plt.subplots(figsize=(8, 8))
colores = df['significativo'].map({True: '#c0392b', False: '#bdc3c7'})
ax.scatter(df['brecha_cruda_pct'], df['gap_ajustado_pct'],
           c=colores, s=25, alpha=0.8, edgecolor='white', linewidth=0.3)
lims = [-70, 60]
ax.plot(lims, lims, color='gray', linestyle='--', linewidth=1, label='No change (raw = adjusted)')
ax.axhline(0, color='black', linewidth=0.6)
ax.axvline(0, color='black', linewidth=0.6)
ax.set_xlim(lims); ax.set_ylim(lims)
ax.set_xlabel('Raw gap by occupation (%)')
ax.set_ylabel('Adjusted gap by occupation (%)\n(age, education, hours, children, marital status, year)')
ax.set_title('Does the occupation-level gap change when isolating the sex effect?\n'
             'Red = statistically significant (p < .05), gray = not significant',
             fontsize=11, fontweight='bold')
ax.legend(loc='upper left', fontsize=9)
sns.despine(); plt.tight_layout()
plt.savefig(f'{FIG}/ranking_ajustado_vs_crudo_en.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK Figure 1 (ranking_ajustado_vs_crudo_en.png)')

# ---------------------------------------------------------------
# Figure 2: gap along the wage distribution (nb09, section 6)
# Los cuantiles se extraen de las salidas del notebook ejecutado.
# ---------------------------------------------------------------
nb = json.load(open('09_robustez.ipynb', encoding='utf-8'))
cuantiles, brechas = [], []
for c in nb['cells']:
    if c['cell_type'] != 'code':
        continue
    for o in c.get('outputs', []):
        txt = ''.join(o.get('text', []))
        for m in re.finditer(r'q(\d+): brecha =\s*(-?\d+\.\d)%', txt):
            cuantiles.append(int(m.group(1)))
            brechas.append(float(m.group(2)))
if len(cuantiles) != 5:
    sys.exit(f'ERROR: se esperaban 5 cuantiles en 09_robustez.ipynb, se encontraron {len(cuantiles)}')

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(cuantiles, brechas, marker='o', color='#8e44ad', linewidth=2)
for q, b in zip(cuantiles, brechas):
    ax.annotate(f'{b:.1f}%', (q, b), textcoords='offset points', xytext=(0, -15),
                ha='center', fontsize=9, fontweight='bold')
ax.axhline(-15.3, color='gray', linestyle='--', linewidth=1, label='Mean gap (WLS, -15.3%)')
ax.set_xlabel('Quantile of the wage distribution')
ax.set_ylabel('Adjusted gap (%)')
ax.set_title('Sticky floor and glass ceiling: the gap along the wage distribution',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
sns.despine(); plt.tight_layout()
plt.savefig(f'{FIG}/brecha_por_cuantil_en.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK Figure 2 (brecha_por_cuantil_en.png)')

# ---------------------------------------------------------------
# Figure 3: robustness of specifications (nb09, synthesis)
# ---------------------------------------------------------------
TRADUCCION = {
    'Mensual + control horas | ocupación 1 dígito': 'Monthly + hours control | 1-digit occupation',
    'Mensual + control horas | ocupación 4 dígitos': 'Monthly + hours control | 4-digit occupation',
    'Salario/hora | ocupación 1 dígito': 'Hourly wage | 1-digit occupation',
    'Salario/hora | ocupación 4 dígitos': 'Hourly wage | 4-digit occupation',
    'Edad prima 25-59 | ocupación 4 dígitos': 'Prime age 25-59 | 4-digit occupation',
    'Ingreso recortado p1-p99 | ocupación 4 dígitos': 'Income trimmed p1-p99 | 4-digit occupation',
    'Jornada completa 40-45 hrs | ocupación 4 dígitos': 'Full-time 40-45 hrs | 4-digit occupation',
    'Asalariados formales (cotizan) | ocupación 4 dígitos': 'Formal employees (contributors) | 4-digit occupation',
    'Asalariados contrato firmado | ocupación 4 dígitos': 'Employees with signed contract | 4-digit occupation',
    'Asalariados informales (no cotizan) | ocupación 4 dígitos': 'Informal employees (non-contributors) | 4-digit occupation',
    'Independientes | ocupación 4 dígitos': 'Self-employed | 4-digit occupation',
    'Asal. sector público | ocupación 4 dígitos': 'Public sector employees | 4-digit occupation',
    'Asal. sector privado | ocupación 4 dígitos': 'Private sector employees | 4-digit occupation',
    'Formalidad como control | ocupación 4 dígitos': 'Formality as a control | 4-digit occupation',
    'Especificación máxima (todos los controles) | ocupación 4 dígitos': 'Maximal specification (all controls) | 4-digit occupation',
    'Máxima + región y zona urbano/rural | ocupación 4 dígitos': 'Maximal + region and urban/rural zone | 4-digit occupation',
    'Máxima + geografía + tipo institución ed. sup. | ocupación 4 dígitos': 'Maximal + geography + higher-ed institution type | 4-digit occupation',
    'Solo universitarios, con tipo de institución | ocupación 4 dígitos': 'University graduates only, with institution type | 4-digit occupation',
}

dfr = pd.read_csv('outputs/data/robustez_especificaciones.csv', encoding='utf-8-sig')
faltantes = [e for e in dfr['especificacion'] if e not in TRADUCCION]
if faltantes:
    sys.exit(f'ERROR: especificaciones sin traducción: {faltantes}')
dfr['spec_en'] = dfr['especificacion'].map(TRADUCCION)

fig, ax = plt.subplots(figsize=(9, 7.8))
orden = dfr.sort_values('brecha_pct', ascending=True)
y_pos = range(len(orden))
ax.barh(y_pos, orden['brecha_pct'],
        xerr=[orden['brecha_pct'] - orden['ic_lo'], orden['ic_hi'] - orden['brecha_pct']],
        color=['#2c7fb8' if '4-digit' in e else '#a6bddb' for e in orden['spec_en']],
        edgecolor='white', capsize=3)
ax.set_yticks(list(y_pos))
ax.set_yticklabels(orden['spec_en'], fontsize=8.5)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_xlabel('Adjusted gap (%) with 95% CI')
ax.set_title('The adjusted gap under alternative specifications', fontsize=12, fontweight='bold')
sns.despine(); plt.tight_layout()
plt.savefig(f'{FIG}/robustez_especificaciones_en.png', dpi=150, bbox_inches='tight')
plt.close()
print('OK Figure 3 (robustez_especificaciones_en.png)')
