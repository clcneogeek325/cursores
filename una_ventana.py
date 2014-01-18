#!/usr/bin/python
# -*- coding: utf-8 -*-


import curses

inicio = curses.initscr()
egin_x = 20 ; begin_y = 7
height = 5 ; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
