"""
Funciones de utilidad
Efectos visuales y helpers
"""

import pygame
import random
from config import ANCHO, ALTO, BLANCO

def generar_estrellas():
    """Genera posiciones aleatorias para las estrellas de fondo"""
    return [(random.randint(0, ANCHO), random.randint(0, ALTO)) for _ in range(100)]

def dibujar_estrellas(surf, estrellas):
    """Dibuja las estrellas de fondo"""
    for estrella in estrellas:
        pygame.draw.circle(surf, BLANCO, estrella, 1)