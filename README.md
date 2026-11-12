# Seguiments de «La ciutat avui» · bcndades.cat

Aquest repositori té **un sol fitxer de dades**, `seguiments.json`, amb tots els seguiments de la secció
[La ciutat avui](https://bcndades.cat/la-ciutat-avui/) de BCN.DADES (aldarulls, acampada per l'habitatge, vaga de l'11-N…).

- Cada matí una tasca programada recull les novetats i actualitza aquest fitxer.
- El web el llegeix cada hora (`raw.githubusercontent.com/sudogat/bcndades-seguiments/main/seguiments.json`)
  i actualitza la pàgina de cada seguiment: `bcndades.cat/la-ciutat-avui/<slug>/`. No es crea cap entrada nova.
- Abans de pujar-lo: `python3 valida.py`.

## Format (`versio: 1`)

```jsonc
{
  "versio": 1,
  "actualitzat": "2026-10-31T08:45:00+01:00",
  "seguiments": [{
    "slug": "aldarulls-placa-catalunya",      // no el canviïs mai: és l'adreça de la pàgina
    "titol": "Aldarulls a plaça Catalunya",
    "kicker": "Seguiment · aldarulls",
    "estat": "obert",                          // "tancat" quan s'acaba
    "inici": "2026-10-24",
    "resum": "Una o dues frases (meta descripció i targetes).",
    "context": "<p>HTML del primer dia. Només s'usa quan es crea el seguiment.</p>",
    "ara": [ { "etiqueta": "Detinguts", "valor": "133", "detall": "85 menors i 48 adults",
               "font": { "nom": "Mossos al Parlament, 28/10", "url": "https://…" } } ],   // fins a 8 xifres clau
    "xifres": { "Detinguts": [ { "data": "2026-10-24", "valor": 100, "nota": "primer balanç" } ] }, // com canvia cada xifra oficial
    "grafics": [ { "titol": "…", "unitat": "", "nota": "…", "fonts": [ { "nom": "…", "url": "…" } ],
                   "punts": [ { "etiqueta": "24 d’octubre", "valor": 133, "serie": "Detinguts", "nota": "" } ] } ],   // fins a 6 gràfics de 12 barres
    "punts": [ { "lat": 41.3870, "lon": 2.1700, "data": "2026-11-11", "lloc": "Plaça de Catalunya",
                 "tipus": ["foc", "barricades", "policia"], "text": "Què hi va passar, en una frase.",
                 "font": { "nom": "Ara", "url": "https://…" } } ],   // tema 1.66.0: mapa «On ha passat» (fins a 300 punts)
    "fons": ["delictes"],                      // gràfics del web: "desnonaments", "lloguer", "delictes"
    "imatges": [ { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/…/1280px-….jpg",
                   "pagina": "https://commons.wikimedia.org/wiki/File:…", "autor": "…", "llicencia": "CC BY-SA 4.0",
                   "llicencia_url": "https://creativecommons.org/licenses/by-sa/4.0", "descripcio": "… Imatge d’arxiu", "any": "2011" } ],
    "bulos": [ { "data": "2026-10-29", "afirmacio": "…", "cert": "…", "verificador": "Maldita.es", "url": "https://…", "tema": "Aldarulls" } ],
    "dies": [ {
      "data": "2026-10-30",                    // un per dia; el mateix dia es pot corregir
      "titol": "Aldarulls a plaça Catalunya: actualització del 30 d’octubre",
      "resum": "La frase més important del dia.",
      "seccions": [
        { "titol": "Què hi ha de nou", "items": ["Fet confirmat (<a href=\"https://…\">Font</a>)."], "text": "" },
        { "titol": "Balanç oficial", "items": ["…"] },
        { "titol": "Seguiment judicial", "items": ["…"] },
        { "titol": "Què no se sap encara", "items": ["…"] },
        { "titol": "Bulos", "text": "…" }
      ],
      "fonts": [ { "nom": "betevé: …", "url": "https://…" } ]
    } ],
    "fonts_context": [ { "nom": "…", "url": "…" } ],
    "substitueix": { "principal": "slug-de-l-entrada-antiga", "prefix": "Títol de les entrades antigues: actualització" }
  }],
  "calendari": [ { "data": "2026-11-11", "titol": "Vaga general", "text": "…", "font": { "nom": "…", "url": "…" } } ],
  "bulos": []
}
```

Regles:

- **Mai no esborris dies antics**: afegeix el dia nou al final de `dies`. El web tampoc no n'esborra cap.
- La primera secció del dia es diu «Què hi ha de nou»; les altres (balanç, judicial, què no se sap) es mostren a «Com està ara».
- Dins dels textos només s'accepten `<a href>`, `<strong>`, `<em>`, `<b>` i `<i>`.
- Imatges: només de Wikimedia Commons amb llicència lliure, autor i llicència. Si és d'arxiu, digues-ho a la descripció.
- Mai noms, cares, edats concretes ni l'origen de persones detingudes o investigades: només xifres agregades.

Si alguna cosa surt malament, a WordPress: **Eines → Seguiments** (amagar un dia, tancar un seguiment, pujar el fitxer a mà).

## Mapa de punts (tema 1.66.0)

- `punts` és opcional. Cada punt necessita `lat`, `lon` (dins de Barcelona) i `lloc`. `data` (AAAA-MM-DD) fa que cada dia surti d'un color i es pugui filtrar.
- `tipus` accepta: `foc`, `aparadors`, `saqueig`, `barricades`, `policia`, `concentracio`, `tall`, `altre`. Sense cap tipus, el punt surt buit (pas de manifestants sense incidents).
- Ubicacions per tram de carrer, mai adreces de particulars. Les mateixes normes de sempre: només llocs que citin fonts oficials o dos mitjans.
- Si un fitxer porta `punts`, substitueix els que hi havia. Per afegir-ne, envia la llista sencera.

## Fitxers més antics

Des del tema 1.66.0, si arriba un fitxer amb un `actualitzat` més antic que el que ja té el web, només s'hi afegeixen els dies que falten: no torna enrere les xifres, el resum ni els gràfics.
