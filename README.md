# Educación en neurociencia del dolor

Página estática sobre el método de la Pain Neuroscience Education: qué es, cómo funciona, cómo se hace, cómo se aplica con ejercicio, qué dice la evidencia según el comparador y cómo la nombran las guías. Español e inglés.

Arabia Saudí es un anexo, no el centro de la página.

## Contenido

- `index.html`: portada con los dos idiomas.
- `pne-es.html`: la página en español.
- `pne-en.html`: la misma página en inglés.
- `data/`: tres CSV derivados (extracción de ensayos, efectos en formato largo y estimadores para los gráficos). No incluyen datos individuales. El dataset de Kaggle todavía no está publicado.
- `src/`: generador en Python 3, sin dependencias.

Cada sección es una pestaña. El menú, el índice y los botones anterior y siguiente la abren, y la URL con `#seccion` enlaza directo. Sin JavaScript la página se ve completa. Respeta `prefers-reduced-motion`. La única dependencia externa es Google Fonts.

## Cómo reconstruir

Hace falta Python 3, sin paquetes externos. Funciona en Windows, macOS y Linux.

```bash
cd src
python3 build.py
```

El script escribe `index.html`, `pne-es.html` y `pne-en.html` en la raíz del repositorio. Si falta una clave de la plantilla, se detiene y la nombra. También comprueba que cada DOI tenga forma válida y que el texto visible no lleve raya ni doble guion.

- `src/template.html` con `src/es.py` y `src/en.py`: textos de cada idioma.
- `src/facts.py`: cifras publicadas, compartidas por los dos idiomas.
- `src/references.py`: las 91 referencias en APA 7.
- `src/common.py`: paleta, CSS y JavaScript.
- `src/index_template.html`: portada.

## Vista previa local

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000
```

Abrir `http://127.0.0.1:8000/`.

## Despliegue

Sitio estático. No hay paso de compilación en el servidor: se sirven los archivos de la raíz. No hay `vercel.json` ni variables secretas.

## Licencia

Textos, tablas y CSV derivados bajo CC BY 4.0. Código bajo MIT. Las fuentes citadas conservan sus derechos. El dataset de O'Keeffe no se redistribuye: solo se enlaza el registro Zenodo 6760585. Ver [LICENSE.md](LICENSE.md).

## Aviso

Información educativa a partir de fuentes publicadas. No es consejo médico ni sustituye la valoración de un profesional de la salud.

Autor: Víctor Andrés Gómez López, fisioterapeuta deportivo.
