#!/usr/bin/env python3
"""
Space Dodger - Archivo Principal
Juego compatible con Raspberry Pi
"""

import pygame
import sys
from config import *
from jugador import Jugador
from asteroide import Asteroide
from powerup import PowerUp
from pantallas import pantalla_inicio, pantalla_game_over
from utils import dibujar_estrellas, generar_estrellas

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Dodger")
reloj = pygame.time.Clock()

def juego_principal():
    """Bucle principal del juego"""
    jugador = Jugador()
    asteroides = []
    powerups = []
    puntos = 0
    contador_frames = 0
    estrellas = generar_estrellas()
    
    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return puntos
                    
        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)
        
        # Crear asteroides
        contador_frames += 1
        if contador_frames % 40 == 0:
            asteroides.append(Asteroide())
        
        # Crear power-ups ocasionalmente
        if contador_frames % 200 == 0:
            powerups.append(PowerUp())
            
        # Mover y actualizar asteroides
        for ast in asteroides[:]:
            ast.mover()
            if ast.fuera_pantalla():
                asteroides.remove(ast)
                puntos += 10
            elif jugador.invulnerable == 0 and jugador.obtener_rect().colliderect(ast.obtener_rect()):
                jugador.vidas -= 1
                jugador.invulnerable = 60
                asteroides.remove(ast)
                if jugador.vidas <= 0:
                    jugando = False
                    
        # Mover y actualizar power-ups
        for pw in powerups[:]:
            pw.mover()
            if pw.fuera_pantalla():
                powerups.remove(pw)
            elif jugador.obtener_rect().colliderect(pw.obtener_rect()):
                puntos += 50
                jugador.vidas = min(jugador.vidas + 1, 5)
                powerups.remove(pw)
                
        # Reducir invulnerabilidad
        if jugador.invulnerable > 0:
            jugador.invulnerable -= 1
            
        # Dibujar todo
        pantalla.fill(NEGRO)
        dibujar_estrellas(pantalla, estrellas)
        
        for ast in asteroides:
            ast.dibujar(pantalla)
            
        for pw in powerups:
            pw.dibujar(pantalla)
            
        jugador.dibujar(pantalla)
        
        # HUD
        texto_puntos = fuente_pequena.render(f"Puntos: {puntos}", True, BLANCO)
        pantalla.blit(texto_puntos, (10, 10))
        
        texto_vidas = fuente_pequena.render(f"Vidas: {jugador.vidas}", True, ROJO)
        pantalla.blit(texto_vidas, (10, 50))
        
        pygame.display.flip()
        reloj.tick(FPS)
        
    return puntos

def main():
    """Función principal que controla el flujo del juego"""
    while True:
        pantalla_inicio(pantalla, reloj)
        puntos_finales = juego_principal()
        if not pantalla_game_over(pantalla, reloj, puntos_finales):
            break
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()