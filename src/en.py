# -*- coding: utf-8 -*-
from facts import charts, legend, dataset_facts
from render import esc

C = charts("en")
L = legend("en")
F = dataset_facts()

def chips(cols):
    return '<div class="cols">' + "".join("<code>%s</code>" % esc(c) for c in cols) + "</div>"

def what():
    return """
<p class="lead">Pain neuroscience education (PNE) is an educational intervention. It aims to change the concept of pain: from a marker of damage to a signal of the perceived need to protect tissue.</p>
<h3>Definition</h3>
<p>Moseley and Butler (2015) call it Explaining Pain. It uses conceptual-change strategies. The authors are clear that it is not behavioural or cognitive advice, and that it does not deny nociception. In that paper it increases knowledge, reduces catastrophising, and comes with short-term reductions in pain and disability.</p>
<p>The literature uses equivalent names: pain neuroscience education (PNE), therapeutic neuroscience education, pain science education (PSE), pain neurophysiology education and Explaining Pain. Reviews use them interchangeably. Bonatesta et al. (2022) and Núñez-Cortés et al. (2024) say PSE.</p>
<h3>Origin</h3>
<p>The first reference randomised trial is Moseley et al. (2004, The Clinical Journal of Pain), in chronic low back pain. Education changed attitudes (SOPA(R)), catastrophising (PCS), straight leg raise and forward flexion. The change in the RMDQ was small. The authors concluded that education alone was insufficient. The abstract gives no n, no sessions, no minutes and no number for the RMDQ.</p>
<p>The same year, Moseley (2004, European Journal of Pain) analysed 121 patients. Cognitive change correlated with physical change: r = 0.88 with straight leg raise and r = 0.79 with forward flexion.</p>
<p>The founding reviews are Louw et al. (2011), 8 studies and n = 401, a narrative synthesis, and Louw et al. (2016), 13 RCTs. In the sources used here, those two reviews do not provide a pooled effect this page can cite.</p>
<h3>Where it sits</h3>
<div class="grid-2">
 <div class="card"><span class="tag">Model</span><h3>Biopsychosocial</h3><p>PNE is an educational tool inside the biopsychosocial model. It is not the whole model.</p></div>
 <div class="card"><span class="tag coral">Not PNE</span><h3>Cognitive functional therapy</h3><p>CFT (O'Sullivan et al., 2018) is an integrated behavioural approach: making sense of pain, exposure with control, and lifestyle change. It includes a reconceptualisation close to PNE and joins it to exposure and behaviour change. That integration is what the data on PNE alone leave open.</p></div>
</div>
<p>The RESTORE trial (Kent et al., 2023, Lancet, n = 492) tested CFT, not stand-alone PNE. At 13 weeks the RMDQ was MD -4.6 (CI -5.9 to -3.4) with CFT and MD -4.6 (CI -5.8 to -3.3) with CFT plus biofeedback. The effect held at 52 weeks. The social saving was about AU$5,276 per person. Thiveos et al. (2024), 7 RCTs, report low to moderate certainty for pain and disability and high certainty for self-efficacy. The source does not give the effect size of that meta-analysis.</p>
<p>Louw et al. (2021, JOSPT) place PNE as an adjunct to exercise and movement for the patient, and as a central focus of clinician training. Nijs et al. (2020) propose integrating it with motivational interviewing. That paper is a practical guide, with no efficacy data, and the authors ask for trials.</p>
"""

def how():
    return """
<p class="lead">The theory is a chain: perceived threat falls, catastrophising and fear of movement fall, activity and exposure rise, and pain and disability fall with them. Mediation analyses test that chain.</p>
<h3>RESOLVE: what mediated</h3>
<p>Cashin et al. (2023) mediated the RESOLVE trial (Bagg et al., 2022): 276 adults with chronic low back pain, education plus graded sensorimotor retraining versus sham. Four of 7 variables mediated pain and 5 of 7 mediated disability. Together they explained most of the effect. The abstract does not name the ones that dropped out.</p>
<p class="small soft">%s</p>
<h3>On pain</h3>
%s
<h3>On disability</h3>
%s
<p>In RESOLVE itself, pain at 18 weeks was -1.0 (CI -1.5 to -0.4) versus sham, with 12 weekly sessions (Bagg et al., 2022). Venter et al. (2026) found no clear effect modifiers. Self-perception of the back was a possible modifier (β 0.18).</p>
<h3>PREVENT: acute pain</h3>
<p>Cashin et al. (2022) mediated PREVENT (Traeger et al., 2019, JAMA Neurology, n = 202): 2 hours of education versus placebo education in high-risk acute low back pain. Catastrophising mediated, -0.64 (CI -1.31 to -0.15), as did back beliefs, -0.51. Self-efficacy did not. To gain 2 RMDQ points, the MCID in that analysis, it would take 8 PSEQ points, 11 BBQ points or 21 PCS points. Those are large changes.</p>
<p>The trial itself found pain at 3 months of -0.3 (CI -1.0 to 0.3). Disability was -1.6 at one week (CI -3.1 to -0.1) and -1.7 at 3 months (CI -3.2 to -0.2). There were no differences at 6 or 12 months.</p>
<div class="callout cy"><strong>The quiz is not the mechanism.</strong> Ram et al. (2023) pooled 14 studies and about 1,500 people. In the short term, change in pain neurophysiology knowledge was not associated with outcomes: pain r = -0.01 (CI -0.14 to 0.13), very low certainty; kinesiophobia r = 0.02; catastrophising r = -0.03, low certainty. What seems to count is changing beliefs about consequences and threat, and carrying that into behaviour.</div>
<h3>Other paths</h3>
<p>Murillo et al. (2023), in PNE plus exercise, found that kinesiophobia and distress linked to central sensitisation mediated disability and medication use. Catastrophising and pain intensity did not. The source does not give the size of those indirect effects.</p>
<p>Alalawi (2026) reanalysed the Indian RCT of Sidiq et al. (2024). In 46 participants who received education plus physiotherapy, emotional wellbeing (WHO-5) had a mediated causal effect of -1.66 (CI -2.8 to -0.72), about a quarter of the effect on disability. Self-efficacy did not mediate. No mediator explained pain. The recovery trajectories from the same material are in the Saudi section: the author is Saudi and the data are from India.</p>
<p>Núñez-Cortés et al. (2024, Neuroscience &amp; Biobehavioral Reviews) analysed 11 studies. The number of target concepts was associated with change in pain (F = 4.45; p = 0.04; R² 26.07%%). Only two concepts had their own effect on pain: transferring knowledge into an adaptive behaviour change, and pain reconceptualisation. No concept had an effect on disability.</p>
<p>Di-Bonaventura et al. (2025) compared 3 hours of PNE with a booklet in 66 participants. Plasma BDNF did not change (p = 0.708). Both groups improved on pain: PNE d = 0.70 and booklet d = 0.39.</p>
<h3>What people say after receiving it</h3>
<ul>
<li>Rizzo et al. (2024), n = 20, after an education-based intervention: the themes included "are you suggesting my pain is not real?", "my pain is different", and doubt about how to carry it into daily life.</li>
<li>Ciolan et al. (2025), 9 studies and 188 participants, moderate confidence: effective communication, emotional support and empowerment.</li>
<li>Kühn et al. (2026), 16 studies and 329 participants, 6 synthesised findings. The source used here does not list those six findings.</li>
<li>Watson et al. (2019), in the metasynthesis: letting the patient tell their story helps reconceptualisation.</li>
</ul>
<div class="callout"><strong>A neighbouring field, with large effects.</strong> Pain Reprocessing Therapy (Ashar et al., 2022, n = 151) goes beyond classical PNE. Versus placebo, g -1.14. Versus usual care, g -1.74. Pain-free or nearly pain-free: 66%% with PRT, 20%% with placebo and 10%% with usual care. At one year: g -0.70 and -1.05. This is not pure PNE. It shows where the field is heading: reconceptualisation with exposure and active reappraisal.</div>
<p class="small soft">Reading. Passing the knowledge quiz is not the mechanism. The chain that does appear in the mediation analyses runs through threat beliefs and behaviour.</p>
""" % (L, C["med_pain"], C["med_dis"])

def dose():
    return """
<p class="lead">Doing PNE means choosing a format, a content and a dose. The reviews do not agree on a single moderator, and the figures below stay with the outcome each review measured.</p>
<h3>Formats</h3>
<div class="grid-2">
 <div class="card"><span class="tag">Group</span><p>In Romm et al. (2021) the group format moderated the effect on kinesiophobia (d = 0.80; CI 0.09 to 1.50). In that review, dose did not moderate the effect. In Ma et al. (2024) the group subgroup had a pain MD of -1.76. Salazar-Méndez et al. (2024, PeerJ) is only a protocol comparing group and individual delivery (n = 69). There are no results yet.</p></div>
 <div class="card"><span class="tag">Online</span><p>de Oliveira Lima et al. (2021), 6 trials and n = 1,664, studied self-guided web education. Pain: SMD -0.23 in the short term and -0.26 in the medium term. Disability: -0.36. No added benefit over usual care. García-Lucas et al. (2026) tested 12 audiovisual lessons for pregnancy-related lumbopelvic pain (n = 211): pain MD -0.5 (CI -1.0 to 0.0) and kinesiophobia MD -1.4 (CI -2.3 to -0.4).</p></div>
 <div class="card"><span class="tag">Virtual reality</span><p>McConnell et al. (2024) ran a feasibility study: 52 people enrolled, 32 completed, with no between-group differences. The full-text extraction puts the mean session at about 21 minutes. The number of sessions varied by therapist, so total minutes cannot be calculated.</p></div>
 <div class="card"><span class="tag">Single session</span><p>Tomás-Rodríguez et al. (2024), n = 121, added 60 minutes of PNE to a back school. Pain did not fall. The CSI and the PCS did improve at 12 weeks.</p></div>
</div>
<h3>Metaphors</h3>
<p>Louw et al. (2019) surveyed clinicians: 19 of 27 responded (70%%). Six of 11 metaphors had a mean above 3, and none stood out clearly. There is no winning metaphor. It is chosen with the person.</p>
<h3>Doses that exceed the MCID</h3>
<p>Núñez-Cortés et al. (2024, Pain) pooled 26 RCTs and n = 1,852, with PNE added to exercise for chronic spinal pain. The effect of exercise alone was small. The source does not give the figure for that small effect. Salazar-Méndez et al. (2023) pooled 23 studies and n = 2,352. Doses ranged from 40 to 720 minutes and the dose-effect relationship was linear. Each card is a different outcome. They are not added together.</p>
%s
%s
<h3>Pain subgroups in Ma et al. 2024</h3>
<p>A negative sign favours PNE. In the meta-regression, only the length of each session was associated with greater pain reduction. The source does not publish the coefficient of that meta-regression.</p>
%s
<h3>Content</h3>
<ul>
<li>Reconceptualise: pain as protection, not as damage (Moseley and Butler, 2015).</li>
<li>Close each block with a translation into behaviour: what to do differently this week. That concept, with reconceptualisation, was one of the two with its own effect on pain (Núñez-Cortés et al., 2024).</li>
<li>Work on beliefs about the consequences of back pain, the largest mediator in RESOLVE (Cashin et al., 2023).</li>
<li>Avoid "injury", "degeneration" and "wear" (KNGF 2021). Say explicitly that the pain is real (Rizzo et al., 2024). Let the person tell their story (Watson et al., 2019).</li>
</ul>
<h3>What to measure</h3>
<p>The rNPQ shows whether the content was understood. Ram et al. (2023) show that this knowledge change does not predict short-term pain, so it is not the clinical target.</p>
%s
""" % (C["dose"], C["ladder"], C["ma"], C["measures"])

def clinic():
    return """
<p class="lead">In clinic, PNE is used with exercise or with other active work. JOSPT 2021 summarises that none of the studies of PNE alone improved pain, and that 5 of 6 studies that combined it with exercise or manual therapy did reduce pain.</p>
<div class="callout"><strong>A practical proposal, not a validated programme.</strong> The eight steps come from the sources cited on each line. Nobody has tested this package, as written here, as a single intervention.</div>
<ol class="rules">
<li>Who. Persistent pain for more than 3 months, especially with high kinesiophobia or catastrophising, or with a high risk of chronicity.<small>This is how the 2026 Saudi guideline and KNGF profile 3 set the priority.</small></li>
<li>Never alone. Always joined to exercise or to active work.<small>JOSPT, grade A. No stand-alone PNE improved pain in that guideline's summary.</small></li>
<li>Dose. Aim for about 150 minutes in total for disability and about 200 minutes for pain.<small>Núñez-Cortés et al., 2024, Pain. Sessions of 60 minutes or longer when possible (Ma et al., 2024). Group format is an option and saves clinician time (Romm et al., 2021; Ma et al., 2024).</small></li>
<li>Content. Reconceptualise pain as protection and close each block with a behaviour for that week.<small>Núñez-Cortés et al., 2024. Beliefs about the consequences of back pain: Cashin et al., 2023.</small></li>
<li>Language. Avoid injury, degeneration and wear. Validate that the pain is real. Let the person tell their story.<small>KNGF 2021. Rizzo et al., 2024. Watson et al., 2019.</small></li>
<li>Metaphors. Choose them with the person. None is superior.<small>Louw et al., 2019. Cultural adaptation into Arabic is in Najem et al., 2025, and Basalem et al., 2025, in the Saudi section.</small></li>
<li>Measure at the start and at 6 to 12 weeks: NRS, a region-specific disability scale, TSK-11 and PCS. The rNPQ stays as a comprehension check.<small>Arabic versions of the TSK, PCS and CSI are in the table in the previous section. Ram et al., 2023.</small></li>
<li>Expectation. A larger change in kinesiophobia than in pain is what the trials show. A minority respond.<small>Watson et al. (2021) estimate that the proportion of people who respond runs from 18% to 45%. There was not enough evidence of true between-person differences in response.</small></li>
</ol>
"""

def evidence():
    return """
<p class="lead">The comparison changes the result. Added to exercise or physiotherapy, meta-analyses show about 1 point on a 0 to 10 pain scale in the short term, with low to moderate certainty. Against another credible active education, the better controlled trials are mostly null on the primary outcome.</p>
<h3>Pain, 0 to 10</h3>
<p class="small soft">%s Wood and Hendrick publish a positive sign in favour of PNE. Ma, Cancela and Siddall publish a negative sign in favour of PNE.</p>
%s
<h3>Disability, fear and catastrophising</h3>
<p>Siddall et al. (2022) is PNE plus exercise versus exercise. Medina-Viedma et al. (2025) compare with physiotherapy or with no intervention: the mixed comparator inflates the effect. Cancela et al. (2025) do not find a significant effect on disability.</p>
<p class="small soft">%s</p>
%s
<h3>A 0 to 100 scale</h3>
<p class="small soft">%s</p>
%s
<h3>Further figures from the same lines of evidence</h3>
%s
<p>Hurley-Wallace et al. (2025), in a component network meta-analysis of knee or hip osteoarthritis, describe little or no effect on pain or function, benefits on the psychological variables, and a worse outcome when PNE is used alone. The source does not give a numeric estimate for that "little or no effect". Escriche-Escuder et al. (2023) scoped tendinopathy: 5 studies, n = 164, with no pooled effect.</p>
<p>Delgado-Gil et al. (2025), shoulder, n = 55, four 75 minute sessions added to manual therapy and exercise. The abstract reports a significant interaction for range of motion, disability, catastrophising, kinesiophobia and therapeutic alliance. The abstract extraction gives the disability interaction F = 6.14, p = 0.01; TSK F = 7.62, p = 0.008; PCS F = 8.79, p = 0.01. Pain is not among the significant interactions. These are not mean differences.</p>
<p>Louw et al. (2014), preoperative PNE for lumbar radiculopathy: no difference in pain or function at one year, and a better surgical experience. The abstract gives P = 0.183 for low back pain, P = 0.075 for leg pain and P = 0.365 for the ODI at 12 months, in 67 people with outcomes. The randomised n is not in the abstract. Healthcare use favoured PNE (P = 0.007).</p>
<p>Huysmans et al. (2023), lumbar surgery, n = 120: pain was not better at 12 months. There were gains on the SF-36 physical score, an additional decrease of 3.15 on the TSK (CI 0.25 to 6.04) and of 6.18 on the PCS (CI 1.97 to 10.39), and a cost-effective result of -€2,732.</p>
<p>Salazar-Méndez et al. (2024), preoperative PNE for arthroplasty: only 2 studies of knee replacement, n = 147.</p>
<h3>Trials with an active comparator</h3>
<p>The primary outcome of these trials did not favour PNE with an interval that excluded 0. Malfliet et al. (2025) compare a package (PNE, stress management and cognition-targeted exercise) with usual physiotherapy, not PNE alone. Larsen et al. (2024) give PNE in both arms and test the added exercise. In Dams et al. (2023) the value -1.31 corresponds, in the abstract extraction, to a smaller improvement with PNE (change 4.22 versus 5.53).</p>
%s
<p>What does move in that group of trials: TSK-17 -3.97 (CI -7.36 to -0.58) at 12 months (Adenis et al., 2026); the TSK and PCS from Huysmans et al. (2023), cited above; pain-free at the end, 23.3%% versus 5.0%% (Malfliet et al., 2025). In Malfliet the NDI also differed at the end, 3.55 (CI 1.12 to 6.26), P = 0.006, and at 12 months, 3.54 (CI 0.81 to 6.28), P = 0.02. The 6 month primary did not. The reported saving is US$854.01. The positive sign in that trial favours the package that includes PNE.</p>
<div class="grid-2">
 <div class="card"><span class="tag">For</span><p>Meta-analyses of PNE added to exercise give about 1 point on a 0 to 10 pain scale and moderate to large effects on kinesiophobia. In the dose reviews, the number of minutes has a coherent relationship with the effect.</p></div>
 <div class="card"><span class="tag coral">Against</span><p>Cuenca-Martínez et al. (2023), an umbrella review of 16 reviews: stand-alone PNE is not significant and the reviews are of critically low quality. Riley et al. (2026): only 5 high-integrity RCTs, and no reliable evidence that PNE adds to a specific physical intervention on pain or function. Ram et al. (2023): knowledge is not associated with outcomes. When the comparator is another active education, the effect on pain and function drops away and kinesiophobia is what often remains.</p></div>
</div>
<p class="small soft">Reading. PNE works as content inside an active intervention. A specific advantage of the neuroscience content over a good education that is not neuroscience is not shown for pain or function.</p>
<h3>Limits that remain open</h3>
<ul>
<li>There are few comparisons against a credible active education with 12 month follow-up.</li>
<li>Long-term effects on pain and function are inconsistent. Wood and Hendrick (2019) find no long-term effect.</li>
<li>It is unknown which component is doing the work: content, alliance, exposure or dose.</li>
<li>Evidence in athletes is very thin. The volleyball trial in the New section is small and retrospectively registered.</li>
<li>There are no data on sex and the hormonal cycle in the response to PNE. Holmes et al. (2026) set this as an agenda, in an editorial, not in a trial.</li>
<li>Review quality is low (Cuenca-Martínez et al., 2023) and RCT integrity is doubtful (Riley et al., 2026).</li>
</ul>
""" % (L, C["pain"], L, C["smd"], L, C["watson"], C["more"], C["nulls"])

def new():
    return """
<p class="lead">From 2024 to 2026 the field sharpened dose, target concepts and comparisons against active education. The figures for each paper are in Dose, in How it works or in Evidence. This section is the map, with no new numbers.</p>
<div class="grid-3">
 <div class="card"><span class="tag">2024</span><p>Dose and target concepts (Núñez-Cortés et al.). Short-term low back pain (Ma et al.). A single session (Tomás-Rodríguez et al.). Virtual reality, feasibility (McConnell et al.). An Indian trial later reanalysed by Alalawi (Sidiq et al.).</p></div>
 <div class="card"><span class="tag">2025</span><p>An umbrella review in low back pain (Cancela et al.). Low back pain with a mixed comparator (Medina-Viedma et al.). Knee or hip by components (Hurley-Wallace et al.). PNE+ (Tatikola et al.). Whiplash (Malfliet et al.). Shoulder (Delgado-Gil et al.). BDNF (Di-Bonaventura et al.). Qualitative work (Ciolan et al.).</p></div>
 <div class="card"><span class="tag">2026</span><p>RCT integrity (Riley et al.). Sleep and psychosocial variables (Khan et al.). 12 month follow-up (Adenis et al.). Pregnancy, online (García-Lucas et al.). Qualitative work (Kühn et al.). Cultural feasibility in India (Ganapathy et al.), with no abstract available and no figures to cite.</p></div>
</div>
<h3>Sport</h3>
<p>Koç and Dengiz (2026) studied elite volleyball players with chronic shoulder pain: 16 with PNE and 24 in the control group, 12 sessions of 45 minutes over 6 weeks. PCS partial eta squared 0.76. Resting pain partial eta squared 0.42. Retrospective registration and a small sample. Maguire et al. (2019) gave one 70 minute session to 61 sports therapy students and knowledge improved, MD 3.2 (CI 2.1 to 4.3). That is training, not a patient trial. Holmes et al. (2026, BJSM) is an editorial on pain neuroscience in the female athlete: hormones, pelvic pain and descending modulation. It is not a trial.</p>
<h3>A protocol, still without results</h3>
<p>Morales-Osorio et al. (2026) published the FIBROIA protocol: telerehabilitation with artificial-intelligence-guided exercise plus PNE for fibromyalgia, 50 participants planned, in Latin America.</p>
"""

def guides():
    return """
<p class="lead">Guidelines that name PNE tie it to another intervention, or they leave it conditional. NICE does not name it. The code column is a proposal on this page so the rows can be compared at a glance. It is not an official scale.</p>
%s
<p class="small soft">Proposed code, not official, taken from the working coding: 4 for grade A, 2 for conditional, 1 for consider, 0 for no PNE recommendation. JOSPT and the Saudi guideline talk about PNE. WHO and NICE talk about education, with the nuance in each row.</p>
<div class="callout"><strong>July 2026 and NICE NG59.</strong> Recommendation 1.2.1 remains in force and asks clinicians to give information on the nature of low back pain as part of self-management. Recommendations 1.2.13 and 1.2.14, on psychological therapy and on combined physical and psychological programmes, were withdrawn because those areas were not prioritised for update. The 2026 Saudi guideline was adapted from NG59 before that withdrawal.</div>
<p>JOSPT 2021 covers RCTs up to 1 July 2020. Standard education receives grade B, and not as a stand-alone treatment. The 2012 guideline already asked, at grade B, to emphasise the neuroscience that explains pain perception. The 2021 grade A is for giving PNE together with exercise or manual therapy, and for preferring active treatments over stand-alone education.</p>
<p>The KNGF row summarises the full text of the 2021 Dutch guideline (Overweeg, profile 3). Apeldoorn et al. (2024) is the journal paper of that guideline in the European Journal of Physical and Rehabilitation Medicine. On this page the clinical detail comes from the guideline text, not from new figures in that paper.</p>
""" % C["guides"]

def saudi():
    return """
<p class="lead">This section is an annex. The method is in the sections above. Here are the Saudi recommendation, what is published on Saudi physiotherapists' knowledge, and a reanalysis by a Saudi author of a trial conducted in India.</p>
<div class="card glow">
 <span class="tag coral">Annex</span>
 <h3>The 2026 Saudi guideline</h3>
 <p>Aldera et al. (2026) answer question 3.11 on chronic non-specific low back pain. The guideline suggests using PNE and prioritising it for people at higher risk of disability and chronicity. The recommendation is conditional for, with low certainty. The evidence base is Wood and Hendrick (2019). The update search found no new studies. No adverse events were reported.</p>
 <p>For the Saudi context, the guideline judged PNE probably not acceptable because it might increase the clinician's workload, although it cites a feasibility trial (GLITtER) that supported acceptability. It judged PNE feasible with training. Telehealth might improve access. There is a concern about equity in rural areas. GLITtER is not among the 91 sources on this page: it is named only as the guideline cites it.</p>
</div>
<h3>Table 22. A positive sign favours PNE</h3>
%s
<div class="callout"><strong>A label that does not match its interval.</strong> The TSK row (MD 4.72; CI 2.32 to 7.13) says there may be little or no effect, and the interval excludes 0. Read the row with that tension. This page does not correct the label.</div>
<h3>Knowledge and practice</h3>
<div class="grid-3">
 <div class="card"><span class="tag">rNPQ</span><p>Alhowimel et al. (2021): 111 Saudi physiotherapists, mean 6.7 ± 2.2 out of 12. 90%% scored 9 or less.</p></div>
 <div class="card"><span class="tag">Practice</span><p>Alshehri et al. (2020), n = 304. Patient education is used by 82.0%%, electrotherapy by 61.9%%, and spinal mobilisation or manipulation by 57.8%%. Biomedical and biopsychosocial orientations were relatively low. Clinicians with a stronger biopsychosocial orientation use CFT more. The source does not give the score for those orientations.</p></div>
 <div class="card"><span class="tag">Patients</span><p>Asiri et al. (2026), n = 298. Each 10 points of TSK were associated with +1.17 points of pain. Kinesiophobia explained 11%% to 12%% of the variance in pain.</p></div>
</div>
<h3>Reanalysis of an Indian trial</h3>
<p>Alalawi (2026, Umm Al-Qura) published secondary analyses of the RCT by Sidiq et al. (2024), conducted in India. These are not data collected in Saudi Arabia. The wellbeing mediation is in How it works. The recovery trajectories, with χ²(2) = 36.25, p &lt; 0.001 and Cramer's V 0.63, are these:</p>
%s
<p>No PNE randomised trial in patients conducted in Saudi Arabia was found.</p>
<h3>The Arabic-speaking world, which is not Saudi Arabia</h3>
<p>Muhsen and Sheeha (2026) randomised 120 physiotherapy students in Jordan, not in Saudi Arabia. One 70 minute class gave an NNT of 2.7 for knowledge and 3.6 for attitudes. At 6 months only knowledge was maintained. The abstract extraction adds the adjusted knowledge difference: 2.46 (CI 1.68 to 3.24) after the class and 1.20 (CI 0.25 to 2.15) at 6 months. Muhsen et al. (2025) describe 216 Jordanian students.</p>
<p>Najem et al. (2025) is an F1000 preprint on culturally adapted Arabic PNE in Lebanon, with 12 patients and 8 physiotherapists. Basalem et al. (2025), a scoping review of 38 studies: educational interventions are the most culturally adapted (9 studies, 33%%) and only 6 (22%%) used adaptation frameworks.</p>
<p>No Arabic validation of the rNPQ or the COPI-Adult turned up. Without them, the knowledge mechanism cannot be measured in Arabic-speaking patients. The TSK-AV-11, the Arabic PCS and the Arabic CSI do have data, in the table in Dose.</p>
<div class="callout"><strong>A study proposal, not evidence.</strong> A design to discuss: first, Arabic validation of the rNPQ and the COPI-Adult. Then a feasibility pilot RCT in Riyadh, randomised and with a blinded assessor, in adults with chronic low back pain at medium or high risk: adapted PNE (about 200 minutes in total, in a group, in Arabic) plus exercise, versus the same contact time of biomedical and ergonomic education plus the same exercise. Feasibility outcomes would be recruitment, adherence, retention and acceptability. Exploratory clinical outcomes would be the Arabic RMDQ, NRS, TSK-AV-11, Arabic PCS, Arabic CSI, rNPQ, COPI and follow-up at 3, 6 and 12 months, with a preplanned mediation in the style of Cashin et al. A feasibility pilot does not need a power calculation. No sample size is proposed here. An athlete arm remains an option, with no figures.</div>
""" % (C["t22"], C["paths"])

def data():
    prim = F["primary"]
    return """
<p class="lead">The Kaggle release is public. Dataset: <a href="https://www.kaggle.com/datasets/vctorandrsgmezlpez/pne-trials-evidence-extraction">PNE Trials Evidence Extraction</a> (CC BY 4.0). Notebook: <a href="https://www.kaggle.com/code/vctorandrsgmezlpez/pne-trials-open-data-review">PNE Trials Open Data Review</a>, which downloads the O'Keeffe file from Zenodo when it runs and does not redistribute it.</p>
<p>The same derived extraction is in this repository. It is published, cited figures in three CSV files. It is not individual patient data. It does not copy third-party text or figures. The licence for these tables is CC BY 4.0. The generator code is MIT.</p>
<div class="grid-3">
 <div class="card"><span class="tag">23 rows</span><h3>Trials</h3><p><a href="data/pne_trials_extraction.csv">pne_trials_extraction.csv</a>. 39 columns. One row per report. Population recorded in the file: 20 patients, 2 student samples and 1 athlete sample.</p></div>
 <div class="card"><span class="tag">21 rows</span><h3>Effects</h3><p><a href="data/pne_trial_effects_long.csv">pne_trial_effects_long.csv</a>. 11 columns. Long format: one row per report, outcome and time point, when the abstract gave a number.</p></div>
 <div class="card"><span class="tag">42 rows</span><h3>Estimates</h3><p><a href="data/pne_meta_estimates.csv">pne_meta_estimates.csv</a>. 17 columns. Estimates from reviews and from table 22, copied for the charts.</p></div>
</div>
<h3>Columns in the trial extraction</h3>
%s
<h3>Columns in the long file</h3>
%s
<h3>Columns in the estimates file</h3>
%s
<p>The primary_result field, as stored in the file, is null_result in %d rows, positive in %d, positive (borderline) in %d, no_between_group_test in %d and not_reported in %d. That is a count of the file's own labels, not a meta-analysis. The file notes say that Larsen et al. (2024) test exercise added to PNE, that Adenis 2024 and Adenis 2026 are the same trial, that Maguire and Muhsen are students, that Ganapathy et al. (2026) has no abstract and nothing was extracted, and that Sousa et al. (2024) was added from the data search and is not part of the narrative in the other sections.</p>
<div class="callout cy"><strong>O'Keeffe and Zenodo record 6760585.</strong> The cognitive functional therapy trial dataset (O'Keeffe et al.) is at <a href="https://doi.org/10.5281/zenodo.6760585">https://doi.org/10.5281/zenodo.6760585</a> (record <a href="https://zenodo.org/records/6760585">6760585</a>), CC BY 4.0, published on 27 June 2022. It has 206 rows and 145 columns: 106 in one arm and 100 in the other, in line with CFT (n = 106) versus group exercise and education (n = 100). It is not pure PNE: CFT includes reconceptualisation inside a cognitive functional approach, and the comparator also included education. This repository does not redistribute that file. The only link is the Zenodo record.</div>
<h3>Other open data, linked only</h3>
<ul>
<li>Dehghani et al. (2026), PNE plus Flexi-Bar exercise, PLOS ONE. Article <a href="https://doi.org/10.1371/journal.pone.0355692">10.1371/journal.pone.0355692</a>. Supplement S1, CC BY 4.0, n = 48: <a href="https://doi.org/10.1371/journal.pone.0355692.s001">10.1371/journal.pone.0355692.s001</a>. The extraction note says the means in table 2 of the article do not match the supplement CSV. This site does not redistribute that CSV.</li>
<li>Windsor, adapted PNE, Figshare, CC BY 4.0, n = 21 (13 adapted PNE and 8 general health education). Four 15 minute sessions, one a month, individual. It is not randomised and the record does not link a verified article. <a href="https://doi.org/10.6084/m9.figshare.26018443">10.6084/m9.figshare.26018443</a> and <a href="https://doi.org/10.6084/m9.figshare.26018440">10.6084/m9.figshare.26018440</a>.</li>
<li>Understanding of Pain, Figshare, CC BY 4.0, n = 55 third-year students, not patients. NPQ and HC-PAIRS. <a href="https://doi.org/10.6084/m9.figshare.5913511">10.6084/m9.figshare.5913511</a>.</li>
</ul>
<p>The search on 30 October 2026 found no pain neuroscience education dataset on Kaggle. Malfliet et al. (2025) state that the data are not available. The data statements for Larsen et al. (2024), RESOLVE, RESTORE, PREVENT and Chimenti et al. (2023) were left unverified in that search.</p>
""" % (chips(F["trial_cols"]), chips(F["effect_cols"]), chips(F["meta_cols"]),
      prim["null_result"], prim["positive"], prim["positive (borderline)"],
      prim["no_between_group_test"], prim["not_reported"])

def sources():
    return """
<p class="lead">91 sources in APA 7. Titles are copied as Crossref records them, so some keep title case. The year is the print year when one exists.</p>
<p>Status recorded in the check of 30 October 2026: 11 with the full text read, 57 open with the abstract read, and 23 abstract only. Each DOI in this list resolved at doi.org with a 302 response. The three guidelines without a DOI returned 200. The filter below needs JavaScript. Without it, the full list is visible.</p>
"""

D = dict(
lang="en", dir="ltr", loc="en-US",
title="Pain neuroscience education · Method, evidence and application",
desc="What PNE is, how it works, how it is dosed and how it is used with exercise, with the published figures and 91 sources.",
skip="Skip to content", brand="PNE · Method", navlabel="Sections",
n1="What", n2="Mechanism", n3="Dose", n4="Clinic", n5="Evidence",
n6="New", n7="Guidelines", n8="Saudi", n9="Data", n10="Sources",
kicker="Method · evidence · application",
h1a="Pain neuroscience education.", h1b="A method with a dose.", h1c="And a clear limit.",
lead="PNE changes the concept of pain: from a marker of damage to a signal of protection. Alone, it moves pain very little. Added to exercise, meta-analyses show about 1 point on a 0 to 10 scale in the short term, with low to moderate certainty. About 200 minutes are associated with exceeding the MCID for pain and about 150 minutes for disability. Against another active education, the better controlled trials are usually null on the primary outcome. Change in knowledge is not associated with pain (r = -0.01).",
cta1="Start with the method", cta2="See the dose",
k1="minutes of PNE added to exercise that exceed the MCID for pain",
k2="minutes that exceed the MCID for disability",
k3v="-0.01", k3="correlation between change in knowledge and short-term pain",
k4="sources with a DOI or link checked on 30 October 2026",
kpi_note="Pain and disability: Núñez-Cortés et al., 2024, Pain. Correlation: Ram et al., 2023, 14 studies and about 1,500 people. The interval and the sign of each figure are in Evidence.",
idx_t="INDEX",
i1="Definition, origin and the link with CFT.",
i2="Mediation, knowledge and behaviour.",
i3="Formats, metaphors, minutes and measures.",
i4="Eight steps for using it with exercise.",
i5="Added to exercise, and against active education.",
i6="What was published from 2024 to 2026.",
i7="JOSPT, WHO, KNGF, NICE and Saudi Arabia.",
i8="Annex: guideline, knowledge and a reanalysis.",
i9="Derived extraction. Dataset and notebook on Kaggle.",
i10="91 references, access status and link status.",
s1_num="WHAT IT IS", s1_h="An education that changes the concept of pain.", sec_what=what(),
s2_num="HOW IT WORKS", s2_h="Threat falls. The quiz does not carry the outcome.", sec_how=how(),
s3_num="HOW IT IS DONE", s3_h="Content, format and minutes.", sec_dose=dose(),
s4_num="HOW IT IS APPLIED", s4_h="Always with exercise or with active work.", sec_clinic=clinic(),
s5_num="EVIDENCE", s5_h="The comparator decides the result.", sec_evidence=evidence(),
s6_num="WHAT IS NEW", s6_h="What was published from 2024 to 2026.", sec_new=new(),
s7_num="GUIDELINES", s7_h="From grade A to no recommendation.", sec_guides=guides(),
s8_num="SAUDI ARABIA", s8_h="An annex, not the centre of the method.", sec_saudi=saudi(),
s9_num="DATA", s9_h="The extraction is here and on Kaggle.", sec_data=data(),
s10_num="SOURCES", s10_h="References and link status.", sec_sources=sources(),
src_filter="Filter sources", src_all="All", src_full="Full text",
src_oabs="Open, abstract", src_abs="Abstract only", src_count_label="sources shown",
st_full="Open, full text read", st_oabs="Open, abstract read", st_abs="Abstract only",
st_doi="DOI: resolved (302) on 30 October 2026",
st_http="Link: returned 200 on 30 October 2026",
disc_h="Disclaimer.",
disc_p="Educational information drawn from published sources. It is not personalised medical advice and it does not replace assessment by a health professional. Dose and study proposals are marked as proposals.",
foot="Víctor Andrés Gómez López, sports physiotherapist. Text and tables: CC BY 4.0. Code: MIT. Figures checked on 30 October 2026. Page updated on 1 November 2026.",
)
