#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este el modulo requerido para trabajar con Curses
import curses
 
# Se crea un objeto de tipo window que abarca toda la pantalla e inicializa curses
fullscreen = curses.initscr()
 
# Dibuja un borde al rededor de los límites del window, el valor 0 indica usar el
# caracter por omisión para pintar el borde.
fullscreen.border(0)
 
# Se coloca el texto Hola Mundo desde Python Curses! aproximadamente en el centro
# de la pantalla, claro si esta es de 80x20
fullscreen.addstr(12, 25, "Hola Mundo desde Python curses!")
 
# Para que los cambios se muestren hay que usar refresh()
fullscreen.refresh()
 
# Se detiene el programa hasta que una tecla sea pulsada
fullscreen.getch()
 
# Se desactiva curses
curses.endwin()
