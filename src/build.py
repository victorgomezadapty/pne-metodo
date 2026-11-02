"""Genera el sitio estático en la raíz del repositorio. Uso: cd src && python3 build.py"""
import html, os, re, sys
from html.parser import HTMLParser
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import css, JS
from references import REFS

DOI_RE = re.compile(r"^https://doi\.org/10\.\d{4,9}/\S+$")
SECTIONS = ["what", "how", "dose", "clinic", "evidence", "new", "guides", "saudi", "data", "sources"]

def fill(T, d):
    miss = set(re.findall(r"\{\{(\w+)\}\}", T)) - set(d)
    if miss:
        raise SystemExit("faltan claves: %s" % sorted(miss))
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(d[m.group(1)]), T)

def cite_html(cite):
    s = html.escape(cite, quote=True)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    def link(m):
        url = m.group(1).rstrip(".,);")
        return '<a href="%s">%s</a>' % (html.escape(url, quote=True), html.escape(url))
    return re.sub(r"(https://[^\s<]+)", link, s)

def refs_html(D):
    labels = {"full": D["st_full"], "open_abs": D["st_oabs"], "abstract": D["st_abs"]}
    bits = []
    for r in REFS:
        linkst = D["st_doi"] if r["kind"] == "doi" else D["st_http"]
        bits.append('<li data-st="%s">%s <span class="st">%s</span> <span class="st">%s</span></li>' % (
            r["status"], cite_html(r["cite"]), html.escape(labels[r["status"]]), html.escape(linkst)))
    return "\n".join(bits)

class TextGrab(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def visible(page):
    g = TextGrab()
    g.feed(page)
    return "\n".join(g.parts)

def check(path, lang):
    page = open(path, encoding="utf-8").read()
    text = visible(page)
    for bad, name in (("\u2013", "en dash"), ("\u2014", "em dash"), ("--", "double hyphen"),
                      ("&mdash;", "mdash"), ("&ndash;", "ndash"), ("&#8211;", "num en"), ("&#8212;", "num em")):
        if bad in text or bad in page and bad.startswith("&"):
            if bad in text or (bad.startswith("&") and bad in page):
                i = text.find(bad) if bad in text else page.find(bad)
                src = text if bad in text else page
                raise SystemExit("%s: %s near %r" % (path, name, src[max(0, i-40):i+40]))
    kag = set(re.findall(r'https://www\.kaggle\.com/[^"\s<]+', page))
    if kag != {"https://www.kaggle.com/datasets/vctorandrsgmezlpez/pne-trials-evidence-extraction", "https://www.kaggle.com/code/vctorandrsgmezlpez/pne-trials-open-data-review"}:
        raise SystemExit("%s unexpected Kaggle links %s" % (path, sorted(kag)))
    if "coming soon" in text:
        raise SystemExit("%s still says coming soon" % path)
    dois = re.findall(r'href="(https://doi\.org/[^"]+)"', page)
    bad = [d for d in dois if not DOI_RE.match(d)]
    if bad:
        raise SystemExit("%s malformed DOI %s" % (path, bad[:5]))
    zen = re.findall(r'https://zenodo\.org/[^"\s<]+', page)
    if any("6760585" not in z for z in zen):
        raise SystemExit("%s unexpected zenodo link %s" % (path, zen))
    if "6760585" not in page:
        raise SystemExit("%s missing Zenodo record 6760585" % path)
    for sid in SECTIONS:
        if 'id="%s"' % sid not in page:
            raise SystemExit("%s missing section %s" % (path, sid))
    nref = page.count("<li data-st=")
    if nref != 91:
        raise SystemExit("%s has %d references" % (path, nref))
    ndoi = len(re.findall(r'<li data-st="[^"]+">.*?href="https://doi\.org/', page))
    if ndoi != 88:
        raise SystemExit("%s has %d DOI references" % (path, ndoi))
    must = ["-0,01", "200", "-2,61", "-6,84", "0,73"] if lang == "es" else ["-0.01", "200", "-2.61", "-6.84", "0.73"]
    for m in must:
        if m not in text:
            raise SystemExit("%s missing figure %s" % (path, m))
    if 'lang="%s"' % lang not in page:
        raise SystemExit("%s lang" % path)
    print(path, "ok", "dois", len(set(dois)), "refs", nref)

def main():
    counts = {}
    for r in REFS:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    if counts != {"full": 11, "open_abs": 57, "abstract": 23} or len(REFS) != 91:
        raise SystemExit("reference counts %s" % counts)
    T = open("template.html", encoding="utf-8").read()
    import importlib
    for L in ("es", "en"):
        D = importlib.import_module(L).D
        d = dict(D)
        d["css"] = css(L)
        d["js"] = JS
        d["refs"] = refs_html(D)
        d["cur_es"] = 'aria-current="page"' if L == "es" else ""
        d["cur_en"] = 'aria-current="page"' if L == "en" else ""
        page = fill(T, d)
        path = "../pne-%s.html" % L
        open(path, "w", encoding="utf-8", newline="\n").write(page)
        check(path, L)
    idx = fill(open("index_template.html", encoding="utf-8").read(), dict(css=css("es"), js=JS))
    open("../index.html", "w", encoding="utf-8", newline="\n").write(idx)
    itext = visible(idx)
    for bad in ("\u2013", "\u2014", "--"):
        if bad in itext:
            raise SystemExit("index dash %r" % bad)
    print("ok: index.html, pne-es.html, pne-en.html")

if __name__ == "__main__":
    main()
