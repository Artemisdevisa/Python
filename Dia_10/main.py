import pygame

# Inicializar a pygame
pygame.init()

# Crear la pantalla con un ancho y un largo definido / ancho y largo
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Artemis")
icono = pygame.image.load("64x64.ico")
pygame.display.set_icon(icono)

# Jugador
img_jugdor = pygame.image.load("nave.png")
jugador_x = 368
jugador_y = 536

def jugador(x, y):
    pantalla.blit(img_jugdor, (x, y))

# Crear un loop del juego
se_ejecuta = True
while se_ejecuta:
    # Asignar fondo RGB al juego
    pantalla.fill((205, 104, 228))

    jugador_x -= 0.1

    for evento in pygame.event.get():
        # evento tipo QUIT - hacer click en la x
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador(jugador_x, jugador_y)

    # Actualizar pantalla para que se muestre el fondo
    pygame.display.update()



