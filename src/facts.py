"""Published estimates used by both language pages.

Strings are copied from chart-data.md, dossier.md and the derived CSVs.
The forest places the dot in the direction that favours PNE and prints the
original signed estimate beside it. sign 'pos' means the paper's positive
value favours PNE. sign 'neg' means the paper's negative value favours PNE.
"""
import csv, os
from collections import Counter
from render import forest, table, dose_cards, ladder, loc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

def _read(name):
    with open(os.path.join(DATA, name), encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows

def dataset_facts():
    trials = _read("pne_trials_extraction.csv")
    effects = _read("pne_trial_effects_long.csv")
    meta = _read("pne_meta_estimates.csv")
    if len(trials) != 23 or len(effects) != 21 or len(meta) != 42:
        raise SystemExit("unexpected derived-file row counts")
    pop = Counter(r["population_type"] for r in trials)
    primary = Counter(r["primary_result"] for r in trials)
    if dict(pop) != {"patients": 20, "students": 2, "athletes": 1}:
        raise SystemExit("unexpected population counts")
    return dict(trials=trials, effects=effects, meta=meta, pop=pop, primary=primary,
                trial_cols=list(trials[0].keys()), effect_cols=list(effects[0].keys()),
                meta_cols=list(meta[0].keys()))

PAIN = [
    dict(es="PNE frente a no PNE, corto plazo", en="PNE versus no PNE, short term",
         est="0.73", lo="-0.14", hi="1.61", sign="pos", metric_es="DMP", metric_en="MD",
         note_es="Certeza baja. Wood y Hendrick 2019. 8 ECA, n = 615.",
         note_en="Low certainty. Wood and Hendrick 2019. 8 RCTs, n = 615."),
    dict(es="PNE junto a fisioterapia, corto plazo", en="PNE with physiotherapy, short term",
         est="1.32", lo="1.08", hi="1.56", sign="pos", metric_es="DMP", metric_en="MD",
         note_es="Certeza moderada. Wood y Hendrick 2019.",
         note_en="Moderate certainty. Wood and Hendrick 2019."),
    dict(es="PNE más ejercicio frente a ejercicio", en="PNE plus exercise versus exercise",
         est="-1.14", lo="-1.55", hi="-0.72", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Certeza no indicada en el resumen. Ma et al. 2024. 17 ECA, n = 1078.",
         note_en="Certainty not stated in the abstract. Ma et al. 2024. 17 RCTs, n = 1078."),
    dict(es="PNE más fisioterapia frente a fisioterapia", en="PNE plus physiotherapy versus physiotherapy",
         est="-1.15", lo="-1.67", hi="-0.64", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Certeza no indicada en el resumen. Ma et al. 2024.",
         note_en="Certainty not stated in the abstract. Ma et al. 2024."),
    dict(es="PNE más ejercicio, revisión paraguas", en="PNE plus exercise, umbrella review",
         est="-1.11", lo="-1.57", hi="-0.66", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Certeza no indicada en el resumen. Cancela et al. 2025. 19 revisiones, 5200 participantes.",
         note_en="Certainty not stated in the abstract. Cancela et al. 2025. 19 reviews, 5200 participants."),
    dict(es="PNE más ejercicio frente a ejercicio", en="PNE plus exercise versus exercise",
         est="-2.09", lo="-3.38", hi="-0.80", sign="neg", metric_es="DMP", metric_en="MD",
         note_es="Certeza baja. Siddall et al. 2022. 5 ECA, n = 460. Dolor en escala 0 a 10.",
         note_en="Low certainty. Siddall et al. 2022. 5 RCTs, n = 460. Pain on a 0 to 10 scale."),
]

SMD = [
    dict(es="Discapacidad, PNE más ejercicio", en="Disability, PNE plus exercise",
         est="-0.68", lo="-1.17", hi="-0.20", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Certeza baja. Siddall et al. 2022.",
         note_en="Low certainty. Siddall et al. 2022."),
    dict(es="Kinesiofobia, PNE más ejercicio", en="Kinesiophobia, PNE plus exercise",
         est="-1.20", lo="-1.84", hi="-0.57", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Certeza moderada. Siddall et al. 2022.",
         note_en="Moderate certainty. Siddall et al. 2022."),
    dict(es="Dolor al terminar", en="Pain at the end of the intervention",
         est="-0.65", lo="", hi="", p="0.005", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Sin IC en el resumen. Medina-Viedma et al. 2025. 15 ECA, n = 810. Comparador mezclado.",
         note_en="No CI in the abstract. Medina-Viedma et al. 2025. 15 RCTs, n = 810. Mixed comparator."),
    dict(es="Discapacidad al terminar", en="Disability at the end",
         est="-0.6", lo="", hi="", p="0.009", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Sin IC en el resumen. Medina-Viedma et al. 2025.",
         note_en="No CI in the abstract. Medina-Viedma et al. 2025."),
    dict(es="Kinesiofobia al terminar", en="Kinesiophobia at the end",
         est="-1.12", lo="", hi="", p="< 0.001", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Sin IC en el resumen. Medina-Viedma et al. 2025.",
         note_en="No CI in the abstract. Medina-Viedma et al. 2025."),
    dict(es="Catastrofización al terminar", en="Catastrophising at the end",
         est="-0.9", lo="", hi="", p="0.016", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Sin IC en el resumen. Medina-Viedma et al. 2025.",
         note_en="No CI in the abstract. Medina-Viedma et al. 2025."),
    dict(es="Dolor, PNE en general", en="Pain, PNE overall",
         est="-0.27", lo="-0.5", hi="0.00", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="Khan et al. 2026. 12 ECA, n = 1485.",
         note_en="Khan et al. 2026. 12 RCTs, n = 1485."),
    dict(es="Discapacidad, paraguas de PNE más ejercicio", en="Disability, PNE plus exercise umbrella",
         est="-0.42", lo="-1.09", hi="0.24", sign="neg", metric_es="DME", metric_en="SMD",
         note_es="No significativa. Cancela et al. 2025.",
         note_en="Not significant. Cancela et al. 2025."),
]

WATSON = [
    dict(es="Dolor a corto plazo", en="Short-term pain",
         est="-5.91", lo="-13.75", hi="1.93", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Escala 0 a 100. Watson et al. 2019. 12 ECA, n = 755.",
         note_en="0 to 100 scale. Watson et al. 2019. 12 RCTs, n = 755."),
    dict(es="Discapacidad a corto plazo", en="Short-term disability",
         est="-4.09", lo="-7.72", hi="-0.45", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Escala 0 a 100. Watson et al. 2019.",
         note_en="0 to 100 scale. Watson et al. 2019."),
    dict(es="Kinesiofobia a corto plazo", en="Short-term kinesiophobia",
         est="-13.55", lo="-25.89", hi="-1.21", sign="neg", metric_es="DM", metric_en="MD",
         note_es="Escala 0 a 100. La fuente la señala como la única cifra clínicamente relevante de este metaanálisis.",
         note_en="0 to 100 scale. The source marks it as the only clinically relevant figure in this meta-analysis."),
]

MED_PAIN = [
    dict(es="Creencias sobre las consecuencias del dolor de espalda", en="Beliefs about the consequences of back pain",
         est="-0.96", lo="-1.47", hi="-0.64", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023. RESOLVE, n = 276.",
         note_en="Cashin et al. 2023. RESOLVE, n = 276."),
    dict(es="Catastrofización", en="Catastrophising",
         est="-0.49", lo="-0.61", hi="-0.24", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023.",
         note_en="Cashin et al. 2023."),
    dict(es="Autoeficacia ante el dolor", en="Pain self-efficacy",
         est="-0.37", lo="-0.66", hi="-0.22", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023.",
         note_en="Cashin et al. 2023."),
]

MED_DIS = [
    dict(es="Creencias sobre las consecuencias del dolor de espalda", en="Beliefs about the consequences of back pain",
         est="-1.66", lo="-2.62", hi="-0.87", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023. RESOLVE, n = 276.",
         note_en="Cashin et al. 2023. RESOLVE, n = 276."),
    dict(es="Catastrofización", en="Catastrophising",
         est="-1.06", lo="-1.79", hi="-0.53", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023.",
         note_en="Cashin et al. 2023."),
    dict(es="Autoeficacia ante el dolor", en="Pain self-efficacy",
         est="-0.84", lo="-1.89", hi="-0.45", sign="neg", metric_es="efecto mediado", metric_en="mediated effect",
         note_es="Cashin et al. 2023.",
         note_en="Cashin et al. 2023."),
]

def charts(lang):
    pain_aria = "Dolor en escala 0 a 10. El punto muestra la dirección a favor de la PNE. El número es el estimador publicado." if lang == "es" else "Pain on a 0 to 10 scale. The dot shows the direction that favours PNE. The number is the published estimate."
    smd_aria = "Diferencias de medias estandarizadas. El punto muestra la dirección a favor de la PNE." if lang == "es" else "Standardised mean differences. The dot shows the direction that favours PNE."
    wat_aria = "Diferencias en escala 0 a 100. Watson et al. 2019." if lang == "es" else "Differences on a 0 to 100 scale. Watson et al. 2019."
    mp_aria = "Efectos mediados sobre el dolor en RESOLVE." if lang == "es" else "Mediated effects on pain in RESOLVE."
    md_aria = "Efectos mediados sobre la discapacidad en RESOLVE." if lang == "es" else "Mediated effects on disability in RESOLVE."
    return dict(
        pain=forest(PAIN, lang, pain_aria),
        smd=forest(SMD, lang, smd_aria),
        watson=forest(WATSON, lang, wat_aria),
        med_pain=forest(MED_PAIN, lang, mp_aria),
        med_dis=forest(MED_DIS, lang, md_aria),
        ladder=ladder(lang),
        dose=dose_cards(_dose(lang)),
        ma=table(_ma_headers(lang), _ma_rows(lang)),
        nulls=table(_null_headers(lang), _null_rows(lang)),
        guides=table(_guide_headers(lang), _guide_rows(lang)),
        t22=table(_t22_headers(lang), _t22_rows(lang)),
        paths=table(_path_headers(lang), _path_rows(lang)),
        more=table(_more_headers(lang), _more_rows(lang)),
        measures=table(_measure_headers(lang), _measure_rows(lang)),
    )

def _dose(lang):
    if lang == "es":
        return [
            dict(kicker="Kinesiofobia", min="100 min", text="DM -8,53. Supera la MCID. Sin IC en la fuente.", src="Salazar-Méndez et al. 2023"),
            dict(kicker="Discapacidad", min="150 min", text="Estimación -6,84 (IC -7,98 a -5,70), añadida al ejercicio. Supera la MCID.", src="Núñez-Cortés et al. 2024, Pain"),
            dict(kicker="Dolor", min="200 min", text="Estimación -2,61 (IC -3,12 a -2,10), añadida al ejercicio. Supera la MCID.", src="Núñez-Cortés et al. 2024, Pain"),
            dict(kicker="Ansiedad", min="200 min", text="DM -1,88. Supera la MCID. Sin IC en la fuente.", src="Salazar-Méndez et al. 2023"),
            dict(kicker="Catastrofización", min="400 min", text="DM -7,17. Supera la MCID. Sin IC en la fuente.", src="Salazar-Méndez et al. 2023"),
        ]
    return [
        dict(kicker="Kinesiophobia", min="100 min", text="MD -8.53. Exceeds the MCID. No CI in the source.", src="Salazar-Méndez et al. 2023"),
        dict(kicker="Disability", min="150 min", text="Estimate -6.84 (CI -7.98 to -5.70), added to exercise. Exceeds the MCID.", src="Núñez-Cortés et al. 2024, Pain"),
        dict(kicker="Pain", min="200 min", text="Estimate -2.61 (CI -3.12 to -2.10), added to exercise. Exceeds the MCID.", src="Núñez-Cortés et al. 2024, Pain"),
        dict(kicker="Anxiety", min="200 min", text="MD -1.88. Exceeds the MCID. No CI in the source.", src="Salazar-Méndez et al. 2023"),
        dict(kicker="Catastrophising", min="400 min", text="MD -7.17. Exceeds the MCID. No CI in the source.", src="Salazar-Méndez et al. 2023"),
    ]

def _ma_headers(lang):
    return ["Subgrupo", "DM en dolor"] if lang == "es" else ["Subgroup", "Pain MD"]

def _ma_rows(lang):
    rows = [
        ("Sesión única de más de 60 min" if lang == "es" else "Single session longer than 60 min", "-2.04"),
        ("Formato grupal" if lang == "es" else "Group format", "-1.76"),
        ("4 a 8 sesiones" if lang == "es" else "4 to 8 sessions", "-1.34"),
        ("7 a 12 semanas" if lang == "es" else "7 to 12 weeks", "-1.32"),
    ]
    out = []
    for a, b in rows:
        out.append([a, loc(b, lang)])
    return out

def _null_headers(lang):
    if lang == "es":
        return ["Ensayo", "n", "Resultado primario", "P"]
    return ["Trial", "n", "Primary result", "P"]

def _null_rows(lang):
    es = lang == "es"
    return [
        ["PREVENT, Traeger et al. 2019. Dolor lumbar agudo de alto riesgo. Educación placebo." if es else "PREVENT, Traeger et al. 2019. High-risk acute low back pain. Placebo education.",
         "202",
         "Dolor a los 3 meses, DM -0,3 (IC -1,0 a 0,3)." if es else "Pain at 3 months, MD -0.3 (CI -1.0 to 0.3).",
         "n. s." if es else "n.s."],
        ["Chimenti et al. 2023. Tendinopatía aquílea. Ambos grupos con ejercicio. Educación patoanatómica." if es else "Chimenti et al. 2023. Achilles tendinopathy. Both groups exercised. Pathoanatomical education.",
         "66",
         "Sin diferencia en el dolor evocado por el movimiento." if es else "No difference in movement-evoked pain.",
         ""],
        ["Dams et al. 2023. Tras cirugía de cáncer de mama. Educación biomédica." if es else "Dams et al. 2023. After breast cancer surgery. Biomedical education.",
         "184",
         "-1,31 (IC -5,28 a 2,65) en el cambio del Pain Disability Index." if es else "-1.31 (CI -5.28 to 2.65) on change in the Pain Disability Index.",
         "0,516" if es else "0.516"],
        ["Larsen et al. 2024. Dolor crónico tras artroplastia de rodilla. Ejercicio más PNE frente a PNE sola." if es else "Larsen et al. 2024. Chronic pain after knee arthroplasty. Exercise plus PNE versus PNE alone.",
         "69",
         "KOOS4, DM -1,33 (IC -7,59 a 4,92)." if es else "KOOS4, MD -1.33 (CI -7.59 to 4.92).",
         "0,68" if es else "0.68"],
        ["Baas et al. 2024. Artroplastia de rodilla. Atención habitual. El resumen no indica la dirección del signo." if es else "Baas et al. 2024. Knee arthroplasty. Usual care. The abstract does not state the sign direction.",
         "68",
         "WOMAC dolor 0,4 (IC -1,7 a 2,4)." if es else "WOMAC pain 0.4 (CI -1.7 to 2.4).",
         "n. s." if es else "n.s."],
        ["Adenis et al. 2024 y 2026. Lumbalgia en rehabilitación multidisciplinar. Educación en fisiología espinal y ergonomía." if es else "Adenis et al. 2024 and 2026. Low back pain in multidisciplinary rehabilitation. Spinal physiology and ergonomics education.",
         "88; 74 a 12 meses" if es else "88; 74 at 12 months",
         "Discapacidad al final -1,7 (IC -4,0 a 0,5). A 12 meses -1,04 (IC -3,14 a 1,06)." if es else "Disability at the end -1.7 (CI -4.0 to 0.5). At 12 months -1.04 (CI -3.14 to 1.06).",
         "0,12; 0,33" if es else "0.12; 0.33"],
        ["Malfliet et al. 2025. Latigazo cervical crónico. Fisioterapia con educación biomédica. Diferencia positiva a favor del paquete con PNE." if es else "Malfliet et al. 2025. Chronic whiplash. Physiotherapy with biomedical education. Positive difference favours the PNE package.",
         "120",
         "NDI a 6 meses, DM 2,38 (IC -0,12 a 4,89)." if es else "NDI at 6 months, MD 2.38 (CI -0.12 to 4.89).",
         "0,15" if es else "0.15"],
    ]

def _guide_headers(lang):
    if lang == "es":
        return ["Guía", "Qué dice de la PNE", "Fuerza", "Código propuesto"]
    return ["Guideline", "What it says about PNE", "Strength", "Proposed code"]

def _guide_rows(lang):
    es = lang == "es"
    return [
        ["JOSPT 2021, George et al.",
         "Dar PNE junto a ejercicio o terapia manual en dolor lumbar crónico. Usar tratamientos activos en vez de educación aislada." if es else "Provide PNE with exercise or manual therapy for chronic low back pain. Use active treatment rather than stand-alone education.",
         "Grado A" if es else "Grade A",
         "4"],
        ["OMS 2023",
         "Educación o consejo estructurados y estandarizados como parte de la atención. No nombra la PNE como recomendación propia. En 7 de 15 ensayos de la evidencia había contenido de neurociencia del dolor." if es else "Structured, standardised education or advice as part of care. It does not name PNE as its own recommendation. Pain neuroscience content was present in 7 of 15 trials in the evidence.",
         "Condicional a favor, certeza muy baja" if es else "Conditional for, very low certainty",
         "2"],
        ["KNGF 2021",
         "Overweeg (considerar) educación en dolor, además de la información, en el perfil 3, por ejemplo con miedo al movimiento irreal o catastrofización. Evitar lesión, degeneración y desgaste." if es else "Overweeg (consider) pain education, in addition to information, for profile 3, for example with unrealistic fear of movement or catastrophising. Avoid injury, degeneration and wear.",
         "Débil: considerar" if es else "Weak: consider",
         "1"],
        ["NICE NG59, 2016, actualizada en julio de 2026" if es else "NICE NG59, 2016, updated July 2026",
         "No nombra la PNE. La recomendación 1.2.1, vigente, pide informar sobre la naturaleza del dolor lumbar como parte del autocuidado. En julio de 2026 se retiraron las recomendaciones de terapia psicológica y de programas físicos y psicológicos combinados." if es else "Does not name PNE. Recommendation 1.2.1, still in force, asks clinicians to give information on the nature of low back pain as part of self-management. In July 2026 the recommendations on psychological therapy and on combined physical and psychological programmes were withdrawn.",
         "Sin recomendación de PNE" if es else "No PNE recommendation",
         "0"],
        ["Arabia Saudí 2026, Aldera et al." if es else "Saudi Arabia 2026, Aldera et al.",
         "Sugiere usar PNE en dolor lumbar crónico inespecífico y priorizarla cuando el riesgo de discapacidad y cronicidad es mayor." if es else "Suggests using PNE for chronic non-specific low back pain and prioritising it when the risk of disability and chronicity is higher.",
         "Condicional a favor, certeza baja" if es else "Conditional for, low certainty",
         "2"],
    ]

def _t22_headers(lang):
    if lang == "es":
        return ["Resultado", "Momento", "DM (IC)", "Certeza"]
    return ["Outcome", "Time", "MD (CI)", "Certainty"]

def _t22_rows(lang):
    es = lang == "es"
    ic = "IC" if es else "CI"
    def dm(est, lo, hi):
        a = "a" if es else "to"
        return "DM %s (%s %s %s %s)" % (loc(est, lang), ic, loc(lo, lang), a, loc(hi, lang))
    return [
        ["RMDQ, PNE frente a no PNE" if es else "RMDQ, PNE versus no PNE",
         "32,8 días" if es else "32.8 days", dm("2.28", "0.30", "4.25"),
         "Moderada" if es else "Moderate"],
        ["NRS, PNE frente a no PNE" if es else "NRS, PNE versus no PNE",
         "Corto plazo" if es else "Short term", dm("0.73", "-0.14", "1.61"),
         "Baja" if es else "Low"],
        ["NRS, PNE frente a no PNE" if es else "NRS, PNE versus no PNE",
         "12 meses" if es else "12 months", dm("0.44", "-1.03", "1.91"),
         "Baja" if es else "Low"],
        ["TSK, PNE frente a no PNE" if es else "TSK, PNE versus no PNE",
         "3,3 semanas" if es else "3.3 weeks", dm("4.72", "2.32", "7.13"),
         "Baja. Etiquetado como poco o ningún efecto, aunque el IC excluye el 0." if es else "Low. Labelled little or no effect, although the CI excludes 0."],
        ["RMDQ, PNE frente a no PNE" if es else "RMDQ, PNE versus no PNE",
         "12 meses" if es else "12 months", dm("2.18", "-0.67", "5.02"),
         "Baja" if es else "Low"],
        ["RMDQ, PNE más fisioterapia" if es else "RMDQ, PNE plus physiotherapy",
         "40 días" if es else "40 days", dm("3.94", "3.37", "4.52"),
         "Moderada" if es else "Moderate"],
        ["NRS, PNE más fisioterapia" if es else "NRS, PNE plus physiotherapy",
         "32,6 días" if es else "32.6 days", dm("1.32", "1.08", "1.56"),
         "Moderada" if es else "Moderate"],
    ]

def _path_headers(lang):
    if lang == "es":
        return ["Trayectoria", "Fisioterapia sola (n = 46)", "Fisioterapia más educación (n = 46)"]
    return ["Trajectory", "Physiotherapy alone (n = 46)", "Physiotherapy plus education (n = 46)"]

def _path_rows(lang):
    es = lang == "es"
    return [
        ["Recuperación mínima" if es else "Minimal recovery", "28 (61%)", "12 (26%)"],
        ["Recuperación psicosocial dominante" if es else "Psychosocial-dominant recovery", "18 (39%)", "8 (17%)"],
        ["Recuperación global" if es else "Global recovery", "0 (0%)", "26 (57%)"],
    ]

def _more_headers(lang):
    if lang == "es":
        return ["Fuente", "Resultado", "Cifra publicada"]
    return ["Source", "Outcome", "Published figure"]

def _more_rows(lang):
    es = lang == "es"
    rows = [
        ("Wood y Hendrick 2019" if es else "Wood and Hendrick 2019",
         "Discapacidad. La fuente no nombra la escala de este 0,42." if es else "Disability. The source does not name the scale of this 0.42.",
         "0,42 (IC 0,28 a 0,56). Junto a fisioterapia: 3,94 (IC 3,37 a 4,52). Sin efecto a largo plazo." if es else "0.42 (CI 0.28 to 0.56). With physiotherapy: 3.94 (CI 3.37 to 4.52). No long-term effect."),
        ("Tegner et al. 2018",
         "7 ECA" if es else "7 RCTs",
         "Dolor: DMP -1,03 al terminar y -1,09 a los 3 meses. Discapacidad: DME -0,47 y -0,38. TSK no significativa. Sin IC en la fuente." if es else "Pain: MD -1.03 at the end and -1.09 at 3 months. Disability: SMD -0.47 and -0.38. TSK not significant. No CI in the source."),
        ("Ma et al. 2024",
         "Discapacidad. 17 ECA, n = 1078." if es else "Disability. 17 RCTs, n = 1078.",
         "PNE más ejercicio: DME -0,80 (IC -1,13 a -0,47). PNE más fisioterapia: DME -0,85. El segundo valor no trae IC en la fuente." if es else "PNE plus exercise: SMD -0.80 (CI -1.13 to -0.47). PNE plus physiotherapy: SMD -0.85. The second value has no CI in the source."),
        ("Medina-Viedma et al. 2025",
         "A los 3 meses. Comparador mezclado." if es else "At 3 months. Mixed comparator.",
         "Dolor DME -1,0. Discapacidad -0,84. Kinesiofobia -1,57. Sin IC en la fuente." if es else "Pain SMD -1.0. Disability -0.84. Kinesiophobia -1.57. No CI in the source."),
        ("Siddall et al. 2022",
         "Catastrofización" if es else "Catastrophising",
         "-7,72. Sin IC en la fuente." if es else "-7.72. No CI in the source."),
        ("Bonatesta et al. 2022",
         "Dolor. 8 ECA, 5 en el metaanálisis." if es else "Pain. 8 RCTs, 5 in the meta-analysis.",
         "DME -0,53 a corto plazo y -0,57 a medio plazo. Certeza baja a muy baja. Sin IC en la fuente." if es else "SMD -0.53 in the short term and -0.57 in the medium term. Low to very low certainty. No CI in the source."),
        ("Khan et al. 2026",
         "Sueño y variables psicosociales" if es else "Sleep and psychosocial variables",
         "Tiempo total de sueño 0,42. La fuente no nombra la métrica. Sin efecto en las variables psicosociales." if es else "Total sleep time 0.42. The source does not name the metric. No effect on the psychosocial variables."),
        ("Tatikola et al. 2025, PNE+",
         "20 estudios en el metaanálisis" if es else "20 studies in the meta-analysis",
         "EVA DME -0,70. NPRS -1,71. TSK -5,29. PCS -3,82. Sin IC en la fuente." if es else "VAS SMD -0.70. NPRS -1.71. TSK -5.29. PCS -3.82. No CI in the source."),
        ("Lin et al. 2024",
         "Cuello. 7 ECA, n = 479." if es else "Neck. 7 RCTs, n = 479.",
         "Dolor g -0,730 (IC -1,340 a -0,119), I² 89%. Kinesiofobia g -0,444. Eficaz en adultos y no en adolescentes." if es else "Pain g -0.730 (CI -1.340 to -0.119), I² 89%. Kinesiophobia g -0.444. Effective in adults and not in adolescents."),
        ("Saracoglu et al. 2022",
         "Fibromialgia. 4 estudios, n = 612." if es else "Fibromyalgia. 4 studies, n = 612.",
         "FIQ DME -1,051. Dolor -1,049." if es else "FIQ SMD -1.051. Pain -1.049."),
        ("Suso-Martí et al. 2022",
         "Fibromialgia. 8 estudios." if es else "Fibromyalgia. 8 studies.",
         "Dolor DME -0,76 (IC -1,33 a -0,19), I² 92%, calidad baja. Sin efecto en catastrofización ni en ansiedad." if es else "Pain SMD -0.76 (CI -1.33 to -0.19), I² 92%, low quality. No effect on catastrophising or anxiety."),
        ("Lesmond et al. 2024",
         "Artrosis de rodilla. 7 estudios." if es else "Knee osteoarthritis. 7 studies.",
         "Dolor DM -0,49 (IC -0,66 a -0,32). Catastrofización -1,81, sin IC en la fuente." if es else "Pain MD -0.49 (CI -0.66 to -0.32). Catastrophising -1.81, no CI in the source."),
        ("Sidiq et al. 2024",
         "Lumbalgia crónica, India. n = 92, 6 semanas. Registro retrospectivo." if es else "Chronic low back pain, India. n = 92, 6 weeks. Retrospective registration.",
         "Discapacidad DM 8,2 (d = 0,75). Dolor DM 3,5 (d = 0,82). Efectos mucho mayores que los de los metaanálisis." if es else "Disability MD 8.2 (d = 0.75). Pain MD 3.5 (d = 0.82). Effects much larger than those of the meta-analyses."),
    ]
    return [list(r) for r in rows]

def _measure_headers(lang):
    if lang == "es":
        return ["Instrumento", "Qué mide", "Datos publicados", "Versión en árabe"]
    return ["Instrument", "What it measures", "Published data", "Arabic version"]

def _measure_rows(lang):
    es = lang == "es"
    return [
        ["NPQ y rNPQ",
         "Conocimiento de la neurofisiología del dolor" if es else "Knowledge of pain neurophysiology",
         "Catley et al. 2013: análisis Rasch, n = 300, 7 ítems problemáticos. De ahí sale el rNPQ." if es else "Catley et al. 2013: Rasch analysis, n = 300, 7 problematic items. That is the source of the rNPQ.",
         "En esta búsqueda no apareció una validación árabe. Alhowimel et al. 2021 usaron el rNPQ con fisioterapeutas saudíes." if es else "No Arabic validation turned up in this search. Alhowimel et al. 2021 used the rNPQ with Saudi physiotherapists."],
        ["COPI-Adult",
         "Concepto de dolor" if es else "Concept of pain",
         "Pate et al. 2022: n = 627, 13 ítems, α = 0,78, CCI 0,84 (0,71 a 0,91)." if es else "Pate et al. 2022: n = 627, 13 items, α = 0.78, ICC 0.84 (0.71 to 0.91).",
         "En esta búsqueda no apareció una validación árabe." if es else "No Arabic validation turned up in this search."],
        ["TSK",
         "Kinesiofobia" if es else "Kinesiophobia",
         "Las fuentes de esta página no traen una cifra psicométrica de la escala genérica." if es else "The sources used for this page do not report a psychometric figure for the generic scale.",
         "TSK-AV-11, validada en Jordania (Al-Shudifat et al. 2020): n = 101, 2 factores que explican el 46,54% de la varianza." if es else "TSK-AV-11, validated in Jordan (Al-Shudifat et al. 2020): n = 101, 2 factors explaining 46.54% of the variance."],
        ["PCS",
         "Catastrofización" if es else "Catastrophising",
         "Las fuentes de esta página no traen una cifra psicométrica de la escala genérica." if es else "The sources used for this page do not report a psychometric figure for the generic scale.",
         "Versión árabe (Terkawi et al. 2017): n = 113, α = 0,94, CCI 0,83." if es else "Arabic version (Terkawi et al. 2017): n = 113, α = 0.94, ICC 0.83."],
        ["CSI",
         "Síntomas de sensibilización central" if es else "Central sensitisation symptoms",
         "Las fuentes de esta página no traen una cifra psicométrica de la escala genérica." if es else "The sources used for this page do not report a psychometric figure for the generic scale.",
         "Versión saudí (Tamboosi et al. 2024): n = 264 más 56 controles, α = 0,919, CCI 0,874. Otra versión árabe (Madi et al. 2022): α = 0,88, CCI 0,94, MDC95 9,57." if es else "Saudi version (Tamboosi et al. 2024): n = 264 plus 56 controls, α = 0.919, ICC 0.874. Another Arabic version (Madi et al. 2022): α = 0.88, ICC 0.94, MDC95 9.57."],
    ]

def legend(lang):
    if lang == "es":
        return "El punto se dibuja en la dirección que favorece a la PNE, para poder leer en un mismo eje trabajos que publican el signo al revés. El número de la derecha es el estimador original, con el signo de cada artículo. Barra cian: el IC queda del lado que favorece a la PNE. Barra cobre: el IC incluye el 0. Punto sin barra: la fuente no trae IC."
    return "The dot is drawn in the direction that favours PNE, so papers that publish the opposite sign can be read on one axis. The number on the right is the original estimate, with each paper's own sign. Cyan bar: the CI lies on the side that favours PNE. Copper bar: the CI includes 0. Dot without a bar: the source gives no CI."
