"""
Clase Jugador
Maneja la nave del jugador
"""

import pygame
from config import ANCHO, ALTO, AZUL, BLANCO

class Jugador:
    def __init__(self):
        self.ancho = 50
        self.alto = 50
        self.x = ANCHO // 2 - self.ancho // 2
        self.y = ALTO - 100
        self.vel = 5
        self.vidas = 3
        self.invulnerable = 0
        
    def mover(self, teclas):
        """Mueve el jugador según las teclas presionadas"""
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.vel
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.vel
            
        # Límites de pantalla
        self.x = max(0, min(self.x, ANCHO - self.ancho))
        self.y = max(0, min(self.y, ALTO - self.alto))
        
    def dibujar(self, surf):
        """Dibuja la nave del jugador"""
        if self.invulnerable % 10 < 5 or self.invulnerable == 0:
            # Nave (triángulo)
            puntos = [
                (self.x + self.ancho // 2, self.y),
                (self.x, self.y + self.alto),
                (self.x + self.ancho, self.y + self.alto)
            ]
            pygame.draw.polygon(surf, AZUL, puntos)
            pygame.draw.polygon(surf, BLANCO, puntos, 2)
            
    def obtener_rect(self):
        """Retorna el rectángulo de colisión"""
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)