#Este codigo se hizo con intencion de jugar Minicraf java con un mando de consola generico
#tambien sirve como raton provisional si el progrma ranca con el sistema o de forma manual con el teclado

import pygame
import pyautogui
import time

# Inicializar pygame
pygame.init()
pygame.joystick.init()

# Detectar mando
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Mando detectado: {joystick.get_name()}")

# Configuración de teclas y botones
botones_teclas = {
    0: "space",   # A → Espacio
    1: "e",       # B → E
    2: "w",       # X → W
    3: "s",       # Y → S
    9: "shift",   # L1 → Mayúsculas
    10: "ctrl",   # R1 → Ctrl (ejemplo)
}

# Botones del ratón
botones_raton = {
    7: "left",    # Joystick izquierdo apretado → Click izquierdo
    8: "right",   # Joystick derecho apretado → Click derecho
}

# Cruceta
cruceta = {
    11: "up",
    12: "down",
    13: "left",
    14: "right"
}

# Sensibilidad del joystick derecho para movimiento del ratón
sensibilidad_raton = 15

print("Listo. Usa el mando para controlar el teclado y ratón.\n")

while True:
    for evento in pygame.event.get():
        # Pulsar botones
        if evento.type == pygame.JOYBUTTONDOWN:
            boton = evento.button
            if boton in botones_teclas:
                pyautogui.keyDown(botones_teclas[boton])
            elif boton in botones_raton:
                pyautogui.mouseDown(button=botones_raton[boton])
            elif boton in cruceta:
                print(f"Cruceta: {cruceta[boton]}")

        # Soltar botones
        elif evento.type == pygame.JOYBUTTONUP:
            boton = evento.button
            if boton in botones_teclas:
                pyautogui.keyUp(botones_teclas[boton])
            elif boton in botones_raton:
                pyautogui.mouseUp(button=botones_raton[boton])

    # Leer ejes (joystick izquierdo/derecho)
    eje_izq_x = joystick.get_axis(0)
    eje_izq_y = joystick.get_axis(1)
    eje_der_x = joystick.get_axis(2)
    eje_der_y = joystick.get_axis(3)

    # Mover el ratón con el joystick derecho
    if abs(eje_der_x) > 0.2 or abs(eje_der_y) > 0.2:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + eje_der_x * sensibilidad_raton, y + eje_der_y * sensibilidad_raton)

    time.sleep(0.01)
                                                                                                                                    