# -*- coding: utf-8 -*-
from facts import charts, legend, dataset_facts
from render import esc

C = charts("es")
L = legend("es")
F = dataset_facts()

def chips(cols):
    return '<div class="cols">' + "".join("<code>%s</code>" % esc(c) for c in cols) + "</div>"

def what():
    return """
<p class="lead">La educación en neurociencia del dolor (PNE) es una intervención educativa. Busca cambiar el concepto de dolor: deja de verse como marcador de daño y pasa a entenderse como señal de la necesidad percibida de proteger el tejido.</p>
<h3>Definición</h3>
<p>Moseley y Butler (2015) la llaman Explaining Pain. Se apoya en estrategias de cambio conceptual. Los autores insisten en que no es consejo conductual ni cognitivo, y en que no niega la nocicepción. Según ese trabajo, aumenta el conocimiento, reduce la catastrofización y se acompaña de reducciones de dolor y discapacidad a corto plazo.</p>
<p>En la literatura aparecen como nombres equivalentes: pain neuroscience education (PNE), therapeutic neuroscience education, pain science education (PSE), pain neurophysiology education y Explaining Pain. Las revisiones los usan de forma intercambiable. Bonatesta et al. (2022) y Núñez-Cortés et al. (2024) dicen PSE.</p>
<h3>Origen</h3>
<p>El primer ensayo aleatorizado de referencia es Moseley et al. (2004, The Clinical Journal of Pain), en dolor lumbar crónico. La educación cambió las actitudes (SOPA(R)), la catastrofización (PCS), la elevación de la pierna recta y la flexión anterior. El cambio en el RMDQ fue pequeño. Los autores concluyeron que la educación, por sí sola, era insuficiente. El resumen no trae n, sesiones, minutos ni un número para el RMDQ.</p>
<p>El mismo año, Moseley (2004, European Journal of Pain) analizó a 121 pacientes. El cambio cognitivo se correlacionó con el cambio físico: r = 0,88 con la elevación de la pierna recta y r = 0,79 con la flexión anterior.</p>
<p>Las revisiones fundacionales son Louw et al. (2011), 8 estudios y n = 401, con síntesis narrativa, y Louw et al. (2016), 13 ECA. Esas dos revisiones, en las fuentes usadas aquí, no aportan un efecto agrupado que esta página pueda citar.</p>
<h3>Dónde se ubica</h3>
<div class="grid-2">
 <div class="card"><span class="tag">Modelo</span><h3>Biopsicosocial</h3><p>La PNE es una herramienta educativa dentro del modelo biopsicosocial. No es el modelo completo.</p></div>
 <div class="card"><span class="tag coral">No es PNE</span><h3>Terapia cognitivo funcional</h3><p>La CFT (O'Sullivan et al., 2018) es un abordaje conductual integrado: dar sentido al dolor, exposición con control y cambio de estilo de vida. Incluye una reconceptualización parecida a la PNE y la junta con exposición y cambio de conducta. Esa integración es lo que los datos de la PNE sola dejan abierto.</p></div>
</div>
<p>El ensayo RESTORE (Kent et al., 2023, Lancet, n = 492) evaluó CFT, no PNE aislada. A las 13 semanas el RMDQ fue DM -4,6 (IC -5,9 a -3,4) con CFT y DM -4,6 (IC -5,8 a -3,3) con CFT más biofeedback. El efecto se mantuvo a las 52 semanas. El ahorro social fue de unos AU$5276 por persona. Thiveos et al. (2024), 7 ECA, reportan certeza baja a moderada para dolor y discapacidad y certeza alta para autoeficacia. La fuente no trae el tamaño del efecto de ese metaanálisis.</p>
<p>Louw et al. (2021, JOSPT) sitúan la PNE como complemento del ejercicio y del movimiento para el paciente, y como foco central de la formación del clínico. Nijs et al. (2020) proponen integrarla con la entrevista motivacional. Es una guía práctica, sin datos de eficacia, y los autores piden ensayos.</p>
"""

def how():
    return """
<p class="lead">La teoría es una cadena: baja la amenaza percibida, bajan la catastrofización y el miedo al movimiento, suben la actividad y la exposición, y con eso bajan el dolor y la discapacidad. Los análisis de mediación ponen a prueba esa cadena.</p>
<h3>RESOLVE: qué medió</h3>
<p>Cashin et al. (2023) mediaron el ensayo RESOLVE (Bagg et al., 2022): 276 adultos con dolor lumbar crónico, educación más reentrenamiento sensoriomotor graduado frente a simulación. Mediaron 4 de 7 variables en dolor y 5 de 7 en discapacidad. En conjunto explicaron la mayor parte del efecto. El resumen no nombra cuáles quedaron fuera.</p>
<p class="small soft">%s</p>
<h3>Sobre el dolor</h3>
%s
<h3>Sobre la discapacidad</h3>
%s
<p>En el propio RESOLVE, el dolor a las 18 semanas fue -1,0 (IC -1,5 a -0,4) frente a la simulación, con 12 sesiones semanales (Bagg et al., 2022). Venter et al. (2026) no encontraron modificadores claros del efecto. La autopercepción de la espalda fue un posible modificador (β 0,18).</p>
<h3>PREVENT: dolor agudo</h3>
<p>Cashin et al. (2022) mediaron PREVENT (Traeger et al., 2019, JAMA Neurology, n = 202): 2 horas de educación frente a educación placebo en dolor lumbar agudo de alto riesgo. Mediaron la catastrofización, -0,64 (IC -1,31 a -0,15), y las creencias sobre la espalda, -0,51. La autoeficacia no medió. Para lograr 2 puntos de RMDQ, la MCID de ese análisis, harían falta 8 puntos de PSEQ, 11 de BBQ o 21 de PCS. Son cambios grandes.</p>
<p>El ensayo mismo tuvo dolor a los 3 meses de -0,3 (IC -1,0 a 0,3). La discapacidad fue -1,6 a la semana (IC -3,1 a -0,1) y -1,7 a los 3 meses (IC -3,2 a -0,2). No hubo diferencias a los 6 ni a los 12 meses.</p>
<div class="callout cy"><strong>El cuestionario no es el mecanismo.</strong> Ram et al. (2023) reunieron 14 estudios y unas 1500 personas. A corto plazo, el cambio en el conocimiento de la neurofisiología del dolor no se asoció con los resultados: dolor r = -0,01 (IC -0,14 a 0,13), certeza muy baja; kinesiofobia r = 0,02; catastrofización r = -0,03, certeza baja. Lo que parece contar es cambiar creencias sobre consecuencias y amenaza, y llevarlo a la conducta.</div>
<h3>Otros caminos</h3>
<p>Murillo et al. (2023), en PNE más ejercicio, encontraron mediación de la kinesiofobia y del malestar ligado a la sensibilización central sobre la discapacidad y el uso de medicación. La catastrofización y la intensidad del dolor no mediaron. La fuente no trae el tamaño de esos efectos indirectos.</p>
<p>Alalawi (2026) reanalizó el ECA indio de Sidiq et al. (2024). En 46 participantes con educación más fisioterapia, el bienestar emocional (WHO-5) tuvo un efecto causal mediado de -1,66 (IC -2,8 a -0,72), cerca de una cuarta parte del efecto en discapacidad. La autoeficacia no medió. Ningún mediador explicó el dolor. Las trayectorias de ese mismo material están en la sección Saudí: el autor es saudí y los datos son de la India.</p>
<p>Núñez-Cortés et al. (2024, Neuroscience &amp; Biobehavioral Reviews) analizaron 11 estudios. El número de conceptos diana se asoció con el cambio de dolor (F = 4,45; p = 0,04; R² 26,07%%). Solo dos conceptos tuvieron efecto propio sobre el dolor: transferir el conocimiento a un cambio conductual adaptativo, y la reconceptualización del dolor. Ningún concepto tuvo efecto sobre la discapacidad.</p>
<p>Di-Bonaventura et al. (2025) compararon 3 horas de PNE con un folleto en 66 participantes. No hubo cambio en el BDNF plasmático (p = 0,708). Ambos grupos bajaron en dolor: PNE d = 0,70 y folleto d = 0,39.</p>
<h3>Lo que dice quien la recibe</h3>
<ul>
<li>Rizzo et al. (2024), n = 20, después de una intervención basada en educación: aparecieron «¿insinúas que mi dolor no es real?», «mi dolor es diferente» y dudas sobre cómo llevarlo al día a día.</li>
<li>Ciolan et al. (2025), 9 estudios y 188 participantes, confianza moderada: comunicación eficaz, apoyo emocional y empoderamiento.</li>
<li>Kühn et al. (2026), 16 estudios y 329 participantes, 6 hallazgos sintetizados. La fuente usada aquí no lista esos seis hallazgos.</li>
<li>Watson et al. (2019), en su metasíntesis: dejar que el paciente cuente su historia facilita la reconceptualización.</li>
</ul>
<div class="callout"><strong>Un campo vecino, con efectos grandes.</strong> La Pain Reprocessing Therapy (Ashar et al., 2022, n = 151) va más allá de la PNE clásica. Frente a placebo, g -1,14. Frente a atención habitual, g -1,74. Libres o casi libres de dolor: 66%% con PRT, 20%% con placebo y 10%% con atención habitual. Al año: g -0,70 y -1,05. No es PNE pura. Muestra hacia dónde va el campo: reconceptualización con exposición y reevaluación activa.</div>
<p class="small soft">Lectura. Aprobar el cuestionario de conocimiento no es el mecanismo. La cadena que sí aparece en los análisis de mediación pasa por creencias de amenaza y por la conducta.</p>
""" % (L, C["med_pain"], C["med_dis"])

def dose():
    return """
<p class="lead">Hacer PNE es elegir un formato, un contenido y una dosis. Las revisiones no coinciden en un único moderador, y las cifras de abajo se quedan en el resultado que cada una midió.</p>
<h3>Formatos</h3>
<div class="grid-2">
 <div class="card"><span class="tag">Grupal</span><p>En Romm et al. (2021) el formato grupal moderó el efecto sobre la kinesiofobia (d = 0,80; IC 0,09 a 1,50). En esa revisión la dosis no moderó el efecto. En Ma et al. (2024) el subgrupo grupal obtuvo DM -1,76 en dolor. Salazar-Méndez et al. (2024, PeerJ) es solo un protocolo que compara grupo e individual (n = 69). Todavía no hay resultados.</p></div>
 <div class="card"><span class="tag">En línea</span><p>de Oliveira Lima et al. (2021), 6 ensayos y n = 1664, estudiaron educación web autoguiada. Dolor: DME -0,23 a corto plazo y -0,26 a medio plazo. Discapacidad: -0,36. Sin beneficio añadido sobre la atención habitual. García-Lucas et al. (2026) probaron 12 lecciones audiovisuales en dolor lumbopélvico del embarazo (n = 211): dolor DM -0,5 (IC -1,0 a 0,0) y kinesiofobia DM -1,4 (IC -2,3 a -0,4).</p></div>
 <div class="card"><span class="tag">Realidad virtual</span><p>McConnell et al. (2024) hicieron un estudio de factibilidad: 52 personas inscritas, 32 completaron, sin diferencias entre grupos. La extracción del texto sitúa la sesión media en unos 21 minutos. El número de sesiones varió según el terapeuta, así que los minutos totales no se pueden calcular.</p></div>
 <div class="card"><span class="tag">Sesión única</span><p>Tomás-Rodríguez et al. (2024), n = 121, añadieron 60 minutos de PNE a una escuela de espalda. No bajó el dolor. Sí mejoraron el CSI y la PCS a las 12 semanas.</p></div>
</div>
<h3>Metáforas</h3>
<p>Louw et al. (2019) encuestaron a clínicos: respondieron 19 de 27 (70%%). Seis de 11 metáforas tuvieron una media mayor de 3, y ninguna destacó con claridad. No hay una metáfora ganadora. Se elige según la persona.</p>
<h3>Dosis que supera la MCID</h3>
<p>Núñez-Cortés et al. (2024, Pain) reunieron 26 ECA y n = 1852, con PNE añadida al ejercicio en dolor espinal crónico. El efecto del ejercicio aislado fue pequeño. La fuente no da la cifra de ese efecto pequeño. Salazar-Méndez et al. (2023) reunieron 23 estudios y n = 2352. Las dosis iban de 40 a 720 minutos y la relación entre dosis y efecto fue lineal. Cada tarjeta es un resultado distinto. No se suman entre sí.</p>
%s
%s
<h3>Subgrupos de dolor en Ma et al. 2024</h3>
<p>Signo negativo a favor de la PNE. En la metarregresión, solo la duración de cada sesión se asoció con más reducción del dolor. La fuente no publica el coeficiente de esa metarregresión.</p>
%s
<h3>Contenido</h3>
<ul>
<li>Reconceptualizar: el dolor como protección, no como daño (Moseley y Butler, 2015).</li>
<li>Cerrar cada bloque con una traducción a la conducta: qué hacer distinto esta semana. Ese concepto, junto con la reconceptualización, fue uno de los dos con efecto propio sobre el dolor (Núñez-Cortés et al., 2024).</li>
<li>Trabajar las creencias sobre las consecuencias del dolor de espalda, el mediador de mayor tamaño en RESOLVE (Cashin et al., 2023).</li>
<li>Evitar «lesión», «degeneración» y «desgaste» (KNGF 2021). Decir de forma explícita que el dolor es real (Rizzo et al., 2024). Dejar que la persona cuente su historia (Watson et al., 2019).</li>
</ul>
<h3>Qué se mide</h3>
<p>El rNPQ sirve para ver si el contenido se entendió. Ram et al. (2023) muestran que ese cambio de conocimiento no predice el dolor a corto plazo, así que no es el objetivo clínico.</p>
%s
""" % (C["dose"], C["ladder"], C["ma"], C["measures"])

def clinic():
    return """
<p class="lead">En la clínica la PNE se aplica junto con ejercicio o con otro trabajo activo. JOSPT 2021 resume que ninguno de los estudios con PNE sola mejoró el dolor, y que 5 de 6 estudios que la combinaron con ejercicio o terapia manual sí lo redujeron.</p>
<div class="callout"><strong>Propuesta práctica, no un programa validado.</strong> Los ocho pasos salen de las fuentes citadas en cada línea. Nadie ha probado este paquete, tal como está escrito aquí, como una intervención única.</div>
<ol class="rules">
<li>A quién. Dolor persistente de más de 3 meses, sobre todo con kinesiofobia o catastrofización altas, o con riesgo alto de cronicidad.<small>Así lo priorizan la guía saudí de 2026 y la KNGF en el perfil 3.</small></li>
<li>Nunca sola. Siempre unida al ejercicio o al trabajo activo.<small>JOSPT, grado A. Ninguna PNE aislada mejoró el dolor en el resumen de esa guía.</small></li>
<li>Dosis. Apuntar a unos 150 minutos en total para la discapacidad y unos 200 minutos para el dolor.<small>Núñez-Cortés et al., 2024, Pain. Sesiones de 60 minutos o más si es posible (Ma et al., 2024). El formato grupal es una opción y ahorra tiempo (Romm et al., 2021; Ma et al., 2024).</small></li>
<li>Contenido. Reconceptualizar el dolor como protección y cerrar cada bloque con una conducta de esa semana.<small>Núñez-Cortés et al., 2024. Creencias sobre las consecuencias del dolor de espalda: Cashin et al., 2023.</small></li>
<li>Lenguaje. Evitar lesión, degeneración y desgaste. Validar que el dolor es real. Dejar que la persona cuente su historia.<small>KNGF 2021. Rizzo et al., 2024. Watson et al., 2019.</small></li>
<li>Metáforas. Elegirlas con la persona. Ninguna es superior.<small>Louw et al., 2019. La adaptación cultural al árabe está en Najem et al., 2025, y en Basalem et al., 2025, dentro de la sección Saudí.</small></li>
<li>Medir al inicio y a las 6 a 12 semanas: NRS, una escala de discapacidad de la región, TSK-11 y PCS. El rNPQ queda como control de comprensión.<small>Versiones árabes de TSK, PCS y CSI en la tabla de la sección anterior. Ram et al., 2023.</small></li>
<li>Expectativa. Es esperable más cambio en la kinesiofobia que en el dolor. Responde una minoría.<small>Watson et al. (2021) estiman que la proporción de personas que responden va del 18% al 45%. No hubo evidencia suficiente de diferencias reales de respuesta entre individuos.</small></li>
</ol>
"""

def evidence():
    return """
<p class="lead">La comparación cambia el resultado. Añadida al ejercicio o a la fisioterapia, los metaanálisis muestran alrededor de 1 punto sobre 10 en dolor a corto plazo, con certeza baja a moderada. Frente a otra educación activa y creíble, los ensayos mejor controlados son en su mayoría nulos en el resultado primario.</p>
<h3>Dolor, escala 0 a 10</h3>
<p class="small soft">%s Wood y Hendrick publican el signo positivo a favor de la PNE. Ma, Cancela y Siddall publican el signo negativo a favor de la PNE.</p>
%s
<h3>Discapacidad, miedo y catastrofización</h3>
<p>Siddall et al. (2022) es PNE más ejercicio frente a ejercicio. Medina-Viedma et al. (2025) comparan con fisioterapia o con no intervención: el comparador mezclado infla el efecto. Cancela et al. (2025) no encuentran un efecto significativo en discapacidad.</p>
<p class="small soft">%s</p>
%s
<h3>Escala 0 a 100</h3>
<p class="small soft">%s</p>
%s
<h3>Otras cifras de las mismas líneas de evidencia</h3>
%s
<p>Hurley-Wallace et al. (2025), en un metaanálisis en red por componentes de rodilla o cadera, describen poco o ningún efecto en dolor o función, beneficios en las variables psicológicas y peor resultado cuando la PNE va sola. La fuente no trae un estimador numérico de ese «poco o ningún efecto». Escriche-Escuder et al. (2023) revisaron el alcance en tendinopatía: 5 estudios, n = 164, sin efecto agrupado.</p>
<p>Delgado-Gil et al. (2025), hombro, n = 55, 4 sesiones de 75 minutos añadidas a terapia manual y ejercicio. El resumen reporta interacción significativa en rango de movimiento, discapacidad, catastrofización, kinesiofobia y alianza terapéutica. La extracción del resumen da la interacción de discapacidad F = 6,14, p = 0,01; TSK F = 7,62, p = 0,008; PCS F = 8,79, p = 0,01. El dolor no aparece entre las interacciones significativas. No son diferencias de medias.</p>
<p>Louw et al. (2014), PNE preoperatoria en radiculopatía lumbar: sin diferencia en dolor ni en función al año, y mejor experiencia quirúrgica. El resumen da P = 0,183 para dolor lumbar, P = 0,075 para dolor de pierna y P = 0,365 para el ODI a los 12 meses, en 67 personas con resultado. El n aleatorizado no está en el resumen. El uso de servicios de salud favoreció a la PNE (P = 0,007).</p>
<p>Huysmans et al. (2023), cirugía lumbar, n = 120: el dolor no fue mejor a los 12 meses. Hubo mejoras en el SF-36 físico, una disminución adicional de 3,15 en la TSK (IC 0,25 a 6,04) y de 6,18 en la PCS (IC 1,97 a 10,39), y un resultado coste-efectivo de -€2732.</p>
<p>Salazar-Méndez et al. (2024), PNE preoperatoria en artroplastia: solo 2 estudios en prótesis de rodilla, n = 147.</p>
<h3>Ensayos con comparador activo</h3>
<p>El resultado primario de estos ensayos no favoreció a la PNE con un intervalo que excluyera el 0. Malfliet et al. (2025) comparan un paquete (PNE, manejo del estrés y ejercicio orientado a la cognición) con fisioterapia habitual, no PNE sola. Larsen et al. (2024) ponen la PNE en los dos brazos y prueban el ejercicio añadido. En Dams et al. (2023) el valor -1,31 corresponde, según la extracción del resumen, a una mejoría menor con la PNE (cambio 4,22 frente a 5,53).</p>
%s
<p>Lo que sí se mueve en ese grupo de ensayos: TSK-17 -3,97 (IC -7,36 a -0,58) a los 12 meses (Adenis et al., 2026); la TSK y la PCS de Huysmans et al. (2023), citadas arriba; libres de dolor al terminar, 23,3%% frente a 5,0%% (Malfliet et al., 2025). En Malfliet el NDI también difirió al terminar, 3,55 (IC 1,12 a 6,26), P = 0,006, y a los 12 meses, 3,54 (IC 0,81 a 6,28), P = 0,02. El primario a los 6 meses no. El ahorro reportado es de US$854,01. El signo positivo de ese ensayo favorece al paquete con PNE.</p>
<div class="grid-2">
 <div class="card"><span class="tag">A favor</span><p>Los metaanálisis de PNE añadida al ejercicio dan alrededor de 1 punto sobre 10 de dolor y efectos moderados a grandes en kinesiofobia. En las revisiones de dosis, la cantidad de minutos tiene una relación coherente con el efecto.</p></div>
 <div class="card"><span class="tag coral">En contra</span><p>Cuenca-Martínez et al. (2023), revisión paraguas de 16 revisiones: la PNE aislada no es significativa y las revisiones son de calidad críticamente baja. Riley et al. (2026): solo 5 ECA de alta integridad, y ninguna evidencia fiable de que la PNE sume a una intervención física concreta en dolor o función. Ram et al. (2023): el conocimiento no se asocia con los resultados. Cuando el comparador es otra educación activa, el efecto en dolor y función desaparece y suele quedar la kinesiofobia.</p></div>
</div>
<p class="small soft">Lectura. La PNE funciona como contenido dentro de una intervención activa. La ventaja específica del contenido neurocientífico frente a una buena educación que no es neurocientífica no está demostrada en dolor ni en función.</p>
<h3>Límites que siguen abiertos</h3>
<ul>
<li>Hay pocas comparaciones contra una educación activa creíble con seguimiento de 12 meses.</li>
<li>Los efectos a largo plazo en dolor y función son inconsistentes. Wood y Hendrick (2019) no encuentran efecto a largo plazo.</li>
<li>No se sabe qué componente trabaja: el contenido, la alianza, la exposición o la dosis.</li>
<li>Hay muy poca evidencia en deportistas. El ensayo de vóleibol de la sección Novedad es pequeño y tiene registro retrospectivo.</li>
<li>No hay datos sobre el sexo y el ciclo hormonal en la respuesta a la PNE. Holmes et al. (2026) lo plantean como agenda, en un editorial, no en un ensayo.</li>
<li>La calidad de las revisiones es baja (Cuenca-Martínez et al., 2023) y la integridad de los ECA es dudosa (Riley et al., 2026).</li>
</ul>
""" % (L, C["pain"], L, C["smd"], L, C["watson"], C["more"], C["nulls"])

def new():
    return """
<p class="lead">De 2024 a 2026 el campo afinó la dosis, los conceptos diana y las comparaciones contra educación activa. Las cifras de cada trabajo están en Dosis, en Cómo funciona o en Evidencia. Aquí queda el mapa, sin números nuevos.</p>
<div class="grid-3">
 <div class="card"><span class="tag">2024</span><p>Dosis y conceptos diana (Núñez-Cortés et al.). Dolor lumbar a corto plazo (Ma et al.). Sesión única (Tomás-Rodríguez et al.). Realidad virtual, factibilidad (McConnell et al.). Ensayo indio reanalizado después por Alalawi (Sidiq et al.).</p></div>
 <div class="card"><span class="tag">2025</span><p>Paraguas en lumbalgia (Cancela et al.). Lumbalgia, comparador mezclado (Medina-Viedma et al.). Rodilla o cadera por componentes (Hurley-Wallace et al.). PNE+ (Tatikola et al.). Latigazo (Malfliet et al.). Hombro (Delgado-Gil et al.). BDNF (Di-Bonaventura et al.). Cualitativo (Ciolan et al.).</p></div>
 <div class="card"><span class="tag">2026</span><p>Integridad de los ECA (Riley et al.). Sueño y variables psicosociales (Khan et al.). Seguimiento a 12 meses (Adenis et al.). Embarazo, en línea (García-Lucas et al.). Cualitativo (Kühn et al.). Factibilidad cultural en India (Ganapathy et al.), sin resumen disponible y sin cifras que citar.</p></div>
</div>
<h3>Deporte</h3>
<p>Koç y Dengiz (2026) estudiaron vóleibolistas de élite con dolor crónico de hombro: 16 con PNE y 24 en el control, 12 sesiones de 45 minutos durante 6 semanas. PCS ηp² 0,76. Dolor en reposo ηp² 0,42. Registro retrospectivo y muestra pequeña. Maguire et al. (2019) dieron una sesión de 70 minutos a 61 estudiantes de terapia deportiva y el conocimiento mejoró, DM 3,2 (IC 2,1 a 4,3). Es formación, no un ensayo en pacientes. Holmes et al. (2026, BJSM) es un editorial sobre neurociencia del dolor en la deportista: hormonas, dolor pélvico y modulación descendente. No es un ensayo.</p>
<h3>Un protocolo, todavía sin resultados</h3>
<p>Morales-Osorio et al. (2026) publicaron el protocolo FIBROIA: telerrehabilitación con ejercicio guiado por inteligencia artificial más PNE en fibromialgia, 50 participantes previstos, en Latinoamérica.</p>
"""

def guides():
    return """
<p class="lead">Las guías que nombran la PNE la atan a otra intervención o la dejan en condicional. NICE no la nombra. La columna de código es una propuesta de esta página para poder compararlas de un vistazo. No es una escala oficial.</p>
%s
<p class="small soft">Código propuesto, no oficial, tomado de la codificación de trabajo: 4 grado A, 2 condicional, 1 considerar, 0 sin recomendación de PNE. JOSPT y la guía saudí hablan de PNE. La OMS y NICE hablan de educación, con el matiz de cada fila.</p>
<div class="callout"><strong>Julio de 2026 y NICE NG59.</strong> La recomendación 1.2.1 sigue vigente y pide informar sobre la naturaleza del dolor lumbar como parte del autocuidado. Se retiraron las recomendaciones 1.2.13 y 1.2.14, de terapia psicológica y de programas físicos y psicológicos combinados, porque esas áreas no se priorizaron para actualización. La guía saudí de 2026 se adaptó de NG59 antes de ese retiro.</div>
<p>JOSPT 2021 cubre ECA hasta el 1 de julio de 2020. La educación estándar recibe grado B, y no como tratamiento aislado. La guía de 2012 ya pedía, con grado B, enfatizar la neurociencia que explica la percepción del dolor. El grado A de 2021 es para dar la PNE junto con ejercicio o terapia manual, y para preferir tratamientos activos frente a la educación aislada.</p>
<p>La fila de la KNGF resume el texto completo de la guía neerlandesa de 2021 (Overweeg, perfil 3). Apeldoorn et al. (2024) es el artículo de esa guía en European Journal of Physical and Rehabilitation Medicine. En esta página el detalle clínico sale del texto de la guía, no de cifras nuevas de ese artículo.</p>
""" % C["guides"]

def saudi():
    return """
<p class="lead">Esta sección es un anexo. El método está en las secciones anteriores. Aquí se reúnen la recomendación saudí, el conocimiento de fisioterapeutas saudíes y un reanálisis con autor saudí sobre datos de un ensayo hecho en la India.</p>
<div class="card glow">
 <span class="tag coral">Anexo</span>
 <h3>Guía saudí de 2026</h3>
 <p>Aldera et al. (2026) responden, en la pregunta 3.11, sobre dolor lumbar crónico inespecífico. La guía sugiere usar PNE y priorizarla en personas con mayor riesgo de discapacidad y cronicidad. La recomendación es condicional a favor, con certeza baja. La base de evidencia es Wood y Hendrick (2019). La búsqueda de actualización no encontró estudios nuevos. No se reportaron eventos adversos.</p>
 <p>Para el contexto de Arabia Saudí, la guía la consideró probablemente no aceptable porque podría aumentar la carga de trabajo del clínico, aunque cita un ensayo de factibilidad (GLITtER) que apoyaba la aceptabilidad. La juzgó factible con formación. La telesalud podría facilitar el acceso. Hay preocupación por la equidad en zonas rurales. GLITtER no está entre las 91 fuentes de esta página: se nombra solo como lo cita la guía.</p>
</div>
<h3>Tabla 22. Signo positivo a favor de la PNE</h3>
%s
<div class="callout"><strong>Una etiqueta que no coincide con su intervalo.</strong> La fila de TSK (DM 4,72; IC 2,32 a 7,13) dice que puede haber poco o ningún efecto, y el intervalo excluye el 0. Conviene leer la fila con esa tensión, sin corregirla.</div>
<h3>Conocimiento y práctica</h3>
<div class="grid-3">
 <div class="card"><span class="tag">rNPQ</span><p>Alhowimel et al. (2021): 111 fisioterapeutas saudíes, media 6,7 ± 2,2 sobre 12. El 90%% puntuó 9 o menos.</p></div>
 <div class="card"><span class="tag">Práctica</span><p>Alshehri et al. (2020), n = 304. Usan educación al paciente el 82,0%%, electroterapia el 61,9%% y movilización o manipulación espinal el 57,8%%. Las orientaciones biomédica y biopsicosocial fueron relativamente bajas. Quienes se orientan más al modelo biopsicosocial usan más CFT. La fuente no da el puntaje de esas orientaciones.</p></div>
 <div class="card"><span class="tag">Pacientes</span><p>Asiri et al. (2026), n = 298. Cada 10 puntos de TSK se asociaron con +1,17 puntos de dolor. La kinesiofobia explicó del 11%% al 12%% de la varianza del dolor.</p></div>
</div>
<h3>Reanálisis de un ensayo indio</h3>
<p>Alalawi (2026, Umm Al-Qura) publicó análisis secundarios del ECA de Sidiq et al. (2024), hecho en la India. No son datos recogidos en Arabia Saudí. La mediación por bienestar está en Cómo funciona. Las trayectorias de recuperación, con χ²(2) = 36,25, p &lt; 0,001 y V de Cramer 0,63, son estas:</p>
%s
<p>No se encontró ningún ECA de PNE con pacientes realizado en Arabia Saudí.</p>
<h3>Mundo árabe, que no es Arabia Saudí</h3>
<p>Muhsen y Sheeha (2026) aleatorizaron a 120 estudiantes de fisioterapia en Jordania, no en Arabia Saudí. Una clase de 70 minutos dio un NNT de 2,7 para conocimiento y de 3,6 para actitudes. A los 6 meses solo se mantuvo el conocimiento. La extracción del resumen añade la diferencia ajustada de conocimiento: 2,46 (IC 1,68 a 3,24) después de la clase y 1,20 (IC 0,25 a 2,15) a los 6 meses. Muhsen et al. (2025) describen a 216 estudiantes jordanos.</p>
<p>Najem et al. (2025) es un preprint de F1000 sobre PNE culturalmente adaptada al árabe en Líbano, con 12 pacientes y 8 fisioterapeutas. Basalem et al. (2025), revisión de alcance de 38 estudios: las intervenciones educativas son las más adaptadas culturalmente (9 estudios, 33%%) y solo 6 (22%%) usaron marcos de adaptación.</p>
<p>No apareció una validación árabe del rNPQ ni del COPI-Adult. Sin ellas no se puede medir el mecanismo de conocimiento en pacientes arabófonos. La TSK-AV-11, la PCS árabe y el CSI árabe sí tienen datos, en la tabla de Dosis.</p>
<div class="callout"><strong>Propuesta de estudio, no evidencia.</strong> Un diseño a discutir: primero, validación árabe del rNPQ y del COPI-Adult. Después, un ECA piloto de factibilidad en Riad, aleatorizado y con evaluador cegado, en adultos con dolor lumbar crónico de riesgo medio o alto: PNE adaptada (unos 200 minutos en total, grupal, en árabe) más ejercicio, frente al mismo tiempo de contacto con educación biomédica y ergonómica más el mismo ejercicio. Los resultados de factibilidad serían reclutamiento, adherencia, retención y aceptabilidad. Los clínicos exploratorios serían RMDQ en árabe, NRS, TSK-AV-11, PCS árabe, CSI árabe, rNPQ, COPI y un seguimiento a 3, 6 y 12 meses, con mediación preplanificada al estilo de Cashin et al. Un piloto de factibilidad no necesita cálculo de potencia. Aquí no se propone un tamaño muestral. Un brazo con deportistas queda como opción, sin cifras.</div>
""" % (C["t22"], C["paths"])

def data():
    prim = F["primary"]
    return """
<p class="lead">El conjunto de datos de Kaggle todavía no está publicado. <strong>Kaggle dataset coming soon</strong>. Esta página no enlaza una URL de Kaggle.</p>
<p>Lo que sí está en este repositorio es una extracción derivada, preparada para esa publicación. Son cifras ya publicadas, citadas, en tres CSV. No son datos individuales de pacientes. No copian textos ni figuras de terceros. La licencia de estas tablas es CC BY 4.0. El código del generador es MIT.</p>
<div class="grid-3">
 <div class="card"><span class="tag">23 filas</span><h3>Ensayos</h3><p><a href="data/pne_trials_extraction.csv">pne_trials_extraction.csv</a>. 39 columnas. Una fila por informe. Población registrada en el archivo: 20 pacientes, 2 estudiantes y 1 grupo de deportistas.</p></div>
 <div class="card"><span class="tag">21 filas</span><h3>Efectos</h3><p><a href="data/pne_trial_effects_long.csv">pne_trial_effects_long.csv</a>. 11 columnas. Formato largo: una fila por informe, resultado y momento, cuando el resumen traía un número.</p></div>
 <div class="card"><span class="tag">42 filas</span><h3>Estimadores</h3><p><a href="data/pne_meta_estimates.csv">pne_meta_estimates.csv</a>. 17 columnas. Estimadores de revisiones y de la tabla 22, copiados para los gráficos.</p></div>
</div>
<h3>Columnas de la extracción de ensayos</h3>
%s
<h3>Columnas del archivo largo</h3>
%s
<h3>Columnas de los estimadores</h3>
%s
<p>El campo primary_result, tal como está en el archivo, vale null_result en %d filas, positive en %d, positive (borderline) en %d, no_between_group_test en %d y not_reported en %d. Es un conteo de etiquetas del archivo, no un metaanálisis. Las notas del archivo avisan que Larsen et al. (2024) prueban el ejercicio añadido a la PNE, que Adenis 2024 y Adenis 2026 son el mismo ensayo, que Maguire y Muhsen son estudiantes, que Ganapathy et al. (2026) no tiene resumen y no se extrajo nada, y que Sousa et al. (2024) se añadió desde la búsqueda de datos y no forma parte del relato de las otras secciones.</p>
<div class="callout cy"><strong>O'Keeffe y el registro Zenodo 6760585.</strong> El dataset del ensayo de terapia cognitivo funcional (O'Keeffe et al.) está en <a href="https://doi.org/10.5281/zenodo.6760585">https://doi.org/10.5281/zenodo.6760585</a> (registro <a href="https://zenodo.org/records/6760585">6760585</a>), licencia CC BY 4.0, publicado el 27 de junio de 2022. Tiene 206 filas y 145 columnas: 106 en un brazo y 100 en el otro, en línea con CFT (n = 106) frente a ejercicio y educación en grupo (n = 100). No es PNE pura: la CFT incluye reconceptualización dentro de un abordaje cognitivo funcional, y el comparador también tenía educación. Este repositorio no redistribuye ese archivo. El único enlace es el registro Zenodo.</div>
<h3>Otros datos abiertos, solo enlazados</h3>
<ul>
<li>Dehghani et al. (2026), PNE más ejercicio con Flexi-Bar, PLOS ONE. Artículo <a href="https://doi.org/10.1371/journal.pone.0355692">10.1371/journal.pone.0355692</a>. Suplemento S1, CC BY 4.0, n = 48: <a href="https://doi.org/10.1371/journal.pone.0355692.s001">10.1371/journal.pone.0355692.s001</a>. La nota de extracción dice que las medias de la tabla 2 del artículo no coinciden con el CSV del suplemento. Este sitio no redistribuye ese CSV.</li>
<li>Windsor, PNE adaptada, Figshare, CC BY 4.0, n = 21 (13 con PNE adaptada y 8 con educación general en salud). Cuatro sesiones de 15 minutos, una al mes, individuales. No es aleatorizado y el registro no enlaza un artículo verificado. <a href="https://doi.org/10.6084/m9.figshare.26018443">10.6084/m9.figshare.26018443</a> y <a href="https://doi.org/10.6084/m9.figshare.26018440">10.6084/m9.figshare.26018440</a>.</li>
<li>Understanding of Pain, Figshare, CC BY 4.0, n = 55 estudiantes de tercer año, no pacientes. NPQ y HC-PAIRS. <a href="https://doi.org/10.6084/m9.figshare.5913511">10.6084/m9.figshare.5913511</a>.</li>
</ul>
<p>La búsqueda del 30 de octubre de 2026 no encontró un dataset de pain neuroscience education en Kaggle. Malfliet et al. (2025) declaran que los datos no están disponibles. La declaración de datos de Larsen et al. (2024), RESOLVE, RESTORE, PREVENT y Chimenti et al. (2023) quedó sin verificar en esa búsqueda.</p>
""" % (chips(F["trial_cols"]), chips(F["effect_cols"]), chips(F["meta_cols"]),
      prim["null_result"], prim["positive"], prim["positive (borderline)"],
      prim["no_between_group_test"], prim["not_reported"])

def sources():
    return """
<p class="lead">91 fuentes en APA 7. Los títulos se copian como los registra Crossref, así que algunos conservan mayúsculas de título. El año es el de la edición impresa cuando existe.</p>
<p>Estado registrado en la verificación del 30 de octubre de 2026: 11 con texto completo leído, 57 abiertas con el resumen leído y 23 solo resumen. Cada DOI de esta lista resolvió en doi.org con una respuesta 302. Las tres guías sin DOI respondieron 200. El filtro de abajo necesita JavaScript. Sin él, la lista se ve completa.</p>
"""

D = dict(
lang="es", dir="ltr", loc="es-ES",
title="Educación en neurociencia del dolor · Método, evidencia y aplicación",
desc="Qué es la PNE, cómo funciona, cómo se dosifica y cómo se aplica junto al ejercicio, con las cifras publicadas y 91 fuentes.",
skip="Saltar al contenido", brand="PNE · Método", navlabel="Secciones",
n1="Qué es", n2="Mecanismo", n3="Dosis", n4="Clínica", n5="Evidencia",
n6="Novedad", n7="Guías", n8="Saudí", n9="Datos", n10="Fuentes",
kicker="Método · evidencia · aplicación",
h1a="Neurociencia del dolor.", h1b="Un método con dosis.", h1c="Y un límite claro.",
lead="La PNE cambia el concepto de dolor: de marcador de daño a señal de protección. Sola mueve poco el dolor. Añadida al ejercicio, los metaanálisis muestran alrededor de 1 punto sobre 10 a corto plazo, con certeza baja a moderada. Unos 200 minutos se asocian con superar la MCID en dolor y unos 150 en discapacidad. Frente a otra educación activa, los ensayos mejor controlados suelen ser nulos en el resultado primario. El cambio de conocimiento no se asocia con el dolor (r = -0,01).",
cta1="Empezar por el método", cta2="Ver la dosis",
k1="minutos de PNE añadida al ejercicio que superan la MCID en dolor",
k2="minutos que superan la MCID en discapacidad",
k3v="-0,01", k3="correlación entre cambio de conocimiento y dolor a corto plazo",
k4="fuentes con DOI o enlace comprobado el 30 de octubre de 2026",
kpi_note="Dolor y discapacidad: Núñez-Cortés et al., 2024, Pain. Correlación: Ram et al., 2023, 14 estudios y unas 1500 personas. El intervalo y el signo de cada cifra están en Evidencia.",
idx_t="ÍNDICE",
i1="Definición, origen y relación con la CFT.",
i2="Mediación, conocimiento y conducta.",
i3="Formatos, metáforas, minutos y medidas.",
i4="Ocho pasos para aplicarla con ejercicio.",
i5="Añadida al ejercicio, y frente a educación activa.",
i6="Lo publicado de 2024 a 2026.",
i7="JOSPT, OMS, KNGF, NICE y Arabia Saudí.",
i8="Anexo: guía, conocimiento y un reanálisis.",
i9="Extracción derivada. Kaggle dataset coming soon.",
i10="91 referencias, estado de acceso y de enlace.",
s1_num="QUÉ ES", s1_h="Una educación que cambia el concepto de dolor.", sec_what=what(),
s2_num="CÓMO FUNCIONA", s2_h="La amenaza baja. El cuestionario no alcanza.", sec_how=how(),
s3_num="CÓMO SE HACE", s3_h="Contenido, formato y minutos.", sec_dose=dose(),
s4_num="CÓMO SE APLICA", s4_h="Siempre con ejercicio o con trabajo activo.", sec_clinic=clinic(),
s5_num="EVIDENCIA", s5_h="El comparador decide el resultado.", sec_evidence=evidence(),
s6_num="NOVEDAD", s6_h="Lo que se publicó entre 2024 y 2026.", sec_new=new(),
s7_num="GUÍAS", s7_h="De grado A a sin recomendación.", sec_guides=guides(),
s8_num="ARABIA SAUDÍ", s8_h="Un anexo, no el centro del método.", sec_saudi=saudi(),
s9_num="DATOS", s9_h="La extracción está. Kaggle, todavía no.", sec_data=data(),
s10_num="FUENTES", s10_h="Referencias y estado de los enlaces.", sec_sources=sources(),
src_filter="Filtrar fuentes", src_all="Todas", src_full="Texto completo",
src_oabs="Abiertas, resumen", src_abs="Solo resumen", src_count_label="fuentes visibles",
st_full="Abierto, texto completo leído", st_oabs="Abierto, resumen leído", st_abs="Solo resumen",
st_doi="DOI: resolvió (302) el 30 de octubre de 2026",
st_http="Enlace: respondió 200 el 30 de octubre de 2026",
disc_h="Aviso.",
disc_p="Información educativa a partir de fuentes publicadas. No es consejo médico personalizado y no sustituye la valoración de un profesional de la salud. Las propuestas de dosis y de estudio están marcadas como tales.",
foot="Víctor Andrés Gómez López, fisioterapeuta deportivo. Texto y tablas: CC BY 4.0. Código: MIT. Cifras contrastadas el 30 de octubre de 2026. Página actualizada el 1 de noviembre de 2026.",
)
