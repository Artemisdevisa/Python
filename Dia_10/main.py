import pygame
import random
import math
from pygame import mixer

# Inicializar a pygame
pygame.init()

# Crear la pantalla con un ancho y un largo definido / ancho y largo
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Artemis")
icono = pygame.image.load("64x64.ico")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo_juego.jpg")

# agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# variable del Jugador
img_jugdor = pygame.image.load("nave.png")
jugador_x = 368
jugador_y = 500
jugdor_x_cambio = 0

# variable del enemigo
img_enemigo_a = []
enemigo_a_x = []
enemigo_a_y = []
enemigo_a_x_cambio = []
enemigo_a_y_cambio = []
cantidad_enemigos = 11

for e in range(cantidad_enemigos):
    for e in range(cantidad_enemigos):
        img_enemigo_a.append(pygame.image.load(f"enemigo_{e+1}.png"))
    enemigo_a_x.append(random.randint(0, 768))
    enemigo_a_y.append(random.randint(50, 200))
    enemigo_a_x_cambio.append(0.5)
    enemigo_a_y_cambio.append(40)

# variable de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
# velocidad de la bala hacia arriba
bala_y_cambio = 3
bala_vicible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font('Tiny5-Regular.ttf', 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font('Tiny5-Regular.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (280, 200))

# función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (texto_x, texto_y))

# función jugador
def jugador(x, y):
    pantalla.blit(img_jugdor, (x, y))

# función enemigo_a
def enemigo_a(x, y, ene):
    pantalla.blit(img_enemigo_a[ene], (x, y))

# funcion disparar bala
def disparar_bala(x, y):
    global bala_vicible
    bala_vicible = True
    pantalla.blit(img_bala, (x + 20, y + 10))


# función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# Crear un loop del juego
se_ejecuta = True
while se_ejecuta:
    # Asignar fondo RGB al juego
    pantalla.blit(fondo, (0,0))

    # iterar eventos
    for evento in pygame.event.get():
        # evento tipo QUIT - hacer click en la x
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento para saber si se presiona las flechas
        if evento.type == pygame.KEYDOWN:
            # evento que sabe si presiona la tecla izquierda
            if evento.key == pygame.K_LEFT:
                jugdor_x_cambio = -1
            # evento que sabe si presiona la tecla derecha
            if evento.key == pygame.K_RIGHT:
                jugdor_x_cambio = 1
            # evento para presionar la barra espacidora, para aparecer la bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_vicible:
                  bala_x = jugador_x
                  disparar_bala(bala_x, bala_y)

        # evento para saber si se suelta las flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugdor_x_cambio = 0

    # modificar ubicacion del jugador
    jugador_x += jugdor_x_cambio

    # mantener dentro de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # si la bala ya llego al limite superior, se hace invicible y regresa a 500
    if bala_y <= -32:
        bala_y = 500
        bala_vicible = False

    # movimiento bala y subida hacia arriba
    if bala_vicible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # -----------------------------------------

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        if enemigo_a_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_a_y[k] = 1000
            texto_final()
            break

        enemigo_a_x[e] += enemigo_a_x_cambio[e]

        # mantener dentro de los bordes al enemigo
        if enemigo_a_x[e] <= 0:
            # si choca actualizar el cambio por si esta en -0.3
            enemigo_a_x_cambio[e] = 1
            enemigo_a_y[e] += enemigo_a_y_cambio[e]
        elif enemigo_a_x[e] >= 768:
            # si choca actualiza el cambio en reversa
            enemigo_a_x_cambio[e] = -1
            enemigo_a_y[e] += enemigo_a_y_cambio[e]

        # colisión
        colision = hay_colision(enemigo_a_x[e], enemigo_a_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_vicible = False
            puntaje += 1
            enemigo_a_x[e] = random.randint(0, 768)
            enemigo_a_y[e] = random.randint(50, 200)

        enemigo_a(enemigo_a_x[e], enemigo_a_y[e], e)

    # -----------------------------------------
    # llamar funciones para todos los personajes
    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # actualizar todos
    pygame.display.update()



