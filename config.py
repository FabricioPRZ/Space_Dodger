"""
Configuración global del juego
Colores, dimensiones y constantes
"""

import pygame

pygame.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 50, 50)
VERDE = (50, 255, 50)
AZUL = (50, 150, 255)
AMARILLO = (255, 255, 100)
GRIS = (100, 100, 100)

# FPS
FPS = 60

# Fuentes
fuente_grande = pygame.font.Font(None, 72)
fuente_media = pygame.font.Font(None, 48)
fuente_pequena = pygame.font.Font(None, 36)