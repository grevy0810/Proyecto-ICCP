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
                   "A.La civilización Egipcia.\n""B.La civilización sumeria.\n""C.La civilización China.\n""D.La civilización persa.\n",
                   "A. El hinduismo.\n""B. El budismo.\n""C. El cristianismo.\n""D. El judaísmo.\n",
                   "A. Mimas.\n""B. Encélado.\n""C. Tetis.\n""D. Dione.\n""E. Titán.\n",
                   "A. El Guepardo Chita.\n""B. El halcón peregrino.\n""C. El Tiburón Mako.\n""D. La tortuga.\n",
                   "A. Esclerosis Lateral Amiotrófica.\n""B. Parkinson.\n""C. Cáncer.\n""D. Sida.\n",
                   "A. No tiene.\n""B. Cinco.\n""C. Tres.\n""D. Uno.\n",
                   "A. 50 años.\n""B. 90 años.\n""C. 116 años.\n""D. 99 años.\n",
                   "A. Marie Curie.\n""B. Charles Darwin.\n""C. Leonardo Da Vinci.\n""D. Alexander Fleming.\n",
                   "A. Francia.\n""B. Colombia.\n""C. Honduras.\n""D. Estados Unidos.\n",
                   "A. La Boa constrictor.\n""B. La pitón reticulada.\n""C. La Cobra Real.\n""D. Serpiente Cascabel.\n",
                   "A. El Río Amazonas.\n""B. El Río Nilo.\n""C. El río Ganges.\n""D. El Río Magdalena.\n",
                   "A. El libro de Levítico.\n""B. El libro de Números.\n""C. El libro de Éxodo.\n""D. El libro de Génesis.\n",
                   "A. Por la ley del efecto fotoeléctrico.\n""B. Por el movimiento Browniano\n""C. Por ea relatividad especial.\n",
                   "A. La Universidad de Stanford\n""B. La Universidad de Bolonia.\n""C. La Universidad de Oxford.\n",
                   "A. 10 millones de años.\n""B. 5.000 millones de años.\n""C. 13.800 millones de años.\n""D. 7.000 millones de años.\n",
                   "A. La Gioconda.\n""B. La última cena.\n""C. La noche estrellada.\n""D. Salvator Mundi.\n",
                   "A. Leonardo da Vinci.\n""B. Pablo Picasso.\n""C. Rembrandt.\n""D. Diego Velázquez.\n",
                   "A. En 2001.\n""B. En 1961.\n""C. En 1990.\n""D. En 1972.\n",
                   "A. Las Ratas.\n""B. Los Cerdos.\n""C. Las pulgas.\n""D. Los Murcielagos.\n",
                   "A. Hace 20 millones de años.\n""B. Hace 7 millones de años.\n""C. Hace 4 millones de años.\n""D. Hace 66 millones de años.\n",
                   "A. Alfa Centauri.\n""B. Sirio.\n""C. Pólux.\n""D. Rigel.\n",
                   "A. La clorofila.\n""B. La melanina.\n""C. La bilirrubina.\n""D. La hemocianina.\n",
                   "A. El Krakatoa.\n""B. El Merapi.\n""C. El Vesubio.\n",
                   "A. 3 películas.\n""B. 4 películas.\n""C. 5 películas.\n""D. 8 películas.\n",
                   "A. Francia.\n""B. Alemania.\n""C. Noruega.\n""D. España.\n",
                   "A. 1869.\n""B. 1890.\n""C. 1894.\n""D. 1860.\n",
                   "A. Oslo.\n""B. Reikiavik.\n""C. Ámsterdam.\n""D. Madrid.\n",
                   "A. 2000.\n""B. 2002.\n""C. 2013.\n""D. 2007.\n",
                   "A. Cinco.\n""B. Dos.\n""C. Tres.\n""D. Cuatro.\n",
                   "A. El masetero (mandíbula principal).\n""B. Los Pectorales.\n""C. El Tríceps.\n""D. El Biceps.\n",
                   "A. España.\n""B. Andorra.\n""C. Grecia.\n""D. Italia.\n",
                   "A. El Thich Nhat Hanh.\n""B. El papa Francisco.\n""C. El Dalai Lama.\n""D. Martín Lutero.\n",
                   "A. Damasco.\n""B. Jerusalén.\n""C. Babilonia.\n""D. Constantinopla.\n",
                   "A. Wellington.\n""B. Riad.\n""C. Buenos Aires.\n""D. Argel.\n",
                   "A. Verdadero.\n""B. Falso.\n",
                   "A. Franco.\n""B. Krone.\n""C. Yen.\n""D. Libra esterlina.\n",
                   "A. Grecia.\n""B. Suiza.\n""C. Paises Bajos.\n""D. Portugal.\n",
                   "A. Tragándose una mosca.\n""B. Cayéndose de un balcón.\n""C. Chocándose contra una puerta.\n""D. Cayéndose de un caballo.\n",
                   "A. Un personaje que carece de seriedad.\n""B. Razonamiento por el que la verdad de una proposición se prueba demostrando la imposibilidad o absurdo de la proposición contraria.\n""C. Algo que sirve como ayuda auxiliar.\n""D. Manuscrito cuya escritura ha sido eliminada con objeto de escribir otro texto encima.\n",
                   "A. Por sus contribuciones al mundo de la física cuántica.\n""B. Por sus contribuciones al mundo de la música.\n""C. Por sus contribuciones al mundo de la pintura.\n""D. Por sus contribuciones al mundo de la literatura.\n",
                   "A. El páncreas.\n""B. El hígado.\n""C. El bazo.\n""D. El timo.\n",
                   "A. Una rata.\n""B. Una mosca.\n""C. Un conejillo de Indias.\n""D. Una cabra.\n",
                   "A. 14.\n""B. 15.\n""C. 16.\n""D. 17.\n",
                   "A. Surinam.\n""B. Chile.\n""C. Uruguay.\n""D. Bolivia.\n",
                   "A. hockey.\n""B. rugby.\n""C. béisbol.\n""D. waterpolo.\n",
                   "A. thor.\n""B. loki.\n""C. odin.\n""D. balder.\n",
                   "A. Verdadero.\n""B. Falso.\n"]

RespuestaCorrecta = ["A", "A", "D", "A", "C", "A", "B", "D", "E", "B",
                     "A", "B", "C", "D", "A", "B", "C", "D", "A", "B",
                     "C", "D", "A", "B", "C", "D", "A", "B", "C", "D",
                     "A", "A", "B", "C", "D", "A", "B", "C", "D", "A",
                     "A", "B", "C", "A", "D", "B", "A", "B", "D", "B",
                     "B", "C", "A"]


menu = """Bienvenido a la prueba adaptativa computarizada de cultura general. 

Esta prueba se adapta a tú nivel de conocimientos!!
Tiene un máximo de 20 preguntas, pero pueden ser menos dependiendo de tus tus respuestas y
no tiene tiempo limite.
¿Estas preparado para la prueba?.

Este es el menú de inicio.

1. Realizar prueba.
2. puntuaciones.
3. Información sobre el programa y la prueba.
4. Salir. 

"""

print (menu)

opcion = input('Digita del 1 al 3 la opción que desea realizar.')

if opcion == '1':
    pass
elif opcion == '2':
    pass
elif opcion == '3':
    pass
elif opcion == '4':
    pass
else:
    print ('Debes digitar una opción entre 1 y 4')
archivo1.close()
archivo2.close()
archivo3.close()