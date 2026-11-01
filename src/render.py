"""HTML helpers. Numeric strings stay as published; Spanish display swaps the decimal dot."""
import html

def esc(s):
    return html.escape(str(s), quote=True)

def loc(s, lang):
    s = "" if s is None else str(s)
    return s.replace(".", ",") if lang == "es" else s

def effect(row, lang):
    metric = row["metric_es"] if lang == "es" else row["metric_en"]
    est = loc(row["est"], lang)
    p = row.get("p")
    extra = ""
    if p:
        sep = "; " 
        extra = sep + ("p = " + loc(p, lang))
    if not row.get("lo"):
        return metric + " " + est + extra
    a = "a" if lang == "es" else "to"
    ic = "IC" if lang == "es" else "CI"
    return "%s %s (%s %s %s %s)%s" % (metric, est, ic, loc(row["lo"], lang), a, loc(row["hi"], lang), extra)

def _bounds(row):
    e = float(row["est"])
    lo, hi = row.get("lo"), row.get("hi")
    if row["sign"] == "pos":
        if not lo:
            return e, None, None
        return e, float(lo), float(hi)
    if not lo:
        return -e, None, None
    a, b = float(lo), float(hi)
    return -e, -b, -a

def forest(rows, lang, aria):
    pts = [0.0]
    parsed = []
    for row in rows:
        b, lo, hi = _bounds(row)
        parsed.append((row, b, lo, hi))
        pts.append(b)
        if lo is not None:
            pts.extend([lo, hi])
    lo_ax, hi_ax = min(pts), max(pts)
    pad = (hi_ax - lo_ax) * 0.08 or 0.2
    lo_ax -= pad
    hi_ax += pad
    span = hi_ax - lo_ax
    def x(v):
        t = (v - lo_ax) / span
        return 5 + t * 90
    zero = x(0)
    bits = ['<div class="forest" role="img" aria-label="%s">' % esc(aria)]
    for row, b, lo, hi in parsed:
        label = row["es"] if lang == "es" else row["en"]
        note = row["note_es"] if lang == "es" else row["note_en"]
        crosses = lo is not None and lo <= 0 <= hi
        tone = "soft" if crosses else "solid"
        num = effect(row, lang)
        bits.append('<div class="frow">')
        bits.append('<div class="flab"><b>%s</b><span>%s</span></div>' % (esc(label), esc(note)))
        bits.append('<div class="ftrack">')
        bits.append('<i class="fzero" style="left:%.4f%%"></i>' % zero)
        if lo is not None:
            left, right = x(lo), x(hi)
            bits.append('<i class="fwh %s" style="left:%.4f%%;width:%.4f%%"></i>' % (tone, left, max(0.6, right - left)))
        bits.append('<i class="fdot %s" style="left:%.4f%%"></i>' % (tone, x(b)))
        bits.append("</div>")
        bits.append('<div class="fnum">%s</div>' % esc(num))
        bits.append("</div>")
    bits.append("</div>")
    return "\n".join(bits)

def table(headers, rows):
    th = "".join("<th>%s</th>" % esc(h) for h in headers)
    body = []
    for row in rows:
        tds = []
        for cell in row:
            if isinstance(cell, tuple):
                text, cls = cell
                tds.append('<td class="%s">%s</td>' % (esc(cls), esc(text)))
            else:
                tds.append("<td>%s</td>" % esc(cell))
        body.append("<tr>" + "".join(tds) + "</tr>")
    return '<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, "".join(body))

def dose_cards(cards):
    bits = ['<div class="dose-grid">']
    for c in cards:
        bits.append('<article class="dose"><b>%s</b><span class="big">%s</span><p>%s</p><span class="src">%s</span></article>' % (
            esc(c["kicker"]), esc(c["min"]), esc(c["text"]), esc(c["src"])))
    bits.append("</div>")
    return "\n".join(bits)

def ladder(lang):
    """Minutes on the 40 to 720 range reported by Salazar-Méndez et al. 2023. Labels are the published minute values."""
    marks = [(40, "40"), (100, "100"), (150, "150"), (200, "200"), (400, "400"), (720, "720")]
    lo, hi = 40, 720
    cap = "Minutos en el rango observado, de 40 a 720 (Salazar-Méndez et al., 2023)." if lang == "es" else "Minutes on the observed range, 40 to 720 (Salazar-Méndez et al., 2023)."
    bits = ['<div class="ladder" role="img" aria-label="%s">' % esc(cap)]
    bits.append('<div class="ladder-line"></div>')
    for minute, label in marks:
        left = (minute - lo) / (hi - lo) * 100
        bits.append('<span class="mark" style="left:%.4f%%"><i></i>%s</span>' % (left, esc(label)))
    bits.append("</div>")
    bits.append('<p class="small soft">%s</p>' % esc(cap))
    return "\n".join(bits)
