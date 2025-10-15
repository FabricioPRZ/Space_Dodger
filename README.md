# 🚀 Space Dodger

Un juego arcade de naves espaciales desarrollado en Python con Pygame. Esquiva asteroides, recoge power-ups y alcanza la puntuación más alta.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Raspberry%20Pi-lightgrey.svg)

## 🎮 Características

- ✨ Gráficos simples y coloridos
- 🎯 Sistema de puntuación y vidas
- 💚 Power-ups coleccionables
- ⚡ Optimizado para Raspberry Pi
- 🎹 Controles intuitivos con teclado
- 🔄 Mecánica de invulnerabilidad temporal

## 🕹️ Controles

- **WASD** o **Flechas**: Mover la nave
- **ESPACIO** o **ENTER**: Iniciar/Reiniciar juego
- **ESC**: Salir al menú o cerrar el juego

## 📋 Requisitos

- Python 3.8 o superior
- Pygame 2.0 o superior

## 🐧 Instalación en Linux / Raspberry Pi

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/space-dodger.git
cd space-dodger
```

### 2. Instalar dependencias

#### En Ubuntu/Debian/Raspberry Pi OS:
```bash
sudo apt update
sudo apt install python3-pygame
```

#### En Fedora:
```bash
sudo dnf install python3-pygame
```

#### En Arch Linux:
```bash
sudo pacman -S python-pygame
```

#### Usando pip (alternativa):
```bash
pip3 install pygame
```

### 3. Ejecutar el juego

```bash
python3 main.py
```

#### Hacer ejecutable (opcional):
```bash
chmod +x main.py
./main.py
```

## 🪟 Instalación en Windows

### 1. Instalar Python

- Descarga Python desde [python.org](https://www.python.org/downloads/)
- **IMPORTANTE:** Durante la instalación, marca la casilla **"Add Python to PATH"**

### 2. Clonar o descargar el repositorio

#### Opción A - Con Git:
```bash
git clone https://github.com/tuusuario/space-dodger.git
cd space-dodger
```

#### Opción B - Descarga directa:
- Descarga el ZIP desde GitHub
- Extrae el archivo
- Abre CMD o PowerShell en la carpeta extraída

### 3. Instalar Pygame

```bash
python -m pip install pygame
```

**Si tienes problemas con Python 3.14+**, usa una versión específica:
```bash
python -m pip install pygame==2.5.2
```

O instala Python 3.12 desde [python.org/downloads](https://www.python.org/downloads/)

### 4. Ejecutar el juego

```bash
python main.py
```

## 📁 Estructura del Proyecto

```
space-dodger/
├── main.py          # Archivo principal (ejecutar este)
├── config.py        # Configuración y constantes
├── jugador.py       # Clase Jugador
├── asteroide.py     # Clase Asteroide
├── powerup.py       # Clase PowerUp
├── pantallas.py     # Pantallas de inicio y game over
├── utils.py         # Funciones de utilidad
└── README.md        # Este archivo
```

## 🎯 Cómo Jugar

1. **Objetivo**: Esquiva los asteroides grises que caen del cielo
2. **Puntuación**: 
   - +10 puntos por cada asteroide que pasa
   - +50 puntos por cada power-up verde recogido
3. **Power-ups**: Los cubos verdes te dan puntos extra y restauran una vida
4. **Vidas**: Empiezas con 3 vidas. Pierdes una vida por cada colisión con un asteroide
5. **Game Over**: El juego termina cuando pierdes todas tus vidas

## 🔧 Solución de Problemas

### Error: "pygame module not found"
```bash
# Linux/Raspberry Pi
sudo apt install python3-pygame

# Windows
python -m pip install pygame
```

### Error: "command not found: python"
```bash
# Intenta con python3
python3 main.py

# O verifica la instalación
python --version
python3 --version
```

### El juego va lento en Raspberry Pi
- Asegúrate de estar usando Raspberry Pi OS Lite o versión optimizada
- Cierra otras aplicaciones
- El juego está optimizado para 60 FPS, debería funcionar bien en Pi 3 y superior

### Error de compilación en Windows con Python 3.14
```bash
# Instala una versión específica pre-compilada
python -m pip install pygame==2.5.2

# O instala Python 3.12 desde python.org
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📝 Ideas para Mejoras

- [ ] Sistema de niveles con dificultad incremental
- [ ] Diferentes tipos de power-ups (escudo, velocidad, etc.)
- [ ] Tabla de puntuaciones altas guardadas
- [ ] Efectos de sonido y música
- [ ] Diferentes tipos de enemigos
- [ ] Modo multijugador local
- [ ] Disparos para destruir asteroides


## 👤 Autor

**Victor Fabricio Pérez Constantino**
- GitHub: [@FabricioPRZ](https://github.com/FabricioPRZ)

## 🌟 Agradecimientos

- Pygame Community por la excelente documentación
- Inspirado en los clásicos juegos arcade de los 80s

---

**¡Disfruta el juego y que tengas suerte esquivando asteroides!** 🚀✨
