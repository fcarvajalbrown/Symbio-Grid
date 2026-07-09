---
title: "Cooperación evolutiva frente al límite biofísico de un recurso de uso común: una simulación basada en agentes de una economía de intercambio"
date: "2026-07-09"
---

<!-- Target: Polis. Revista Latinoamericana (Universidad de Los Lagos), sin cargo por
     publicación (APC), indexada en Scielo/DOAJ/Redalyc/Latindex. Formato verificado
     directamente en https://polis.ulagos.cl/index.php/polis/about/submissions (2026-07-09):
     Word, tamaño carta, márgenes normales, interlineado 1.5 (citas de 40+ palabras y
     bibliografía a espacio simple), cuerpo en Century Gothic 10pt justificado, IMRAD sin
     numeración de secciones, título/resumen/palabras clave en español + inglés + portugués,
     4-5 palabras clave, citas y referencias en APA 7, extensión 7000-9000 palabras incluyendo
     bibliografía, resumen de hasta 200 palabras por idioma. Revisión ciega: el manuscrito NO
     lleva datos de autor; se agregan solo tras la aceptación, vía el formulario de envío de
     OJS. Datos de autor para ese formulario: Felipe Carvajal Brown, Universidad Politécnica
     de Madrid, Madrid, España, fcarvajalbrown@gmail.com, ORCID 0000-0002-8300-7587. Resultados
     y cifras provienen de paper/study/run_study.py y run_study_extended.py; no editar a mano. -->

## Cooperación evolutiva frente al límite biofísico de un recurso de uso común: una simulación basada en agentes de una economía de intercambio

**Resumen:** Presento Symbio-Grid, un modelo basado en agentes donde plantas y hongos
intercambian carbono y fósforo bajo reglas heredables que evolucionan por mutación y
selección: un caso generativo mínimo de una economía de intercambio que depende de un
recurso de uso común, el fósforo del suelo. Siguiendo la pregunta central de la literatura
sobre gobernanza de recursos de uso común, pregunto cuándo esta economía sostiene la
cooperación y cuándo colapsa, y si la adaptación conductual desplaza el umbral de
sostenibilidad. Barriendo la mutación, la disponibilidad de fósforo y su renovación, mido
la frecuencia de colapso y la fracción de agentes que intercambia. La cooperación no está
impuesta: partiendo de reglas aleatorias, la fracción que intercambia supera el azar y casi
se duplica entre los sobrevivientes bajo escasez. Pero ni la mutación ni el tamaño de la
grilla desplazan el umbral de colapso, fijado solo por la renovación del recurso, cercana a
cero: la dinámica biofísica del recurso acota la sostenibilidad, con independencia de cuánta
flexibilidad conductual tengan quienes lo explotan, un resultado que dialoga con el marco de
Ostrom sobre sistemas socioecológicos. La señal de selección solo es visible en el
comportamiento expresado, no en el promedio de la tabla de reglas.

**Palabras clave:** Modelado basado en agentes; evolución de la cooperación; recursos de
uso común; economía de intercambio; gobernanza de recursos.

**English title:** Evolutionary cooperation against the biophysical limit of a common-pool
resource: an agent-based simulation of a trading economy

**Abstract:** I present Symbio-Grid, an agent-based model in which plant and fungal agents
trade carbon and phosphorus under heritable rules that evolve by mutation and selection: a
minimal generative case of a trading economy that depends on a common-pool resource, soil
phosphorus. Following the central question of the common-pool resource governance
literature, I ask when this economy sustains cooperation and when it collapses, and whether
behavioral adaptability shifts the sustainability threshold. Sweeping mutation, phosphorus
availability, and its renewal rate, I measure collapse frequency and the fraction of agents
that trade. Cooperation is not imposed: starting from random rules, the trading fraction
rises above chance and nearly doubles among survivors under scarcity. Yet neither mutation
nor grid size shifts the collapse threshold, which is set solely by resource renewal, near
zero: the resource's own biophysical dynamics bound sustainability, regardless of how
behaviorally flexible its exploiters are, a result that speaks directly to Ostrom's
social-ecological systems framework. The selection signal is visible only in expressed
behavior, not in the genotype-wide average.

**Keywords:** Agent-based modeling; evolution of cooperation; common-pool resources;
resource-trading economy; resource governance.

**Título em português:** Cooperação evolutiva perante o limite biofísico de um recurso de
uso comum: uma simulação baseada em agentes de uma economia de troca

**Resumo:** Apresento o Symbio-Grid, um modelo baseado em agentes em que plantas e
fungos trocam carbono e fósforo segundo regras hereditárias que evoluem por mutação e
seleção: um caso generativo mínimo de uma economia de troca que depende de um recurso de
uso comum, o fósforo do solo. Seguindo a pergunta central da literatura sobre governança de
recursos de uso comum, pergunto quando essa economia sustenta a cooperação e quando
colapsa, e se a adaptação comportamental desloca o limiar de sustentabilidade. Variando
sistematicamente a mutação, a disponibilidade de fósforo e sua renovação, meço a
frequência de colapso e a fração de agentes que troca. A cooperação não é imposta: partindo
de regras aleatórias, a fração que troca supera o acaso e quase duplica entre os
sobreviventes sob escassez. Porém, nem a mutação nem o tamanho da grade deslocam o limiar de
colapso, fixado apenas pela renovação do recurso, próxima de zero: a dinâmica biofísica do
recurso limita a sustentabilidade, independentemente da flexibilidade comportamental de quem
o explora, em diálogo direto com o referencial de Ostrom sobre sistemas socioecológicos. O sinal de
seleção só é visível no comportamento efetivamente expresso, não na média da tabela de
regras.

**Palavras-chave:** Modelagem baseada em agentes; evolução da cooperação; recursos de uso
comum; economia de troca; governança de recursos.

## Introducción

### El problema de los recursos de uso común y la cooperación

Toda comunidad que depende de un recurso compartido y agotable enfrenta la misma pregunta:
¿bajo qué condiciones sus miembros sostienen una práctica cooperativa de uso, y bajo cuáles
la abandonan hasta que el recurso colapsa? Hardin (1968) planteó esta pregunta como una
tragedia casi inevitable. En su lectura, actores racionales sobreexplotan un recurso
compartido: el costo de la sobreexplotación se reparte entre todos, pero el beneficio de
extraer un poco más lo captura solo quien extrae. Ostrom (1990) mostró lo contrario.
Comunidades reales de pescadores, regantes y usuarios de bosques sostienen sus recursos de
uso común durante generaciones, mediante instituciones que ellas mismas diseñan: reglas de
acceso, mecanismos de monitoreo y sanción graduada, y fronteras claras sobre quién pertenece
al grupo de usuarios. Ese hallazgo desplazó la pregunta de si la
cooperación en torno a un recurso compartido es posible a bajo qué condiciones emerge y se
sostiene, y qué papel cumplen las reglas mismas, a diferencia del recurso, en esa
sostenibilidad. Ostrom (2009) formalizó después esa pregunta en un marco de sistemas
socioecológicos que distingue explícitamente el sistema de recursos (su tamaño, su
productividad, su tasa de renovación) del sistema de gobernanza (las reglas que los usuarios
adoptan), y sostiene que la sostenibilidad del conjunto depende de la interacción entre
ambos subsistemas, no de uno solo.

Un supuesto que suele quedar implícito en gran parte de esa literatura es que las reglas de
uso son diseñadas deliberadamente por actores que negocian, se comunican y aprenden de la
experiencia colectiva. Ese es el caso en las comunidades humanas que Ostrom documentó. Pero
la pregunta de fondo, si la cooperación en torno a un recurso compartido puede sostenerse y
bajo qué condiciones colapsa, no es exclusiva de sistemas con deliberación. En ecología, la
simbiosis micorrícica entre plantas y hongos ofrece un caso extremo del mismo problema sin
ninguna de esas condiciones: la planta entrega carbono fotosintético y el hongo entrega
fósforo extraído del suelo, un intercambio que Simard et al. (2012) describen explícitamente
en términos de mercado, cada socio comercia el recurso que al otro le falta. Ninguno de los
dos socios delibera, negocia ni diseña reglas; el comportamiento de intercambio, si existe,
está codificado genéticamente y solo puede cambiar por mutación y selección a lo largo de
generaciones. Van 't Padje et al. (2021) muestran, mediante experimento y modelamiento, que
los hongos ajustan el "precio" al que comercian fósforo cuando la disponibilidad del recurso
sufre caídas y auges abruptos, de modo que los términos de intercambio responden a la
escasez incluso sin ningún tipo de institución que los fije. Más recientemente, Grasso et al.
(2025) presentan un modelo de coevolución del comercio de recursos entre planta y hongo
micorrícico en el que las estrategias de intercambio coevolucionan y el modelo reproduce
estabilidad de la mutualidad, extinción y parasitismo transitorio a través de
retroalimentación de aptitud (fitness feedback). Estos modelos establecen que los términos y
la estabilidad del intercambio dependen del valor relativo de los recursos y de la selección,
pero no preguntan directamente si la cooperación observada está acotada por la capacidad de
adaptación conductual de la población o por la dinámica del propio sistema de recursos, la
pregunta que en la literatura de gobernanza de recursos de uso común distingue el sistema de
gobernanza del sistema de recursos.

Una segunda tradición, en ciencias de la complejidad y ciencias sociales computacionales,
estudia la evolución de la cooperación de manera abstracta, sin referencia a ningún sistema
biológico particular. Axelrod (1984) lo probó con torneos computacionales del dilema del
prisionero iterado. Estrategias condicionales y basadas en reciprocidad, como "toma y daca"
(tit-for-tat), pueden invadir y sostenerse en una población de estrategias egoístas cuando
las interacciones se repiten. Nowak (2006) sintetizó cinco mecanismos que la
literatura posterior identificó como suficientes para que la selección natural favorezca la
cooperación en distintos contextos: selección de parentesco, reciprocidad directa,
reciprocidad indirecta, reciprocidad de red y selección de grupo. Estos mecanismos son
formulaciones generales, aplicables en principio tanto a poblaciones de organismos biológicos
como a poblaciones de estrategias artificiales, y han sido la base de una enorme literatura
de simulación evolutiva de la cooperación mediante juegos espaciales, en la que las
estrategias se codifican como tablas de decisión o cadenas de bits que mutan y se propagan
por imitación o reproducción. Epstein y Axtell (1996), con su modelo Sugarscape, fundaron una
forma distinta de hacer ciencia social: en lugar de deducir propiedades agregadas a partir de
supuestos sobre actores racionales, generan esas propiedades desde abajo hacia arriba, a
partir de agentes simples con reglas de decisión heredables, y leen las regularidades que
emergen, migración, comercio, desigualdad, guerra, como explicaciones candidatas de
fenómenos sociales. Ese programa, que Epstein llamó "ciencia social generativa", es
precisamente el que permite tratar un sistema no humano, como una economía de intercambio
entre plantas y hongos, como un caso de estudio legítimo para preguntas de ciencia social:
lo que se generaliza no es el organismo, sino el mecanismo, la estructura mínima de agentes,
reglas heredables y un recurso compartido que basta para que la cooperación emerja, se
sostenga o colapse.

En el ámbito latinoamericano, Vélez Torres (2019) revisa el estado del arte del modelamiento
y la simulación basada en agentes en ciencias sociales y lo presenta como una tercera vía
para hacer ciencia, cuyo potencial no reside en la predicción sino en la comprensión de los
procesos fundamentales de fenómenos complejos: estructuras sociales y comportamientos
grupales que emergen de la interacción de agentes heterogéneos bajo reglas de decisión
simples y racionalidad limitada. Esa caracterización describe con precisión el tipo de
modelo que presento aquí, y la propia revista que publicó ese estado del arte es evidencia
de que la comunidad de ciencias sociales latinoamericana reconoce la modelación basada en
agentes, incluida la que usa sustratos no humanos para poner a prueba mecanismos generales,
como una herramienta metodológica legítima y no como una curiosidad computacional ajena a
sus preguntas.

Lo que ninguna de estas dos tradiciones, la de los mercados biológicos micorrícicos y la de
la evolución computacional de la cooperación, pone a prueba directamente es la pregunta que
Ostrom formalizó para sistemas humanos: si la sostenibilidad de un recurso de uso común está
acotada por la capacidad de adaptación conductual de quienes lo usan, o por la dinámica
biofísica del recurso mismo, independientemente de cuánto varíe el comportamiento. En
sistemas humanos esa pregunta es difícil de aislar porque las instituciones y el recurso
cambian juntos y de manera correlacionada. Un modelo generativo mínimo, donde el "sistema de
gobernanza" se reduce a una tasa de mutación que controla cuánto varía el comportamiento
heredado, y el "sistema de recursos" se reduce a una tasa de renovación del fósforo del
suelo, permite variar ambos de manera independiente y preguntar directamente cuál de los dos
gobierna el umbral de colapso.

### El modelo Symbio-Grid y preguntas de investigación

Este artículo presenta *Symbio-Grid*, un modelo espacial basado en agentes en el que el
comportamiento de intercambio de cada agente no está fijo, sino codificado en una tabla de
reglas que mapea la percepción local del agente a una acción, y que se hereda con mutación
cuando el agente se reproduce. La cooperación nunca está impuesta: debe evolucionar. Uso
el modelo para responder tres preguntas. Primero, ¿cómo afecta la tasa de mutación, como
aproximación a la capacidad de adaptación conductual de la población, a que emerja o colapse
una economía de intercambio estable, y cambia el nivel de cooperación que evoluciona?
Segundo, ¿cuán robusta es la mutualidad a la disponibilidad del recurso de uso común y, en
particular, a la tasa a la que se renueva? Tercero, ¿está la cooperación efectivamente
seleccionada, y en qué situaciones la expresan los agentes?

Las contribuciones de este artículo son: (i) un modelo espacial basado en agentes, abierto y
reproducible, de una economía de intercambio evolutiva sobre un recurso de uso común,
descrito según el protocolo ODD; (ii) evidencia directa de que el umbral de sostenibilidad de
ese recurso está fijado por su propia tasa de renovación y no se desplaza con la capacidad de
adaptación conductual de la población, un resultado que dialoga con la distinción de Ostrom
(2009) entre sistema de recursos y sistema de gobernanza; (iii) evidencia de que la
cooperación es efectivamente seleccionada a partir de estrategias aleatorias, con mayor
fuerza bajo escasez, en línea con la teoría de mercados biológicos y con los mecanismos de
evolución de la cooperación descritos por Nowak (2006); y (iv) una advertencia metodológica
para la simulación social de estrategias evolutivas: la señal de selección solo es visible en
el comportamiento efectivamente expresado, no en el promedio de toda la tabla de reglas. El
resto del artículo describe el modelo y el diseño experimental (Métodos), reporta los
resultados (Resultados) y discute su interpretación, sus límites y su relación con la
literatura sobre gobernanza de recursos de uso común (Discusión), antes de concluir
(Conclusiones).

## Métodos

### Visión general y propósito

El modelo está implementado sobre el framework Mesa (ter Hoeven et al., 2025; Masad y Kazil,
2015) y se describe aquí siguiendo la convención ODD (Overview, Design concepts, Details;
Grimm et al., 2020). Su propósito es estudiar cuándo una mutualidad de intercambio de
recursos, evolutiva y espacialmente explícita entre plantas y hongos, alcanza un equilibrio
estable o colapsa, bajo condiciones variables de mutación y estrés de recursos, y si ese
umbral está determinado por la conducta de la población o por la dinámica del recurso.

### Entidades, variables de estado y escalas

Dos tipos de agentes habitan una grilla toroidal `MultiGrid` de ancho W y alto H. Una
**planta** es estacionaria y posee carbono y fósforo (cada uno un número real en [0, 20]). Un
**hongo** es micelial y también posee carbono y fósforo. El entorno mantiene un campo de
fósforo del suelo, un escalar por celda en [0, 10]: el recurso de uso común del sistema. Un
paso de tiempo equivale a una generación.

Cada agente posee una **tabla de reglas**: un arreglo de 64 posiciones sobre las tres
acciones disponibles para su especie (una planta puede INTERCAMBIAR, BROTAR o esperar; un
hongo puede INTERCAMBIAR, EXPANDIRSE o esperar). En cada paso el agente forma un índice
entero entre 0 y 63 a partir de una percepción discretizada de su estado local y lee la
acción correspondiente. El índice empaqueta tres campos de dos bits: el nivel propio de
carbono, el nivel propio de fósforo (cada uno agrupado en cuatro niveles al dividir por cinco
y limitar en tres), y el número de vecinos relevantes (socios adyacentes de la otra especie,
limitado en tres). Escribiendo estos campos como $c$, $p$ y $n$, el índice es
$(c \ll 4) \mathbin{|} (p \ll 2) \mathbin{|} n$. Debido a que la percepción usa solo estos
rasgos toscos, el número efectivo de estados *distintos* que un agente realmente encuentra es
pequeño, un hecho que resulta relevante para el análisis de Resultados.

### Proceso y programación

En cada paso, todos los agentes actúan en orden aleatorio siguiendo un ciclo de
percibir–deliberar–actuar: perciben su vecindario, indexan su tabla de reglas para
seleccionar una acción, y la ejecutan. Luego se remueven los agentes muertos, el fósforo del
suelo se repone, y avanza el contador de generación. Toda la aleatoriedad proviene de un
único generador con semilla, de modo que cada corrida es idéntica byte a byte bajo su
semilla.

Como ilustración concreta, considérese una planta con carbono 11 y fósforo 3 con dos hongos
en su vecindario de Moore. En el paso de percepción registra sus recursos y sus dos socios;
en el paso de deliberación agrupa carbono en el nivel 2, fósforo en el nivel 0 y socios en 2,
formando el índice $(2 \ll 4) \mathbin{|} (0 \ll 2) \mathbin{|} 2 = 34$ y lee la entrada 34 de
su tabla de reglas, por ejemplo INTERCAMBIAR. En el paso de acción primero fotosintetiza y
paga su costo de fósforo, luego, como hay un socio presente y la acción es INTERCAMBIAR,
entrega carbono a uno de los hongos y recibe fósforo a cambio. Una planta hermana con la
misma tabla de reglas pero sin vecino fúngico leería una entrada distinta y, aunque esa
entrada fuera también INTERCAMBIAR, no podría actuar sobre ella. La selección opera entonces
solo sobre las entradas que las circunstancias de cada agente efectivamente lo llevan a leer,
lo cual es el núcleo del problema de medición discutido en la Discusión.

### Conceptos de diseño

*Emergencia:* una economía de intercambio persistente (o su colapso) no está programada,
sino que surge de intercambios locales y de la selección. *Adaptación:* la descendencia
hereda la tabla de reglas del progenitor con mutación por locus. *Objetivo:* supervivencia
implícita, ya que los agentes que no consiguen su recurso limitante mueren y no dejan
descendencia. *Percepción:* un agente percibe su propio carbono/fósforo, los agentes vecinos
y, en el caso de los hongos, el fósforo del suelo en su vecindario de Moore. *Interacción:*
intercambio bilateral de recursos entre planta y hongo adyacentes. *Estocasticidad:*
ubicación, inicialización/mutación de tablas de reglas, y elecciones entre opciones
equivalentes. *Observación:* se recolectan poblaciones y recursos por paso, y las tablas de
reglas del estado final.

### Inicialización

N_p plantas y N_f hongos se ubican con los hongos sembrados junto a plantas de modo que el
intercambio sea posible desde el inicio. El fósforo del suelo se extrae de una distribución
Uniforme(0, 10) escalada por un parámetro de densidad. Las plantas comienzan con carbono 5 y
fósforo 5; los hongos con carbono 3 y fósforo 5. Todas las tablas de reglas se inicializan de
manera uniformemente aleatoria.

### Submodelos

*Metabolismo.* Una planta fotosintetiza, ganando 1.0 de carbono (con tope 20), y consume
$d_p$ de fósforo (parámetro `plant_p_decay`). Un hongo consume $d_c$ de carbono (parámetro
`fungi_c_decay`) y forrajea fósforo: extrae hasta $u$ unidades (parámetro `fungi_uptake`) de
las celdas de su vecindario de Moore, incluida la propia, tomando primero de las celdas más
ricas, lo que representa a las hifas alcanzando el suelo circundante. Carbono y fósforo tienen
tope 20.

*Intercambio.* Si la acción elegida por una planta es INTERCAMBIAR y hay al menos un hongo
adyacente, elige uno y el par intercambia cantidades iguales del recurso que a cada uno le
falta: la planta entrega carbono y recibe fósforo, el hongo entrega fósforo y recibe carbono.
La cantidad intercambiada es $\min(0.25 \times \text{reserva del dador}, 2.0)$ y solo se
ejecuta si quien recibe posee lo suficiente del recurso que debe entregar a cambio, de modo
que un intercambio conserva el carbono total y el fósforo total entre los dos agentes. Los
hongos intercambian simétricamente cuando su acción es INTERCAMBIAR.

*Reproducción.* Una planta cuya acción es BROTAR, o un hongo cuya acción es EXPANDIRSE, se
reproduce si existe una celda vecina vacía y posee recursos suficientes (carbono sobre 12 y
fósforo sobre 6 para plantas; fósforo sobre 6 y carbono sobre 4 para hongos). La cría se
ubica en la celda vacía, hereda una copia de la tabla de reglas del progenitor con cada
entrada re-aleatorizada independientemente con probabilidad igual a la tasa de mutación, y
recibe el 40% de cada recurso del progenitor, que este último pierde.

*Mortalidad.* Un agente muere y se remueve cuando su recurso limitante (fósforo para
plantas, carbono para hongos) llega a cero.

*Entorno.* Después de que todos los agentes actuaron y se removió a los muertos, cada celda
de suelo regenera fósforo en $r$ (parámetro `phosphorus_regen`), con tope 10.

### Parámetros

La Tabla 1 lista los parámetros por defecto, que se mantienen fijos salvo cuando el
parámetro es objeto de un barrido.

**Tabla 1.** Parámetros por defecto del modelo.

| Parámetro | Símbolo | Valor por defecto | Significado |
|---|---|---|---|
| Ancho × alto de la grilla | W × H | 60 × 40 | tamaño toroidal de la grilla |
| Plantas / hongos iniciales | | 80 / 60 | poblaciones de partida |
| Tamaño de la tabla de reglas | | 64 | estados perceptuales por agente |
| Tasa de mutación | | 0.1 | re-aleatorización por entrada en la reproducción |
| Densidad de fósforo | | 0.5 | escala el fósforo inicial del suelo |
| Renovación de fósforo | r | 0.05 | fósforo añadido por celda por paso |
| Captación fúngica | u | 1.2 | fósforo máximo que un hongo forrajea por paso |
| Decaimiento de fósforo en planta | d_p | 0.15 | fósforo que una planta consume por paso |
| Decaimiento de carbono en hongo | d_c | 0.1 | carbono que un hongo consume por paso |

### Implementación y reproducibilidad

El modelo está implementado en Python sobre el framework Mesa (ter Hoeven et al., 2025).
Toda la estocasticidad (ubicación inicial, inicialización de tablas de reglas, mutación y la
elección entre opciones empatadas) se extrae de un único generador aleatorio inicializado una
vez por corrida, de modo que una semilla y configuración dadas reproducen una corrida
exactamente, hasta la salida de métricas idéntica byte a byte. Una corrida se ejecuta de
manera interactiva, para observación, o en modo headless mediante un ejecutor por lotes que
registra series de población y recursos por paso, una instantánea de la tabla de reglas de
cada agente sobreviviente, y un manifiesto que captura la configuración, la semilla y la
versión del código. Este determinismo es lo que permite que el mismo modelo sirva tanto para
la exploración como para la experimentación controlada sin que ambas diverjan, y hace que
cada resultado de este artículo sea regenerable desde los scripts que lo acompañan.

### Diseño experimental

Todos los experimentos usan la grilla e poblaciones iniciales por defecto y corren durante
300 generaciones con 10 semillas aleatorias cada uno; una corrida se registra como
*colapsada* si alguna de las dos especies se extingue. Para cada corrida registro el
resultado de colapso y la población final total. Para medir la selección de la cooperación
uso una métrica *expresada*: la fracción de agentes vivos que efectivamente elige la
acción INTERCAMBIAR en la situación en la que se encuentra, registrada por paso. Como una
tabla de reglas inicializada al azar selecciona cualquiera de las tres acciones con
probabilidad igual, un valor sobre 1/3 indica que la selección ha enriquecido el
comportamiento de intercambio. (Evito deliberadamente promediar INTERCAMBIAR sobre las 64
entradas de la tabla de reglas completa, porque los agentes visitan solo unos pocos estados,
de modo que la mayoría de entradas nunca expresadas deriva neutralmente y enmascara la señal;
véase la Discusión.)

- **Experimento A (tasa de mutación):** barrido de la tasa de mutación por locus sobre
  {0.0, 0.05, 0.1, 0.2, 0.35, 0.5}.
- **Experimento B (disponibilidad de fósforo):** barrido de la densidad de fósforo del suelo
  sobre {0.1, 0.15, 0.2, 0.3, 0.5, 0.7}.
- **Experimento C (renovación de fósforo):** barrido de la tasa de regeneración de fósforo
  del suelo sobre {0.0, 0.0025, 0.005, 0.0075, 0.01, 0.02, 0.05} para ubicar el límite de
  resiliencia.
- **Experimento D (interacción mutación × renovación):** factorial completo de tasa de
  mutación {0.0, 0.1, 0.35} y tasa de regeneración {0.0, 0.0025, 0.005, 0.0075, 0.01} para
  probar si la mutación, como aproximación de la capacidad de adaptación conductual, desplaza
  el umbral de resiliencia.
- **Experimento E (robustez a la escala de la grilla):** repetición del barrido de
  regeneración {0.0, 0.005, 0.02, 0.05} en grillas de 40 × 25, 60 × 40 y 80 × 50 (8 semillas,
  200 generaciones) para verificar que el umbral de resiliencia no es un artefacto de una
  sola escala.
- **Experimento F (mecanismo de la selección):** para diez corridas en la configuración por
  defecto, en la generación 300 se recalcula la acción elegida por cada agente sobreviviente
  y se divide la población según si tiene un socio de intercambio actualmente adyacente, para
  probar si el comportamiento seleccionado es intercambio *condicional* (intercambiar cuando
  hay un socio presente).

Los experimentos A–C son reproducibles mediante `paper/study/run_study.py` y D–F mediante
`paper/study/run_study_extended.py`; los valores de los parámetros, las semillas y los
recuentos de generaciones quedan registrados allí y en el manifiesto de cada corrida.

## Resultados

Todos los valores son promedios sobre 10 semillas por punto de parámetro; "±" indica una
desviación estándar de la población final total.

### Tasa de mutación (Experimento A)

Ninguna corrida colapsó en ninguna tasa de mutación entre 0.0 y 0.5. La población final
declinó de manera moderada y monótona con la mutación, de 713 ± 128 individuos a tasa 0.0 a
592 ± 72 a tasa 0.5, una carga de mutación que reduce la población sin desestabilizarla. El
intercambio expresado subió de alrededor de 0.25 en etapas tempranas (generación 5) a
0.357–0.388 hacia la generación 300, por sobre la línea base aleatoria de 1/3 en todas las
tasas de mutación, lo que indica que la selección enriquece el comportamiento de intercambio
incluso a tasa 0.0 (selección actuando sobre la variación presente en las tablas de reglas
iniciales aleatorias). La fracción de intercambio en generaciones tardías aumentó con la tasa
de mutación, alcanzando un máximo de 0.388 a tasa 0.35, de modo que mayor mutación produjo
algo más de cooperación expresada junto con menos individuos.

### Disponibilidad de fósforo (Experimento B)

Ninguna corrida colapsó a través de densidades de fósforo del suelo entre 0.1 y 0.7. La
población final escaló con la disponibilidad de recursos, de manera aproximadamente lineal,
de 464 ± 83 a densidad 0.1 a 748 ± 96 a densidad 0.7, de modo que la oferta de fósforo fija
la capacidad de carga. El intercambio expresado se mantuvo moderadamente por sobre la línea
base (alrededor de 0.34–0.38) sin una dependencia fuerte de la densidad.

### Umbral de resiliencia (Experimento C)

La mutualidad colapsó solo cuando el ingreso renovable de fósforo estuvo cerca de cero: 50%
de las corridas colapsaron a tasa de regeneración 0.0 y 30% a 0.0025, pero ninguna corrida
colapsó a 0.005 o más. Eso marca un umbral de resiliencia abrupto cerca de 0.005 unidades por
celda por paso. La población final subió abruptamente con la renovación, de 8 ± 3
sobrevivientes a tasa 0.0 a 657 ± 82 a tasa 0.05. Notablemente, el intercambio expresado fue
más alto bajo escasez: los sobrevivientes en el borde de supervivencia (tasas 0.005–0.0075)
intercambiaron a alrededor de 0.64, casi el doble de la línea base, declinando hacia 0.36 a
medida que el fósforo se volvió abundante. La escasez del recurso intensificó así la
selección de la cooperación entre los sobrevivientes.

### Cooperación en el tiempo

Para una corrida representativa, la fracción de agentes que elige intercambiar comenzó bajo
la línea base aleatoria y se estableció moderadamente por sobre ella dentro de
aproximadamente cincuenta generaciones, manteniéndose allí después.

### Interacción mutación × renovación (Experimento D)

El umbral de resiliencia es esencialmente independiente de la tasa de mutación. Bajo
renovación cero, entre aproximadamente la mitad y dos tercios de las corridas colapsaron en
cada tasa de mutación (tasas de colapso de 0.6, 0.5 y 0.7 a tasas 0.0, 0.1 y 0.35), sin un
ordenamiento consistente según la mutación. En la tasa de renovación límite de 0.0025 el
resultado fue ruidoso y parcial (0 a 0.3 de colapso), y en tasas de renovación de 0.005 o
más ninguna corrida colapsó en ninguna tasa de mutación. La mutación, por lo tanto, no
desplaza el límite de colapso, que está gobernado por la renovación del fósforo y no por la
tasa de variación conductual. Este es el resultado central para la pregunta de gobernanza de
recursos de uso común planteada en la Introducción: variar la capacidad de adaptación
conductual de la población, manteniendo todo lo demás fijo, no cambia el punto en el que el
sistema colapsa.

### Robustez a la escala de la grilla (Experimento E)

Corrido hasta 400 generaciones, el umbral de resiliencia aparece en todas las escalas de
grilla. Bajo renovación cero, esencialmente todas las corridas colapsaron (tasa de colapso
1.0 en 40 × 25 y 60 × 40, y 0.83 en 80 × 50); a la renovación más alta (0.05) ninguna
colapsó en ninguna escala. La transición se ubica en el rango 0.0025 a 0.005 para las tres
grillas, con grillas más grandes algo más resilientes cerca del límite: a renovación 0.005 la
tasa de colapso bajó de 0.50 en 40 × 25 a 0.17 en 60 × 40 a 0.00 en 80 × 50. El umbral es,
por lo tanto, un rasgo robusto a través de escalas y no un artefacto de un solo tamaño de
grilla, aunque su posición exacta se desplaza levemente con el área. Comparado con el
Experimento C, que usó un horizonte de 300 generaciones, esto también muestra que el colapso
bajo renovación cero es progresivo: más corridas han colapsado hacia la generación 400 que
hacia la generación 300, porque la reserva finita de suelo se agota gradualmente.

### Mecanismo de la cooperación seleccionada (Experimento F)

Pregunto si el intercambio seleccionado es *condicional* a la presencia de un socio.
Entre los agentes sobrevivientes en la generación 300, la fracción que eligió intercambiar
fue 0.365 cuando un socio de intercambio estaba adyacente (n = 6232) y 0.355 cuando ninguno
lo estaba (n = 335): ambos apenas por sobre el nivel de azar de 1/3, y casi iguales.
Contrario a lo esperado, el aumento seleccionado en el intercambio es entonces leve y en gran
medida *incondicional* bajo condiciones benignas por defecto. La evolución empuja a la
población hacia intercambiar algo más que el azar, pero no produce aquí una estrategia
marcadamente condicional al socio. Leído junto con el resultado de escasez del Experimento C,
donde el intercambio expresado alcanzó alrededor de 0.64, esto sugiere que una respuesta de
intercambio más pronunciada y más fuertemente seleccionada emerge solo cuando los recursos
escasean.

## Discusión

### Un umbral fijado por el recurso

Tres observaciones se destacan. Primero, la mutualidad de intercambio es robusta: persiste a
través de un amplio rango de tasas de mutación y disponibilidades de fósforo, y colapsa solo
cuando el ingreso renovable de fósforo cae esencialmente a cero. Esto es intuitivo en
retrospectiva. Sin renovación, el único fósforo del sistema es la reserva finita inicial del
suelo, que los agentes extraen y consumen hasta agotarla. Sin embargo, la transición es
abrupta, y basta 0.005 unidades por paso para sostener el ecosistema indefinidamente. El
umbral está gobernado específicamente por la renovación: no se desplaza con la tasa de
mutación (Experimento D), y reaparece en una ubicación similar a través de las escalas de
grilla que evalúo (Experimento E), con grillas más grandes solo levemente más resilientes
cerca del límite. En otras palabras, si la economía sobrevive lo determina principalmente la
capacidad del entorno de reponer el recurso limitante, no la velocidad con que varía la
conducta ni, en primer orden, el tamaño del mundo.

Este resultado se lee de manera directa contra el marco de sistemas socioecológicos de Ostrom
(2009), que distingue el sistema de recursos, con su propia dinámica de renovación, del
sistema de gobernanza, las reglas que adoptan quienes lo usan. En este modelo, la tasa de
mutación es la aproximación más directa a la capacidad de adaptación conductual de una
población: una tasa alta permite que la población explore más rápido el espacio de posibles
tablas de reglas, de manera análoga, aunque no idéntica, a como una comunidad con reglas de
uso más flexibles o mejor información podría ajustar más rápido su comportamiento de
extracción. El Experimento D muestra que esa capacidad de adaptación, por sí sola, no basta
para mover el punto de colapso ni un ápice. Si la renovación del recurso cae por debajo del
umbral, ninguna cantidad de variación conductual evita el colapso, y tampoco lo evita
ninguna estrategia de intercambio posible dentro del espacio que el modelo permite explorar.
Esto no contradice a Ostrom, cuyas comunidades de estudio de caso sí lograban ajustar sus
tasas de extracción por debajo de la tasa de renovación del recurso mediante reglas
deliberadas de acceso y sanción; lo que el modelo aísla es que ese ajuste depende de que la
tasa de renovación deje margen para alguna regla sostenible, no de la sofisticación de la
regla misma. Cuando ese margen no existe, como en la condición de renovación cercana a
cero, ni la deliberación humana ni la selección natural ciega tienen una regla que ofrecer:
el límite es biofísico, no institucional.

La transición abrupta a renovación cero se lee de manera natural como una transición crítica.
El sistema tiene dos regímenes de largo plazo cualitativamente distintos, una economía de
intercambio poblada y autosostenida, y una grilla vacía y agotada, y una banda estrecha de
tasas de renovación separa ambos. La transición es además dependiente de la trayectoria y
efectivamente irreversible dentro de una corrida: una vez que la reserva finita de suelo se
extrae por debajo de lo que la población necesita, no existe estrategia de intercambio que
pueda recuperarla, porque el recurso mismo desapareció en lugar de estar simplemente mal
distribuido. Esto distingue el colapso de una falla conductual; es un punto de inflexión por
agotamiento del recurso. La naturaleza progresiva del colapso bajo renovación cero, visible
en la diferencia entre los horizontes de 300 y 400 generaciones, es la aproximación lenta a
ese punto de inflexión a medida que la reserva se agota. Este tipo de comportamiento umbral,
en el que un impulsor ambiental que cambia lentamente produce un cambio de régimen abrupto,
es un tema recurrente en el estudio de la resiliencia de sistemas ecológicos y otros sistemas
complejos, y Symbio-Grid lo reproduce a partir de reglas puramente locales.

### La selección genera la cooperación observada

Segundo, la cooperación está seleccionada y no asumida. Partiendo de tablas de reglas
aleatorias, la fracción de agentes que efectivamente elige intercambiar sube por sobre el
nivel esperado por azar y se mantiene allí. El efecto es modesto bajo condiciones benignas
pero pronunciado bajo escasez: en el borde de la viabilidad los sobrevivientes son fuertemente
cooperativos, intercambiando a aproximadamente el doble de la tasa de azar. El análisis de
mecanismo (Experimento F) matiza este cuadro: bajo condiciones benignas por defecto, el
enriquecimiento del intercambio es solo leve y no está fuertemente condicionado a la presencia
de un socio, de modo que la población evolucion a una propensión leve y en gran medida
incondicional a intercambiar, en lugar de una regla finamente ajustada y condicional al
socio. La respuesta abrupta, cercana al doble, aparece específicamente bajo escasez. Este
patrón es consistente con la visión de mercado biológico según la cual el recurso de un socio
se vuelve más valioso a medida que escasea (van 't Padje et al., 2021) y hace eco, en un
entorno evolutivo espacial, del resultado de estabilidad por retroalimentación de aptitud de
modelos recientes de coevolución del comercio (Grasso et al., 2025). También dialoga con los
mecanismos de Nowak (2006): aquí no hay reciprocidad indirecta ni selección de grupo
explícitas, pero la estructura espacial de la grilla, que hace que los socios de intercambio
sean vecinos persistentes generación tras generación, opera como una forma de reciprocidad de
red, uno de los cinco mecanismos que Nowak identifica como suficientes para que la selección
favorezca la cooperación, y ofrece una explicación candidata de por qué la cooperación emerge
aquí sin que ningún agente reconozca ni recuerde a su socio.

### Una advertencia metodológica para la simulación social de estrategias evolutivas

Tercero, hay una advertencia metodológica. Promediar la acción INTERCAMBIAR sobre toda la
tabla de reglas de 64 entradas da un valor indistinguible de la línea base aleatoria de 1/3,
lo que sugeriría erróneamente que no ocurre selección alguna. La señal aparece solo cuando el
intercambio se mide sobre los estados que los agentes efectivamente visitan, porque las
muchas entradas nunca expresadas de la tabla de reglas derivan neutralmente y diluyen el
promedio. Quienes analizan modelos basados en agentes con estrategias evolutivas, sea en
ecología, en ciencias de la complejidad o en simulación social, deberían medir el
comportamiento expresado y no el promedio del genotipo completo. Esta advertencia es
relevante más allá de este modelo específico: cualquier simulación social en la que las
estrategias se codifiquen como estructuras de decisión ricas, tablas, árboles, redes,
mientras que las circunstancias efectivamente encontradas por los agentes sean un subconjunto
pequeño de todas las posibles, corre el mismo riesgo de subestimar la selección si mide sobre
la estructura completa en lugar de sobre el comportamiento realizado.

### El uso del modelo como caso generativo y sus límites

El carácter del modelo como caso generativo, en el sentido de Epstein y Axtell (1996), también
condiciona cómo deben leerse estos resultados. Symbio-Grid no pretende describir con
precisión la ecología de la simbiosis micorrícica, ni menos aún trasladar sus cifras
literalmente a una comunidad humana que gestiona un recurso de uso común. Lo que ofrece es
una estructura mínima, agentes con reglas heredables, un recurso compartido con una tasa de
renovación explícita, e intercambio bilateral, en la que se puede aislar el efecto de variar
independientemente la capacidad de adaptación conductual y la dinámica del recurso, algo
difícil de lograr en los estudios de caso empíricos que fundan la literatura de gobernanza de
recursos de uso común, donde ambos factores suelen cambiar de manera correlacionada.
Vélez Torres (2019) describe precisamente esta clase de modelo, agentes heterogéneos con
reglas simples y racionalidad limitada cuya interacción genera estructuras y comportamientos
agregados, como una de las contribuciones distintivas que la simulación basada en agentes
ofrece a las ciencias sociales: no predicción cuantitativa, sino comprensión de mecanismos.
Symbio-Grid además carece, deliberadamente, de todo lo que en la literatura de Ostrom
distingue a una institución de una regla heredada ciegamente: no hay comunicación entre
agentes, no hay monitoreo ni sanción, no hay memoria de interacciones pasadas ni reputación,
y las reglas cambian por mutación aleatoria y no por deliberación. Esa ausencia es, en sí
misma, parte del resultado: incluso sin ningún mecanismo institucional, la selección natural
sobre reglas heredadas basta para producir un enriquecimiento medible de la cooperación,
aunque uno mucho más modesto que el que las instituciones humanas deliberadas logran sostener
en los casos de Ostrom.

Estos hallazgos son exploratorios y varias limitaciones deben moderar su interpretación. El
modelo no está calibrado ni validado contra datos empíricos, de modo que los resultados son
propiedades cualitativas del modelo y no predicciones cuantitativas sobre sistemas
micorrícicos reales, y menos aún sobre sistemas humanos de gestión de recursos comunes.
Aunque varié la escala de la grilla, mantuve fija la composición inicial de la
población, los topes de recursos y los umbrales de intercambio y reproducción, y cada punto
de parámetro descansa en un número modesto de semillas (seis a diez), de modo que el
comportamiento ruidoso en el filo del colapso está estimado solo de manera gruesa. Más
importante aún, la señal de cooperación, aunque consistente y estadísticamente visible, es
pequeña bajo condiciones benignas y se vuelve grande solo bajo escasez; no querría
sobrestimarla. La percepción disponible para cada agente es deliberadamente tosca (tres
rasgos agrupados), lo que a la vez habilita una tabla de reglas interpretable y limita las
estrategias que pueden evolucionar, incluida la posibilidad de que emerjan formas de
reciprocidad más ricas que las que aquí observo.

Varias extensiones se siguen naturalmente. Introducir un mecanismo explícito de elección de
socio o de memoria de interacciones pasadas permitiría preguntar si la ausencia casi total de
condicionalidad al socio observada aquí (Experimento F) es una limitación de la percepción
más que de la selección, y acercaría el modelo a las condiciones bajo las cuales Ostrom
documenta instituciones deliberadas. Añadir un segundo recurso de uso común, o permitir que
los propios agentes modifiquen la tasa de renovación mediante su comportamiento, tal como
ocurre cuando el manejo humano de un bosque o una pesquería afecta su propia tasa de
recuperación, tendería un puente más directo hacia los sistemas socioecológicos que Ostrom
estudió, en los que sistema de recursos y sistema de gobernanza no son independientes sino que
coevolucionan. Finalmente, porque el modelo corre tanto de manera interactiva como headless y
es enteramente reproducible, se presta bien para uso docente y de divulgación, donde los
mismos experimentos aquí reportados pueden ser reproducidos y extendidos por estudiantes de
ciencias sociales interesados en simulación de sistemas de cooperación y gobernanza de
recursos.

## Conclusiones

Symbio-Grid muestra que una economía de intercambio de recursos, sostenida sobre un recurso
de uso común, puede emerger y sostener cooperación seleccionada a partir de estrategias
aleatorias, y cuantifica cómo la mutación, la disponibilidad de fósforo y su renovación
desplazan el balance entre una economía persistente y su colapso. El resultado más claro es
un umbral de resiliencia abrupto en renovación de fósforo cercana a cero que fija el entorno,
con independencia de la población: no se desplaza con la tasa de mutación y reaparece a través
de las escalas de grilla evaluadas. Leído contra el marco de sistemas socioecológicos de
Ostrom (2009), este resultado sugiere que la sostenibilidad de un recurso de uso común puede
estar acotada por su propia dinámica biofísica de manera independiente de cuánto varíe la
conducta de quienes lo explotan, un límite que ninguna capacidad de adaptación conductual,
biológica o institucional, puede por sí sola superar. La cooperación está genuinamente
seleccionada a partir de estrategias aleatorias, pero el efecto es leve y en gran medida
incondicional bajo condiciones benignas, y se vuelve fuerte solo bajo escasez, un patrón que
dialoga con la teoría de mercados biológicos y con los mecanismos de evolución de la
cooperación descritos por Nowak (2006). Esa señal solo aparece cuando el comportamiento se
mide en su expresión efectiva y no en promedios de genotipo completo, una advertencia
metodológica para la simulación social de estrategias evolutivas. Más allá de los hallazgos
específicos, el modelo se ofrece como un caso generativo abierto, reproducible e
interactivamente explorable para el estudio de la emergencia y evolución de la cooperación en
torno a recursos de uso común, en el que cada resultado aquí puede regenerarse desde una
semilla fija y extenderse. El software y todos los scripts de experimentación están
disponibles abiertamente.

## Agradecimientos

Este trabajo no recibió financiamiento externo. El autor declara no tener conflictos de
interés. El modelo, los scripts de experimentación y los datos generados están disponibles
abiertamente en el repositorio del proyecto.

## Referencias

Axelrod, R. (1984). *The evolution of cooperation*. Basic Books.

Epstein, J. M., y Axtell, R. (1996). *Growing artificial societies: Social science from the
bottom up*. Brookings Institution Press / MIT Press.

Grasso, S. V., Ryan, M. H., Albornoz, F. E., y Renton, M. (2025). A simple
plant–mycorrhizal fungal resource trade co-evolution model explains mutualism stability,
extinction and transitory parasitism via fitness feedback. *New Phytologist*, *248*(3),
1429-1441. https://doi.org/10.1111/nph.70540

Grimm, V., Railsback, S. F., Vincenot, C. E., Berger, U., Gallagher, C., DeAngelis, D. L.,
Edmonds, B., Ge, J., Giske, J., Groeneveld, J., Johnston, A. S. A., Milles, A.,
Nabe-Nielsen, J., Polhill, J. G., Radchuk, V., Rohwäder, M.-S., Stillman, R. A., Thiele, J.
C., y Ayllón, D. (2020). The ODD protocol for describing agent-based and other simulation
models: A second update to improve clarity, replication, and structural realism. *Journal of
Artificial Societies and Social Simulation*, *23*(2), 7. https://doi.org/10.18564/jasss.4259

Hardin, G. (1968). The tragedy of the commons. *Science*, *162*(3859), 1243-1248.
https://doi.org/10.1126/science.162.3859.1243

Masad, D., y Kazil, J. (2015). Mesa: An agent-based modeling framework. En *Proceedings of
the 14th Python in Science Conference* (pp. 51-58). https://doi.org/10.25080/Majora-7b98e3ed-009

Nowak, M. A. (2006). Five rules for the evolution of cooperation. *Science*, *314*(5805),
1560-1563. https://doi.org/10.1126/science.1133755

Ostrom, E. (1990). *Governing the commons: The evolution of institutions for collective
action*. Cambridge University Press.

Ostrom, E. (2009). A general framework for analyzing sustainability of social-ecological
systems. *Science*, *325*(5939), 419-422. https://doi.org/10.1126/science.1172133

Simard, S. W., Beiler, K. J., Bingham, M. A., Deslippe, J. R., Philip, L. J., y Teste, F. P.
(2012). Mycorrhizal networks: Mechanisms, ecology and modelling. *Fungal Biology Reviews*,
*26*(1), 39-60. https://doi.org/10.1016/j.fbr.2012.01.001

ter Hoeven, E., Kwakkel, J., Hess, V., Pike, T., Wang, B., rht, y Kazil, J. (2025). Mesa 3:
Agent-based modeling with Python in 2025. *Journal of Open Source Software*, *10*(107), 7668.
https://doi.org/10.21105/joss.07668

van 't Padje, A., Werner, G. D. A., y Kiers, E. T. (2021). Mycorrhizal fungi control
phosphorus value in trade symbiosis with host roots when exposed to abrupt 'crashes' and
'booms' of resource availability. *New Phytologist*, *229*(5), 2933-2944.
https://doi.org/10.1111/nph.17055

Vélez Torres, Á. (2019). Modelación y simulación basada en agentes en ciencias sociales: Una
aproximación al estado del arte. *Polis. Revista Latinoamericana*, *18*(53), 282-308.
https://doi.org/10.32735/s0718-6568/2019-n53-1392
