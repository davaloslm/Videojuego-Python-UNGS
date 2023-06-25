import pygame, json, operator
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == 241: #AGREGAR Ñ
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
        sonidoReloj()
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 130
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_TIEMPO_FINAL), (pos, 100))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS), (pos, 100))
        pos = pos + TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))


def estanTodas(palabra, cadenaLetras):

    for letra in palabra:
        if letra  not in cadenaLetras:
           return False
    return True

#manejo de botones
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)



#sonidos

def sonidoAcierto():
    acierto = pygame.mixer.Sound('sonidos/acierto.mp3')
    acierto.play(0)

# sonido de error

def sonidoError():
    error = pygame.mixer.Sound('./sonidos/error.mp3')
    error.play(0)

#sonido de reloj
def sonidoReloj():
    fin = pygame.mixer.Sound('./sonidos/reloj.mp3')
    fin.play(0)

# sonido de fin

def sonidoFin():
    fin = pygame.mixer.Sound('./sonidos/fin.mp3')
    fin.play(0)

#guardado y lectura de puntajes en archivo JSON

def lecturaJSON():
    archivo = open("puntajes.json", "r")

    #guardar la cadena leida convertida en lista
    listaPuntajes = json.loads(archivo.read())

    #ordenar la lista por puntajes (de mayor a menor)

    listaPuntajes = sorted(listaPuntajes, key=operator.itemgetter('puntaje') , reverse=True)

    archivo.close()

    return listaPuntajes

def escrituraJSON(nombre, puntaje, lista):

    #solo admite 20 caracteres para el nombre. si tiene más, se recorta
    if len(nombre) > 20:
        nombre = nombre[:20]

    registro = {"nombre": nombre.upper(), "puntaje": puntaje}

    listaPuntajes = lecturaJSON()

    #agregar el nuevo puntaje
    listaPuntajes.append(registro)

    #ordenar la lista por puntajes (de mayor a menor) y quitar el ultimo(para mostrar solo los 10 mejores)
    listaPuntajes = sorted(listaPuntajes, key=operator.itemgetter('puntaje') , reverse=True)
    listaPuntajes.pop(10)

    #sobreescribir el archivo
    archivo = open("puntajes.json", "w")
    archivo.write(json.dumps(listaPuntajes)) #guarda la lista como JSON string

    archivo.close()

    return listaPuntajes

#guardar en una lista las palabras correctas ingresadas por el usuario.
def correctas(palabraCorrecta, listaCorrectas):

    listaCorrectas.append(palabraCorrecta)

    return listaCorrectas
