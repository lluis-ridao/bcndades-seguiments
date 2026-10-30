#!/usr/bin/env python3
"""Comprova seguiments.json abans de pujar-lo. Ús: python3 valida.py [seguiments.json]"""
import json, re, sys
f = sys.argv[1] if len(sys.argv) > 1 else 'seguiments.json'
d = json.load(open(f, encoding='utf-8'))
err = []
D = re.compile(r'^\d{4}-\d{2}-\d{2}$')
if d.get('versio') != 1: err.append('«versio» ha de ser 1')
if not isinstance(d.get('seguiments'), list) or not d['seguiments']: err.append('falta «seguiments»')
for s in d.get('seguiments', []):
    n = s.get('slug', '?')
    for k in ('slug', 'titol', 'kicker', 'estat', 'resum'):
        if not s.get(k): err.append(f'{n}: falta «{k}»')
    if s.get('estat') not in ('obert', 'tancat'): err.append(f'{n}: «estat» ha de ser obert o tancat')
    dates = [x.get('data', '') for x in s.get('dies', [])]
    if len(dates) != len(set(dates)): err.append(f'{n}: hi ha dies repetits')
    for x in s.get('dies', []):
        if not D.match(x.get('data', '')): err.append(f'{n}: data incorrecta {x.get("data")}')
        if not x.get('resum'): err.append(f'{n} {x.get("data")}: falta «resum»')
        for sec in x.get('seccions', []):
            for it in sec.get('items', []):
                if re.search(r'<(?!/?(a|strong|em|b|i)\b)', it): err.append(f'{n} {x["data"]}: etiqueta HTML no permesa: {it[:60]}')
    for i in s.get('imatges', []):
        if not re.match(r'^https://(upload|thumb)\.wikimedia\.org/wikipedia/commons/', i.get('url', '')): err.append(f'{n}: imatge que no és de Wikimedia Commons')
        if not i.get('autor') or not i.get('llicencia'): err.append(f'{n}: imatge sense autor o llicència')
    for lab, pts in s.get('xifres', {}).items():
        for p in pts:
            if not D.match(p.get('data', '')) or not isinstance(p.get('valor'), (int, float)): err.append(f'{n}: punt incorrecte a «{lab}»')
for e in d.get('calendari', []):
    if not D.match(e.get('data', '')): err.append(f'calendari: data incorrecta {e}')
print('\n'.join(err) if err else 'OK: ' + ', '.join(f"{s['slug']} ({len(s.get('dies', []))} dies)" for s in d['seguiments']))
sys.exit(1 if err else 0)
