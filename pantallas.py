"""
Pantallas del juego
Inicio y Game Over
"""

import pygame
import sys
from config import *
from utils import dibujar_estrellas, generar_estrellas

def pantalla_inicio(pantalla, reloj):
    """Muestra la pantalla de inicio"""
    estrellas = generar_estrellas()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                    return
                    
        pantalla.fill(NEGRO)
        dibujar_estrellas(pantalla, estrellas)
        
        titulo = fuente_grande.render("SPACE DODGER", True, AZUL)
        rect_titulo = titulo.get_rect(center=(ANCHO // 2, ALTO // 3))
        pantalla.blit(titulo, rect_titulo)
        
        instruc1 = fuente_pequena.render("Usa WASD o Flechas para moverte", True, BLANCO)
        rect_inst1 = instruc1.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(instruc1, rect_inst1)
        
        instruc2 = fuente_pequena.render("Esquiva asteroides, recoge power-ups", True, VERDE)
        rect_inst2 = instruc2.get_rect(center=(ANCHO // 2, ALTO // 2 + 40))
        pantalla.blit(instruc2, rect_inst2)
        
        inicio = fuente_media.render("PRESIONA ESPACIO", True, AMARILLO)
        rect_inicio = inicio.get_rect(center=(ANCHO // 2, ALTO * 2 // 3))
        pantalla.blit(inicio, rect_inicio)
        
        pygame.display.flip()
        reloj.tick(FPS)

def pantalla_game_over(pantalla, reloj, puntos):
    """Muestra la pantalla de game over"""
    estrellas = generar_estrellas()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False
                    
        pantalla.fill(NEGRO)
        dibujar_estrellas(pantalla, estrellas)
        
        game_over = fuente_grande.render("GAME OVER", True, ROJO)
        rect_go = game_over.get_rect(center=(ANCHO // 2, ALTO // 3))
        pantalla.blit(game_over, rect_go)
        
        puntuacion = fuente_media.render(f"Puntos: {puntos}", True, BLANCO)
        rect_punt = puntuacion.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(puntuacion, rect_punt)
        
        reiniciar = fuente_pequena.render("ESPACIO - Jugar de nuevo", True, AMARILLO)
        rect_rein = reiniciar.get_rect(center=(ANCHO // 2, ALTO * 2 // 3))
        pantalla.blit(reiniciar, rect_rein)
        
        salir = fuente_pequena.render("ESC - Salir", True, BLANCO)
        rect_salir = salir.get_rect(center=(ANCHO // 2, ALTO * 2 // 3 + 40))
        pantalla.blit(salir, rect_salir)
        
        pygame.display.flip()
        reloj.tick(FPS)