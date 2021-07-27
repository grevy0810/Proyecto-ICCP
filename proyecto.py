#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def itr(a, b, c, x):
    ModelLog3 = c + (1-c)/(1+math.exp(-a*(x-b)))
    return ModelLog3

archivo1 = open('Dificultades.txt', 'r')
valorDifi = archivo1.readlines()

archivo2 = open('Discriminante.txt', 'r')
valorDiscri = archivo2.readlines()

archivo3 = open('Azar.txt', 'r')
valorAzar = archivo3.readlines()

conocimiento = 0

Dificultad={}
Discriminante={}
Azar={}

for i in range(0, 6):
    Dificultad[i] = valorDifi[i]
    Discriminante[i] = valorDiscri[i]
    Azar[i] = valorAzar[i]

BancoPreguntas = ["¿Cuál es el país con menos habitantes del mundo?\n", "¿En qué año cayó el muro de Berlín?\n",
                  "¿Cuándo empezó y terminó la Segunda Guerra Mundial?\n", "¿Cuándo murió Freddie Mercury?\n",
                  "¿Cuál es el himno de la Unión Europea?\n", "¿Cuál es el atleta con más medallas olímpicas?\n",
                  "¿Cuál fue la primera civilización humana?\n","¿Qué religión tiene la Torá como su libro sagrado?\n",
                  "¿Cuál es la luna más grande de Saturno?\n","¿Cuál es el animal más rápido?\n",
                  "¿Qué enfermedad provocó la muerte de Stephen Hawking?\n","¿Cuántos corazones tiene un gusano de tierra?\n",
                  "¿Cuánto duró “La Guerra de los Cien Años”?\n","¿Quién descubrió la penicilina?\n",
                  "¿Qué país tiene el mejor sistema sanitario del mundo?\n","¿Cuál es la serpiente más larga del mundo?\n",
                  "¿Qué río atraviesa la ciudad de Benarés, en la India?\n","¿Cuál es el primer libro de la biblia?\n",
                  "¿Gracias a qué ganó Albert Einstein el Premio Nobel?\n","¿Cuál es la universidad más antigua del mundo?\n",
                  "¿Cuál es la edad del Universo?\n","¿Cuál es la obra de arte más cara jamás vendida?\n",
                  "¿Cuál es el nombre del pintor de la obra \"La Gioconda\"\n?","¿En qué año el ser humano llegó al espacio?\n",
                  "¿Qué animal contagió a los humanos en la pandemia de peste negra?\n","¿Cuándo se extinguieron los dinosaurios?\n",
                  "¿Cuál es la estrella más cercana al Sol?\n","¿Qué pigmento da color a nuestra piel?\n",
                  "¿Qué volcán sepultó la ciudad de Pompeya?\n","¿Cuántas peliculas tiene la serie \"Harry Potter\"?\n",
                  "¿De qué país es originario el queso brie?\n","¿En qué año se estableció la compañía Heinz?\n",
                  "¿Cuál es la capital de Islandia?\n","¿En qué año murió Margaret Thatcher?\n",
                  "¿Cuántas válvulas tiene el corazón?\n","Por lo general, ¿cuál es el músculo más fuerte en el cuerpo humano?\n",
                  "¿Cuál de estos países no tiene litoral en Europa?\n","¿Quién es el líder espiritual más alto del Tíbet?\n",
                  "¿Cómo se llamaba la ciudad turca de Estambul antes de 1930?\n","¿Cuál es la capital de Nueva Zelanda?\n",
                  "En la rodilla se encuentra el ligamento cruzado. ¿Verdadero o falso?\n","¿Cuál es la moneda de Dinamarca?\n",
                  "¿En qué país europeo encontrarías el Rijksmuseum?\n","Según la leyenda, ¿cómo murió el Papa Adriano IV en 1159?\n",
                  "¿Qué significa “palimpsesto”?\n","¿Por qué es reconocido Serguéi Rajmáninov?\n",
                  "¿Qué parte del cuerpo produce insulina?\n","¿Qué animal es la drosophila?\n",
                  "¿Cuántas sílabas forman un haiku?\n","¿Cuál de estos países no tiene frontera con Brasil?\n",
                  "¿en qué deporte el juego interrumpido se reanuda con un \"scrum\"?\n","¿quién era el padre de los dioses en la mitología nórdica?\n",
                  "El precuneo se encuentra en el lóbulo parietal superior. ¿Verdadero o Falso?\n"]

RespuestasBanco = ["A. La Ciudad del Vaticano.\n""B. San marino.\n""C. Mónaco.\n""D. Nauru.\n",
                   "A. En 1989.\n""B. En 1980.\n""C. En 1990\n""D. En 1987.\n",
                   "A. De 1914 a 1918.\n""B. De 1937 a 1943.\n""C. De 1917 a 1922.\n""D. De 1939 a 1945.\n",
                   "A. En el año 1991.\n""B. En el año 1990.\n""C. En el año 1992.\n""D. En el año 1994.\n",
                   "A. Fur Elise.\n""B. Mollys Abschied.\n""C. Oda a la Alegría.\n""D. Urians Reise\n",
                   "A. Michael Phelps.\n""B. Larisa Latynina.\n""C. Usain Bolt.\n""D. Paavo Nurmi.\n",
                   "A.La civilización Egipcia.""B.La civilización sumeria.""C.La civilización China.""D.La civilización persa.",
                   "A. El hinduismo.""B. El budismo.""C. El cristianismo.""D. El judaísmo.",
                   "A. Mimas.""B. Encélado.""C. Tetis.""D. Dione.""E. Titán.",
                   "A. El Guepardo Chita.""B. El halcón peregrino.""C. El Tiburón Mako.""D. La tortuga.",
                   "A. Esclerosis Lateral Amiotrófica.""B. Parkinson.""C. Cáncer.""D. Sida.",
                   "A. No tiene.""B. Cinco.""C. Tres.""D. Uno.",
                   "A. 50 años.""B. 90 años.""C. 116 años.""D. 99 años.",
                   "A. Marie Curie.""B. Charles Darwin.""C. Leonardo Da Vinci.""D. Alexander Fleming.",
                   "A. Francia.""B. Colombia.""C. Honduras.""D. Estados Unidos.",
                   "A. La Boa constrictor.""B. La pitón reticulada.""C. La Cobra Real.""D. Serpiente Cascabel.",
                   "A. El Río Amazonas.""B. El Río Nilo.""C. El río Ganges.""D. El Río Magdalena.",
                   "A. El libro de Levítico.""B. El libro de Números.""C. El libro de Éxodo.""D. El libro de Génesis.",
                   "A. Por la ley del efecto fotoeléctrico.""B. Por el movimiento Browniano""C. Por ea relatividad especial.",
                   "A. La Universidad de Stanford""B. La Universidad de Bolonia.""C. La Universidad de Oxford.",
                   "A. 10 millones de años.""B. 5.000 millones de años.""C. 13.800 millones de años.""D. 7.000 millones de años.",
                   "A. La Gioconda.""B. La última cena.""C. La noche estrellada.""D. Salvator Mundi.",
                   "A. Leonardo da Vinci.""B. Pablo Picasso.""C. Rembrandt.""D. Diego Velázquez.",
                   "A. En 2001.""B. En 1961.""C. En 1990.""D. En 1972.",
                   "A. Las Ratas.""B. Los Cerdos.""C. Las pulgas.""D. Los Murcielagos.",
                   "A. Hace 20 millones de años.""B. Hace 7 millones de años.""C. Hace 4 millones de años.""D. Hace 66 millones de años.",
                   "A. Alfa Centauri.""B. Sirio.""C. Pólux.""D. Rigel.",
                   "A. La clorofila.""B. La melanina.""C. La bilirrubina.""D. La hemocianina.",
                   "A. El Krakatoa.""B. El Merapi.""C. El Vesubio.",
                   "A. 3 películas.""B. 4 películas.""C. 5 películas.""D. 8 películas.",
                   "A. Francia.""B. Alemania.""C. Noruega.""D. España.",
                   "A. 1869.""B. 1890.""C. 1894.""D. 1860.",
                   "A. Oslo.""B. Reikiavik.""C. Ámsterdam.""D. Madrid.",
                   "A. 2000.""B. 2002.""C. 2013.""D. 2007.",
                   "A. Cinco.""B. Dos.""C. Tres.""D. Cuatro.",
                   "A. El masetero (mandíbula principal).""B. Los Pectorales.""C. El Tríceps.""D. El Biceps.",
                   "A. España.""B. Andorra.""C. Grecia.""D. Italia.",
                   "A. El Thich Nhat Hanh.""B. El papa Francisco.""C. El Dalai Lama.""D. Martín Lutero.",
                   "A. Damasco.""B. Jerusalén.""C. Babilonia.""D. Constantinopla.",
                   "A. Wellington.""B. Riad.""C. Buenos Aires.""D. Argel.",
                   "A. Verdadero.""B. Falso.",
                   "A. Franco.""B. Krone.""C. Yen.""D. Libra esterlina.",
                   "A. Grecia.""B. Suiza.""C. Paises Bajos.""D. Portugal.",
                   "A. Tragándose una mosca.""B. Cayéndose de un balcón.""C. Chocándose contra una puerta.""D. Cayéndose de un caballo.",
                   "A. Un personaje que carece de seriedad.""B. Razonamiento por el que la verdad de una proposición se prueba demostrando la imposibilidad o absurdo de la proposición contraria.""C. Algo que sirve como ayuda auxiliar.""D. Manuscrito cuya escritura ha sido eliminada con objeto de escribir otro texto encima.",
                   "A. Por sus contribuciones al mundo de la física cuántica.""B. Por sus contribuciones al mundo de la música.""C. Por sus contribuciones al mundo de la pintura.""D. Por sus contribuciones al mundo de la literatura.",
                   "A. El páncreas.""B. El hígado.""C. El bazo.""D. El timo.",
                   "A. Una rata.""B. Una mosca.""C. Un conejillo de Indias.""D. Una cabra.",
                   "A. 14.""B. 15.""C. 16.""D. 17.",
                   "A. Surinam.""B. Chile.""C. Uruguay.""D. Bolivia.",
                   "A. hockey." "B. rugby.""C. béisbol.""D. waterpolo.",
                   "A. thor.""B. loki.""C. odin.""D. balder.",
                   "A. Verdadero.""B. Falso."]
RespuestaCorrecta = ["A", "A", "D", "A", "C", "A"]


print itr(1,1,0.25,0)
archivo1.close()
archivo2.close()
archivo3.close()