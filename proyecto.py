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
                  "¿Cuál es el himno de la Unión Europea?\n", "¿Cuál es el atleta con más medallas olímpicas?\n"]

RespuestasBanco = ["A. La Ciudad del Vaticano.\n""B. San marino.\n""C. Mónaco.\n""D. Nauru.\n",
                   "A. En 1989.\n""B. En 1980.\n""C. En 1990\n""D. En 1987.\n",
                   "A. De 1914 a 1918.\n""B. De 1937 a 1943.\n""C. De 1917 a 1922.\n""D. De 1939 a 1945.\n",
                   "En el año 1991.\n""En el año 1990.\n""En el año 1992.\n""En el año 1994.\n",
                   "A. Fur Elise.\n""B. Mollys Abschied.\n""C. Oda a la Alegría.\n""D. Urians Reise\n",
                   "Michael Phelps.\n""Larisa Latynina.\n""Usain Bolt.\n""Paavo Nurmi.\n"]
RespuestaCorrecta = ["A", "A", "D", "A", "C", "A"]


print itr(1,1,0.25,0)
archivo1.close()
archivo2.close()
archivo3.close()