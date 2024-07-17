import pygame

# Inicializar a pygame
pygame.init()

# Crear la pantalla con un ancho y un largo definido
pantalla = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Invasion Espacial", )

# Crear un loop hasta que mi evento de cierre se ejecute
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        # evento tipo QUIT - hacer click en la x
        if evento.type == pygame.QUIT:
            se_ejecuta = False


