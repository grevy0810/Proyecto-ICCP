

import math
import random
import os


def itr(dis, dif, azar, x):

    a = float(dis)
    b = float(dif)
    c = float(azar)
    itr3lp = c + (1-c)/(1+math.exp(-a*(x-b)))
    return itr3lp


def informacionITR(resulItr, dis, azar):

    itr = float(resulItr)
    a = float(dis)
    c = float(azar)

    info = (pow(a, 2))*((1-itr)/itr)*pow((itr-c)/(1-c), 2)
    return info


def GuardarCambios(archivo, valores):
    archivo1 = open(archivo, 'w')
    archivo1_contents = "".join(valores)
    archivo1.write(archivo1_contents)
    archivo1.close()


def CambioDificul(index):

    if float(valorDifi[index]) > Deltha and Correct == True:
        cambio = float(valorDifi[index])-0.5
        valorDifi[index] = ("%.1f\n" % cambio)

    elif float(valorDifi[index]) < Deltha and Correct == False:
        cambio = float(valorDifi[index]) + 0.5
        valorDifi[index] = ("%.1f\n" % cambio)


def CambioDiscri(index):

    if float(valorDifi[index]) > Deltha and Correct == True:
        cambio = float(valorDiscri[index])-0.1
        valorDiscri[index] = ("%.1f\n" % cambio)

    elif float(valorDifi[index]) < Deltha and Correct == False:
        cambio = float(valorDiscri[index]) + 0.1
        valorDiscri[index] = ("%.1f\n" % cambio)


def PrintPregunt(idx):

    index = int(idx)
    print ("%d. %s" % (cont2, BancoPreguntas[index]))
    print (RespuestasBanco[index])


def VeriRespuest(Respuesta, index):

    entrada = Respuesta.capitalize()

    if entrada == RespuestaCorrecta[index]:
        return True
    else:
        return False


def RangoResp(respuesta, index):

    entrada = respuesta.capitalize()

    if "0.25\n" == valorAzar[index]:
        rang = ["A", "B", "C", "D"]
        while entrada != rang[0] and entrada != rang[1] and entrada != rang[2] and entrada != rang[3]:
            print ('Ingrese una de las opciones de respuesta\n')
            resp = raw_input()
            entrada = resp.capitalize()


    elif "0.20\n" == valorAzar[index]:
        rang = ["A", "B", "C", "D", "E"]
        while entrada != rang[0] and entrada != rang[1] and entrada != rang[2] and entrada != rang[3] and entrada != rang[4]:
            print ('Ingrese una de las opciones de respuesta\n')
            resp = raw_input()
            entrada = resp.capitalize()


    elif "0.33\n" == valorAzar[index]:

        rang = ["A", "B", "C"]
        while entrada != rang[0] and entrada != rang[1] and entrada != rang[2]:
            print ('Ingrese una de las opciones de respuesta\n')
            resp = raw_input()
            entrada = resp.capitalize()

    else:

        rang = ["A", "B"]
        while entrada != rang[0] and entrada != rang[1]:
            print ('Ingrese una de las opciones de respuesta\n')
            resp = raw_input()
            entrada = resp.capitalize()


def AumentDelth(correcta, deltha):
    if correcta == True:
        deltha += 0.3
    else:
        deltha -= 0.3
    return deltha

def limpiar():
    os.system("cls")


archivo1 = open('Dificultades.txt', 'r')
valorDifi = archivo1.readlines()

archivo2 = open('Discriminante.txt', 'r')
valorDiscri = archivo2.readlines()

archivo3 = open('Azar.txt', 'r')
valorAzar = archivo3.readlines()

archivo1.close()
archivo2.close()
archivo3.close()



BancoPreguntas = [("%cCu%cl es el pa%cs con menos habitantes del mundo?\n" % (168, 160, 161)), ("%cEn qu%c a%co cay%c el muro de Berl%cn?\n" % (168, 130, 164, 162, 161)),
                  ("%cCu%cndo empez%c y termin%c la Segunda Guerra Mundial?\n" % (168, 160, 162, 162)), ("%cCu%cndo muri%c Freddie Mercury?\n" % (168, 160, 162)),
                  ("%cCu%cl es el himno de la Uni%cn Europea?\n" % (168, 160, 162)), ("%cCu%cl es el atleta con m%cs medallas ol%cmpicas?\n" % (168, 160, 160, 161)),
                  ("%cCu%cl fue la primera civilizaci%cn humana?\n" % (168, 160, 162)), ("%cQu%c religi%cn tiene la Tor%c como su libro sagrado?\n" % (168, 130, 162, 160)),
                  ("%cCu%cl es la luna m%cs grande de Saturno?\n" % (168, 160, 160)), ("%cCu%cl es el animal m%cs r%cpido?\n" % (168, 160, 160, 160)),
                  ("%cQu%c enfermedad provoc%c la muerte de Stephen Hawking?\n" % (168, 130, 162)), ("%cCu%cntos corazones tiene un gusano de tierra?\n" % (168, 160)),
                  ("%cCu%cnto dur%c \"La Guerra de los Cien A%cos\"?\n" % (168, 160, 162, 164)), ("%cQui%cn descubri%c la penicilina?\n" % (168, 130, 162)),
                  ("%cQu%c pa%cs tiene el mejor sistema sanitario del mundo?\n" % (168, 130, 161)), ("%cCu%cl es la serpiente m%cs larga del mundo?\n" % (168, 160, 160)),
                  ("%cQu%c r%co atraviesa la ciudad de Benar%cs, en la India?\n" % (168, 130, 161, 130)), ("%cCu%cl es el primer libro de la biblia?\n" % (168, 160)),
                  ("%cGracias a qu%c gan%c Albert Einstein el Premio Nobel?\n" % (168, 130, 162)), ("%cCu%cl es la universidad m%cs antigua del mundo?\n" % (168, 160, 160)),
                  ("%cCu%cl es la edad del Universo?\n" % (168, 160)), ("%cCu%cl es la obra de arte m%cs cara jam%cs vendida?\n" % (168, 160, 160, 160)),
                  ("%cCu%cl es el nombre del pintor de la obra \"La Gioconda\"\n?" % (168, 160)), ("%cEn qu%c a%co el ser humano lleg%c al espacio?\n" % (168, 130, 164, 162)),
                  ("%cQu%c animal contagi%c a los humanos en la pandemia de peste negra?\n" % (168, 130, 162)), ("%cCu%cndo se extinguieron los dinosaurios?\n" % (168, 160)),
                  ("%cCu%cl es la estrella m%cs cercana al Sol?\n" % (168, 160, 160)), ("%cQu%c pigmento da color a nuestra piel?\n" % (168, 130)),
                  ("%cQu%c volc%cn sepult%c la ciudad de Pompeya?\n" % (168, 130, 160, 162)), ("%cCu%cntas peliculas tiene la serie \"Harry Potter\"?\n" % (168, 160)),
                  ("%cDe qu%c pa%cs es originario el queso brie?\n" % (168, 130, 161)), ("%cEn qu%c a%co se estableci%c la compa%c%ca Heinz?\n" % (168, 130, 164, 162, 164, 161)),
                  ("%cCu%cl es la capital de Islandia?\n" % (168, 160)), ("%cEn qu%c a%co muri%c Margaret Thatcher?\n" % (168, 130, 164, 162)),
                  ("%cCu%cntas v%clvulas tiene el coraz%cn?\n" % (168, 160, 160, 162)), ("Por lo general, %ccu%cl es el m%csculo m%cs fuerte en el cuerpo humano?\n" % (168, 160, 163, 160)),
                  ("%cCu%cl de estos pa%cses no tiene litoral en Europa?\n" % (168, 160, 161)), ("%cQui%cn es el l%cder espiritual m%cs alto del T%cbet?\n" % (168, 130, 161, 160, 161)),
                  ("%cC%cmo se llamaba la ciudad turca de Estambul antes de 1930?\n" % (168, 162)), ("%cCu%cl es la capital de Nueva Zelanda?\n" % (168, 160)),
                  ("En la rodilla se encuentra el ligamento cruzado. %cVerdadero o falso?\n" % 168), ("%cCu%cl es la moneda de Dinamarca?\n" % (168, 160)),
                  ("%cEn qu%c pa%cs europeo encontrar%cas el Rijksmuseum?\n" % (168, 130, 161, 161)), ("Seg%cn la leyenda, %cc%cmo muri%c el Papa Adriano IV en 1159?\n" % (163, 168, 162, 162)),
                  ("%cQu%c significa \"palimpsesto\"?\n" % (168, 130)), ("%cPor qu%c es reconocido Sergu%ci Rajm%cninov?\n" % (168, 130, 130, 160)),
                  ("%cQu%c parte del cuerpo produce insulina?\n" % (168, 130)), ("%cQu%c animal es la drosophila?\n" % (168, 130)),
                  ("%cCu%cntas s%clabas forman un haiku?\n" % (168, 160, 161)), ("%cCu%cl de estos pa%cses no tiene frontera con Brasil?\n" % (168, 160, 161)),
                  ("%cen qu%c deporte el juego interrumpido se reanuda con un \"scrum\"?\n" % (168, 130)), ("%cQui%cn era el padre de los dioses en la mitolog%ca n%crdica?\n" % (168, 130, 161, 162)),
                  ("El precuneo se encuentra en el l%cbulo parietal superior. %cVerdadero o Falso?\n" % (162, 168))]

RespuestasBanco = [("A. La Ciudad del Vaticano.\nB. San marino.\nC. M%cnaco.\nD. Nauru.\n" % 162),
                   "A. En 1989.\nB. En 1980.\nC. En 1990\nD. En 1987.\n",
                   "A. De 1914 a 1918.\nB. De 1937 a 1943.\nC. De 1917 a 1922.\nD. De 1939 a 1945.\n",
                   ("A. En el a%co 1991.\nB. En el a%co 1990.\nC. En el a%co 1992.\nD. En el a%co 1994.\n" % (164, 164, 164, 164)),
                   ("A. Fur Elise.\nB. Mollys Abschied.\nC. Oda a la Alegr%ca.\nD. Urians Reise\n" % 161),
                   "A. Michael Phelps.\nB. Larisa Latynina.\nC. Usain Bolt.\nD. Paavo Nurmi.\n",
                   ("A.La civilizaci%cn Egipcia.\nB.La civilizaci%cn sumeria.\nC.La civilizaci%cn China.\nD.La civilizaci%cn persa.\n" % (162, 162, 162, 162)),
                   ("A. El hinduismo.\nB. El budismo.\nC. El cristianismo.\nD. El juda%csmo.\n" % 161),
                   ("A. Mimas.\nB. Enc%clado.\nC. Tetis.\nD. Dione.\nE. Tit%cn.\n" % (130, 160)),
                   ("A. El Guepardo Chita.\nB. El halc%cn peregrino.\nC. El Tibur%cn Mako.\nD. La tortuga.\n" % (162, 162)),
                   ("A. Esclerosis Lateral Amiotr%cfica.\nB. Parkinson.\nC. C%cncer.\nD. Sida.\n" % (162, 160)),
                   "A. No tiene.\nB. Cinco.\nC. Tres.\nD. Uno.\n",
                   ("A. 50 a%cos.\nB. 90 a%cos.\nC. 116 a%cos.\nD. 99 a%cos.\n" % (164, 164, 164, 164)),
                   "A. Marie Curie.\nB. Charles Darwin.\nC. Leonardo Da Vinci.\nD. Alexander Fleming.\n",
                   "A. Francia.\nB. Colombia.\nC. Honduras.\nD. Estados Unidos.\n",
                   ("A. La Boa constrictor.\nB. La pit%cn reticulada.\nC. La Cobra Real.\nD. Serpiente Cascabel.\n" % 162),
                   ("A. El R%co Amazonas.\nB. El R%co Nilo.\nC. El r%co Ganges.\nD. El R%co Magdalena.\n" % (161, 161, 161, 161)),
                   ("A. El libro de Lev%ctico.\nB. El libro de N%cmeros.\nC. El libro de %cxodo.\nD. El libro de G%cnesis.\n" % (161, 163, 144, 130)),
                   ("A. Por la ley del efecto fotoel%cctrico.\nB. Por el movimiento Browniano\nC. Por la relatividad especial.\n" % 130),
                   "A. La Universidad de Stanford\nB. La Universidad de Bolonia.\nC. La Universidad de Oxford.\n",
                   ("A. 10 millones de a%cos.\nB. 5.000 millones de a%cos.\nC. 13.800 millones de a%cos.\nD. 7.000 millones de a%cos.\n" % (164, 164, 164, 164)),
                   ("A. La Gioconda.\nB. La %cltima cena.\nC. La noche estrellada.\nD. Salvator Mundi.\n" % 163),
                   ("A. Leonardo da Vinci.\nB. Pablo Picasso.\nC. Rembrandt.\nD. Diego Vel%czquez.\n"% 160),
                   "A. En 2001.\nB. En 1961.\nC. En 1990.\nD. En 1972.\n",
                   ("A. Las Ratas.\nB. Los Cerdos.\nC. Las pulgas.\nD. Los Murci%clagos.\n" % 130),
                   ("A. Hace 20 millones de a%cos.\nB. Hace 7 millones de a%cos.\nC. Hace 4 millones de a%cos.\nD. Hace 66 millones de a%cos.\n" % (164, 164, 164, 164)),
                   ("A. Alfa Centauri.\nB. Sirio.\nC. P%clux.\nD. Rigel.\n" % 162),
                   "A. La clorofila.\nB. La melanina.\nC. La bilirrubina.\nD. La hemocianina.\n",
                   "A. El Krakatoa.\nB. El Merapi.\nC. El Vesubio.\n",
                   ("A. 3 pel%cculas.\nB. 4 pel%cculas.\nC. 5 pel%cculas.\nD. 8 pel%cculas.\n" % (161, 161, 161, 161)),
                   ("A. Francia.\nB. Alemania.\nC. Noruega.\nD. Espa%ca.\n" % 164),
                   "A. 1869.\nB. 1890.\nC. 1894.\nD. 1860.\n",
                   ("A. Oslo.\nB. Reikiavik.\nC. %cmsterdam.\nD. Madrid.\n" % 143),
                   "A. 2000.\nB. 2002.\nC. 2013.\nD. 2007.\n",
                   "A. Cinco.\nB. Dos.\nC. Tres.\nD. Cuatro.\n",
                   ("A. El masetero (mand%cbula principal).\nB. Los Pectorales.\nC. El Tr%cceps.\nD. El Biceps.\n" % (161, 161)),
                   ("A. Espa%ca.\nB. Andorra.\nC. Grecia.\nD. Italia.\n"% 164),
                   ("A. El Thich Nhat Hanh.\nB. El papa Francisco.\nC. El Dalai Lama.\nD. Mart%cn Lutero.\n" % 161),
                   ("A. Damasco.\nB. Jerusal%cn.\nC. Babilonia.\nD. Constantinopla.\n" % 130),
                   "A. Wellington.\nB. Riad.\nC. Buenos Aires.\nD. Argel.\n",
                   "A. Verdadero.\nB. Falso.\n",
                   "A. Franco.\nB. Krone.\nC. Yen.\nD. Libra esterlina.\n",
                   "A. Grecia.\nB. Suiza.\nC. Paises Bajos.\nD. Portugal.\n",
                   ("A. Trag%cndose una mosca.\nB. Cay%cndose de un balc%cn.\nC. Choc%cndose contra una puerta.\nD. Cay%cndose de un caballo.\n" % (160, 130, 162, 160, 130)),
                   ("A. Un personaje que carece de seriedad.\nB. Razonamiento por el que la verdad de una proposici%cn se prueba demostrando la imposibilidad o absurdo de la proposici%cn contraria.\nC. Algo que sirve como ayuda auxiliar.\nD. Manuscrito cuya escritura ha sido eliminada con objeto de escribir otro texto encima.\n" % (162, 162)),
                   ("A. Por sus contribuciones al mundo de la f%csica cu%cntica.\nB. Por sus contribuciones al mundo de la m%csica.\nC. Por sus contribuciones al mundo de la pintura.\nD. Por sus contribuciones al mundo de la literatura.\n" % (161, 160, 163)),
                   ("A. El p%cncreas.\nB. El h%cgado.\nC. El bazo.\nD. El timo.\n" % (160, 161)),
                   "A. Una rata.\nB. Una mosca.\nC. Un conejillo de Indias.\nD. Una cabra.\n",
                   "A. 14.\nB. 15.\nC. 16.\nD. 17.\n",
                   "A. Surinam.\nB. Chile.\nC. Uruguay.\nD. Bolivia.\n",
                   ("A. hockey.\nB. rugby.\nC. b%cisbol.\nD. waterpolo.\n" % 130),
                   "A. thor.\nB. loki.\nC. odin.\nD. balder.\n",
                   "A. Verdadero.\nB. Falso.\n"]

RespuestaCorrecta = ["A", "A", "D", "A", "C", "A", "B", "D", "E", "B",
                     "A", "B", "C", "D", "A", "B", "C", "D", "A", "B",
                     "C", "D", "A", "B", "C", "D", "A", "B", "C", "D",
                     "A", "A", "B", "C", "D", "A", "B", "C", "D", "A",
                     "A", "B", "C", "A", "D", "B", "A", "B", "D", "B",
                     "B", "C", "A"]


infoPrueba = ("""Bienvenido a la prueba adaptativa computarizada de cultura general. 

Esta prueba se adapta a t%c nivel de conocimientos!!
Te clasifica entre 7 niveles. 
Tiene un m%cximo de 15 preguntas, pero pueden ser menos dependiendo de tus respuestas.

%cEstas preparado para la prueba?.

""" % (163, 160, 168))

print (infoPrueba)
menu = raw_input('Men%c Principal:\n\n'
                 '1. Realizar prueba.\n'
                 '2. puntuaciones.\n'
                 '3. Salir. \n'
                 'Digita del 1 al 3 la opci%cn que desea realizar.\n' % (163, 162))

limpiar()
while menu != '3':
    if menu == '1':

        name = raw_input('%cCu%cl es su nombre?\n' % (168, 160))
        limpiar()
        cont2 = 1
        Deltha = 0
        difiProm = "0.0\n"
        opcion = []
        cont = 0
        for j in valorDifi:

            if difiProm == j:
                opcion.append(valorDifi.index(j, cont, len(valorDifi)))

            cont += 1

        opcionInicial = random.randint(0, len(opcion)-1)
        PrintPregunt(opcion[opcionInicial])
        cont2 += 1

        UsuarioResp = raw_input()
        limpiar()
        RangoResp(UsuarioResp, opcion[opcionInicial])
        Correct = VeriRespuest(UsuarioResp, opcion[opcionInicial])

        CambioDificul(opcion[opcionInicial])
        CambioDiscri(opcion[opcionInicial])
        Deltha = AumentDelth(Correct, Deltha)

        PreguntasRespond = [opcion[opcionInicial]]

        k = 0
        finTest = False
        while k < 14 and finTest == False:

            ResultITR = []
            infoITR = []

            for i in range(0, len(valorDifi)):
                ResultITR.append(itr(valorDiscri[i], valorDifi[i], valorAzar[i], Deltha))

            for j in range(0, len(ResultITR)):
                infoITR.append(informacionITR(ResultITR[j], valorDiscri[j], valorAzar[j]))

            for s in PreguntasRespond:
                infoITR[s] = 0

            max_value = None
            max_index = None
            for idx, num in enumerate(infoITR):

                if (max_value is None or num > max_value):
                    max_value = num
                    max_index = idx

            PreguntasRespond.append(max_index)
            PrintPregunt(max_index)
            cont2 += 1

            UsuarioResp = raw_input()
            limpiar()
            RangoResp(UsuarioResp, max_index)
            Correct = VeriRespuest(UsuarioResp, max_index)

            CambioDificul(max_index)
            CambioDiscri(max_index)
            Deltha = AumentDelth(Correct, Deltha)

            if (Deltha > 3.5) or (Deltha < -3.5) or (-2.7 < Deltha < -2 and k >= 10) or (
                    2.7 > Deltha > 2 and k >= 10) or \
                    (k == 12 and (Deltha >= 1.5 or Deltha <= -1.5)):
                finTest = True

            k += 1

        Level = int(Deltha) + 4
        print ("siendo 1 el m%cs bajo y 7 el m%cs alto\n" % (160, 160))
        print ("Su nivel de cultura general es:  %d\n" % Level)


        GuardarCambios('Dificultades.txt', valorDifi)
        GuardarCambios('Discriminante.txt', valorDiscri)

        archivo4 = open('puntuaciones.txt', 'a')
        infoparti = ("%s\t\t%d\n" % (name, Level))
        archivo4.write(infoparti)
        archivo4.close()

    elif menu == '2':

        my_puntuacion = open('puntuaciones.txt')
        puntuaciones = my_puntuacion.read()
        my_puntuacion.close()

        print ('Puntuaciones:\n' )
        print (puntuaciones)

    else:
        print ('Debes digitar una opci%cn entre 1 y 3\n' % 162)

    menu = raw_input('Men%c Principal:\n\n'
                     '1. Realizar prueba.\n'
                     '2. puntuaciones.\n'
                     '3. Salir. \n'
                     'Digita del 1 al 3 la opci%cn que desea realizar.\n' % (163, 162))
    limpiar()