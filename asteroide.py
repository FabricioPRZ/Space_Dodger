"""
Clase Asteroide
Maneja los asteroides enemigos
"""

import pygame
import random
from config import ANCHO, ALTO, GRIS, ROJO

class Asteroide:
    def __init__(self):
        self.tam = random.randint(30, 60)
        self.x = random.randint(0, ANCHO - self.tam)
        self.y = -self.tam
        self.vel = random.randint(2, 5)
        
    def mover(self):
        """Mueve el asteroide hacia abajo"""
        self.y += self.vel
        
    def dibujar(self, surf):
        """Dibuja el asteroide"""
        pygame.draw.circle(surf, GRIS, 
                         (self.x + self.tam // 2, self.y + self.tam // 2), 
                         self.tam // 2)
        pygame.draw.circle(surf, ROJO, 
                         (self.x + self.tam // 2, self.y + self.tam // 2), 
                         self.tam // 2, 2)
        
    def obtener_rect(self):
        """Retorna el rectángulo de colisión"""
        return pygame.Rect(self.x, self.y, self.tam, self.tam)
    
    def fuera_pantalla(self):
        """Verifica si el asteroide salió de la pantalla"""
        return self.y > ALTO