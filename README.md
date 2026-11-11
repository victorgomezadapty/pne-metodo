# Pain neuroscience education

A static page about the pain neuroscience education method: what it is, how it works, how it is done, how it is applied with exercise, what the evidence says according to the comparator, and how guidelines name it. English is the default at `/`. Spanish is the same report at `pne-es.html`. The root file does not switch language from Accept-Language or cookies.

Saudi Arabia is an annex, not the centre of the page.

## Contents

- `index.html`: English front page. It links to both editions. Spanish is one click away.
- `pne-es.html`: the page in Spanish.
- `pne-en.html`: the same page in English.
- `data/`: three derived CSVs (trial extraction, effects in long format and estimates for the charts). They do not include individual data. The dataset is published on Kaggle (https://www.kaggle.com/datasets/vctorandrsgmezlpez/pne-trials-evidence-extraction) together with the notebook (https://www.kaggle.com/code/vctorandrsgmezlpez/pne-trials-open-data-review).
- `src/`: a Python 3 generator, with no dependencies.

Each section is a tab. The menu, the index and the previous and next buttons open it, and a URL with `#section` links directly to it. Without JavaScript the full page is visible. It respects `prefers-reduced-motion`. The only external dependency is Google Fonts.

## How to rebuild

Python 3 is required, with no external packages. It runs on Windows, macOS and Linux.

```bash
cd src
python3 build.py
```

The script writes `index.html`, `pne-es.html` and `pne-en.html` in the repository root. If a template key is missing, it stops and names that key. It also checks that each DOI has a valid form and that the visible text contains neither an em dash nor a double hyphen.

- `src/template.html` with `src/es.py` and `src/en.py`: the text for each language.
- `src/facts.py`: published figures, shared by both languages.
- `src/references.py`: the 91 references in APA 7.
- `src/common.py`: palette, CSS and JavaScript.
- `src/index_template.html`: the front page.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Open `http://127.0.0.1:8000/`.

## Deployment

Static site. There is no build step on the server: the files in the root are served. There is no `vercel.json` and there are no secret variables.

## Licence

Text, tables and derived CSVs are under CC BY 4.0. Code is under MIT. Cited sources keep their rights. The O'Keeffe dataset is not redistributed: only Zenodo record 6760585 is linked. See [LICENSE.md](LICENSE.md).

## Disclaimer

Educational information drawn from published sources. It is not medical advice and it does not replace assessment by a health professional.

Author: Víctor Andrés Gómez López, sports physiotherapist.
