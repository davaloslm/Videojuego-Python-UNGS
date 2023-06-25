#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      davaloslm-PC
#
# Created:     10/06/2023
# Copyright:   (c) davaloslm-PC 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from configuracion import *
import random
import math
from extras import *

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    archivo = open("lemario.txt", "r", encoding="latin-1")
    lineas = archivo.readlines()

    for linea in lineas:
        palabra = linea.rstrip("\n")
        diccionario.append(palabra)

    archivo.close()


#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras(dificultad):

    listaLetrasDificiles = ["k","x","y","z"]
    listaVocales = ["a","e","i","o","u"]
    listaConsonantes = ["b", "c", "d", "f", "g", "h","j", "l","m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w"]

    letras = []


    #a mayor dificultad, mayor chance de que toquen letras difíciles

    if dificultad == "facil":
        probabilidad = random.randint(1,100)
    elif dificultad == "normal":
        probabilidad = random.randint(1,50)
    elif dificultad == "dificil":
        probabilidad = 2

    if probabilidad == 2:
        letras.append(random.choice(listaLetrasDificiles))

    cantVocales = random.randint(2,3)

    vocalRandom = random.sample(listaVocales,k=cantVocales) # toma 3 vocales aleatorios
    consonanteRandom = random.sample(listaConsonantes,k=7-(cantVocales+len(letras))) # poner el 7 en configuracion
    letras = letras + vocalRandom + consonanteRandom
    letras_final = ''.join(letras)

    return letras_final

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
    posicion = random.randint(0, (len(letrasEnPantalla)-1))
    letraPrincipal = letrasEnPantalla[posicion]

    return letraPrincipal

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, listaCorrectas):

    #si es valida y además si no es una palabra repetida
    if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario) and candidata not in listaCorrectas:
        correctas(candidata, listaCorrectas)
        sonidoAcierto()
        return Puntos(candidata)

    else:
        sonidoError()
        return -1

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):

    if letraPrincipal in candidata and candidata in diccionario and len(candidata)>=3 :

        return estanTodas(candidata,letrasEnPantalla)


#devuelve los puntos
def Puntos(candidata):

    puntos = -1

    if len(candidata) == 3:
        puntos = 1
    elif len(candidata) == 4:
        puntos = 2
    elif len(candidata) == 7:
        puntos = 10
    elif len(candidata) > 4 and len(candidata) !=7:
        puntos = len(candidata)

    return(puntos)

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    correctas = []

    for palabra in diccionario:
        if letraPrincipal in palabra:
            if estanTodas(palabra, letrasEnPantalla):
                correctas.append(palabra)


    return correctas

