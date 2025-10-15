"""
Clase PowerUp
Maneja los power-ups coleccionables
"""

import pygame
import random
from config import ANCHO, ALTO, VERDE, AMARILLO

class PowerUp:
    def __init__(self):
        self.tam = 30
        self.x = random.randint(0, ANCHO - self.tam)
        self.y = -self.tam
        self.vel = 3
        
    def mover(self):
        """Mueve el power-up hacia abajo"""
        self.y += self.vel
        
    def dibujar(self, surf):
        """Dibuja el power-up"""
        pygame.draw.rect(surf, VERDE, (self.x, self.y, self.tam, self.tam))
        pygame.draw.rect(surf, AMARILLO, (self.x, self.y, self.tam, self.tam), 3)
        
    def obtener_rect(self):
        """Retorna el rectángulo de colisión"""
        return pygame.Rect(self.x, self.y, self.tam, self.tam)
    
    def fuera_pantalla(self):
        """Verifica si el power-up salió de la pantalla"""
        return self.y > ALTO