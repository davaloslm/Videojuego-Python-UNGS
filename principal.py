#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      davaloslm-PC
#
# Created:     18/06/2023
# Copyright:   (c) davaloslm-PC 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesRESUELTO import *
from extras import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Tiene la Palabra")
screen = pygame.display.set_mode((800, 600))
BG = pygame.image.load("img/fondo.jpg")
start = pygame.mixer.Sound("sonidos/start.mp3") #nuevo
start.play(0)

dificultad = "normal"
listaPuntajes = lecturaJSON()
listaCorrectas = []


defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

def menuInicio():
    while True:

        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = defaultFontGrande.render("Tiene la Palabra", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(400, 300),
                            text_input="JUGAR", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(400, 350),
                            text_input="OPCIONES", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="#d7fcd4", hovering_color="Green")
        RECORDS_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(400, 400),
                            text_input="RÉCORDS", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="#d7fcd4", hovering_color="Green")
        HOWTOPLAY_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(400, 450),
                            text_input="CÓMO JUGAR", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("img/Options Rect.png"), pos=(400, 500),
                            text_input="SALIR", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="#d7fcd4", hovering_color="Green")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, RECORDS_BUTTON, HOWTOPLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main(dificultad)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    opciones()
                if RECORDS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    records()
                if HOWTOPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    comoJugar()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def opciones():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        #MOSTRAR DIFICULTADES
        OPTIONS_TEXT = defaultFont.render("SELECCIONAR DIFICULTAD", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #botones de dificultad

        OPTIONS_EASY = Button(image=None, pos=(400, 250),
                            text_input="FÁCIL", font=pygame.font.Font( pygame.font.get_default_font(), 20), base_color="White", hovering_color="Blue")
        OPTIONS_NORMAL = Button(image=None, pos=(400, 300),
                            text_input="NORMAL", font=pygame.font.Font( pygame.font.get_default_font(), 20), base_color="White", hovering_color="Green")
        OPTIONS_HARD = Button(image=None, pos=(400, 350),
                            text_input="DIFÍCIL", font=pygame.font.Font( pygame.font.get_default_font(), 20), base_color="White", hovering_color="Red")

        OPTIONS_BACK = Button(image=None, pos=(400, 460),
                            text_input="ATRÁS", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="White", hovering_color="Green")

        for button in [OPTIONS_EASY, OPTIONS_NORMAL, OPTIONS_HARD, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global dificultad #para que se modifique la variable dificultad y no se cree una local con el mismo nombre
                if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    #sonido dificultad facil
                    dificultad = "facil"
                    menuInicio()
                if OPTIONS_NORMAL.checkForInput(OPTIONS_MOUSE_POS):
                    #sonido dificultad normal
                    dificultad = "normal"
                    menuInicio()
                if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    #sonido dificultad dificil
                    dificultad = "dificil"
                    menuInicio()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    menuInicio()

        pygame.display.update()

def comoJugar():
    while True:
        HOW_TO_PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        HOW_TO_PLAY_TEXT1 = defaultFont.render("El objetivo es armar palabras de al menos 3 letras.", True, "White")
        HOW_TO_PLAY_RECT1 = HOW_TO_PLAY_TEXT1.get_rect(center=(400, 200))
        screen.blit(HOW_TO_PLAY_TEXT1, HOW_TO_PLAY_RECT1)

        HOW_TO_PLAY_TEXT2 = defaultFont.render("Puedes repetir las letras, pero siempre incluyendo la letra principal.", True, "White")
        HOW_TO_PLAY_RECT2 = HOW_TO_PLAY_TEXT2.get_rect(center=(400, 250))
        screen.blit(HOW_TO_PLAY_TEXT2, HOW_TO_PLAY_RECT2)

        HOW_TO_PLAY_TEXT3 = defaultFont.render("No se admiten plurales y formas verbales conjugadas (solo infinitivos).", True, "White")
        HOW_TO_PLAY_RECT3 = HOW_TO_PLAY_TEXT3.get_rect(center=(400, 300))
        screen.blit(HOW_TO_PLAY_TEXT3, HOW_TO_PLAY_RECT3)

        HOW_TO_PLAY_TEXT4 = defaultFont.render("La dificultad controla la probabilidad de que aparezcan letras difíciles(K, X, Y, Z)", True, "White")
        HOW_TO_PLAY_RECT4 = HOW_TO_PLAY_TEXT4.get_rect(center=(400, 350))
        screen.blit(HOW_TO_PLAY_TEXT4, HOW_TO_PLAY_RECT4)

        HOW_TO_PLAY_BACK = Button(image=None, pos=(400, 460),
                            text_input="ATRÁS", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="White", hovering_color="Green")

        HOW_TO_PLAY_BACK.changeColor(HOW_TO_PLAY_MOUSE_POS)
        HOW_TO_PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HOW_TO_PLAY_BACK.checkForInput(HOW_TO_PLAY_MOUSE_POS):
                    menuInicio()

        pygame.display.update()

def finDelJuego(puntos):
    while True:
        END_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        #si el puntaje es mayor al puntaje mas bajo de los records
        if puntos > sorted(listaPuntajes, key=operator.itemgetter('puntaje') )[0]["puntaje"]:

            sonidoFin()

            nombre = ""
            gameClock = pygame.time.Clock()
            segundos = TIEMPO_MAX
            fps = FPS_inicial

            while segundos > fps/1000:
            # 1 frame cada 1/fps segundos
                gameClock.tick(fps)

                if True:
                    fps = 3

                #Buscar la tecla apretada del modulo de eventos de pygame
                for e in pygame.event.get():

                    #QUIT es apretar la X en la ventana
                    if e.type == QUIT:
                        pygame.quit()
                        return()

                    #Ver si fue apretada alguna tecla
                    if e.type == KEYDOWN:
                        letra = dameLetraApretada(e.key)
                        nombre += letra   #va concatenando las letras que escribe
                        if e.key == K_BACKSPACE:
                            nombre = nombre[0:len(nombre)-1] #borra la ultima
                        if e.key == K_RETURN:  #presionó enter
                            #GUARDA EL NUEVO RECORD Y SALE AL MENU DE INICIO
                            escrituraJSON(nombre, puntos, listaPuntajes)
                            menuInicio()

                #Limpiar pantalla anterior
                screen.fill(COLOR_FONDO)

                #Linea del piso
                pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

                #blit
                END_TEXT1 = defaultFont.render("¡NUEVO RÉCORD!", True, "White")
                END_RECT1 = END_TEXT1.get_rect(center=(400, 250))
                screen.blit(END_TEXT1, END_RECT1)

                END_TEXT2 = defaultFont.render("Ingresa tu nombre", True, "White")
                END_RECT2 = END_TEXT2.get_rect(center=(400, 300))
                screen.blit(END_TEXT2, END_RECT2)

                NAME_TEXT = defaultFont.render(nombre, True, "White")
                NAME_RECT = NAME_TEXT.get_rect(center=(400, 570))
                screen.blit(NAME_TEXT, NAME_RECT)

                #usar funcion escritura json

                pygame.display.flip()

        else:
            END_TEXT = defaultFont.render("Juego terminado", True, "White")
            END_RECT = END_TEXT.get_rect(center=(400, 300))
            screen.blit(END_TEXT, END_RECT)

            END_PLAY_AGAIN = Button(image=None, pos=(200, 460),
                                text_input="JUGAR DE NUEVO", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="White", hovering_color="Green")
            END_BACK = Button(image=None, pos=(600, 460),
                                text_input="MENÚ", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="White", hovering_color="Green")

            END_BACK.changeColor(END_MOUSE_POS)
            END_BACK.update(screen)

            END_PLAY_AGAIN.changeColor(END_MOUSE_POS)
            END_PLAY_AGAIN.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if END_BACK.checkForInput(END_MOUSE_POS):
                    menuInicio()
                if END_PLAY_AGAIN.checkForInput(END_MOUSE_POS):
                    main(dificultad)

        pygame.display.update()

def records():
    while True:
        RECORDS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        RECORDS_TEXT = defaultFont.render("MEJORES PUNTAJES", True, "White")
        RECORDS_RECT = RECORDS_TEXT.get_rect(center=(400, 75))
        screen.blit(RECORDS_TEXT,RECORDS_RECT)

        #llamar a lecturaJSON y listar en columnas los nombres y puntajes

        espaciado = 0
        for i in lecturaJSON():

            NAME_TEXT = defaultFont.render(i["nombre"], True, "White")
            NAME_RECT = NAME_TEXT.get_rect(center=(150, (175+espaciado)))
            screen.blit(NAME_TEXT, NAME_RECT)
            SCORE_TEXT = defaultFont.render(str(i["puntaje"]), True, "White")
            SCORE_RECT = SCORE_TEXT.get_rect(center=(650, (175+espaciado)))
            screen.blit(SCORE_TEXT, SCORE_RECT)

            espaciado += 25



        RECORDS_BACK = Button(image=None, pos=(400, 550),
                            text_input="ATRÁS", font=pygame.font.Font( pygame.font.get_default_font(), 25), base_color="White", hovering_color="Green")

        RECORDS_BACK.changeColor(RECORDS_MOUSE_POS)
        RECORDS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RECORDS_BACK.checkForInput(RECORDS_MOUSE_POS):
                    menuInicio()

        pygame.display.update()

def main(dificultad):
    listaCorrectas = []

    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    candidata = ""
    diccionario = []
    palabrasAcertadas = []

    #lee el diccionario
    lectura(diccionario)

    #elige las 7 letras al azar y una de ellas como principal
    letrasEnPantalla = dame7Letras(dificultad)
    letraPrincipal = dameLetra(letrasEnPantalla)

    #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
    while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))< MINIMO):
        letrasEnPantalla = dame7Letras(dificultad)
        letraPrincipal = dameLetra(letrasEnPantalla)

    print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario))

    #dibuja la pantalla la primera vez
    dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

    while segundos > fps/1000:
    # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                candidata += letra   #va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata)-1] #borra la ultima
                if e.key == K_RETURN:  #presionó enter
                    puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, listaCorrectas)
                    candidata = ""

        segundos = TIEMPO_MAX - totaltime/1000 #reemplaza pygame.time.get_ticks() por totaltime para que no corra el tiempo mientras se esta en el menu principal

        #Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        #Dibujar de nuevo todo
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)

        pygame.display.flip()

    finDelJuego(puntos) #pantalla de final del juego

    while 1:
        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

menuInicio()
