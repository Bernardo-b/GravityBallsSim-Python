# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:56:14 2021

@author: Bernardo
"""

import pygame
import time
from math import sin
from random import randint
from classes import Circle
from constants import *


def render(balls,screen):
    screen.fill(branco)
    for i in balls:
        i.draw(screen)
    pygame.display.update()




pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
ball = Circle()
balls = [Circle() for i in range(15)]


while 1:
    
    # for to quit game
    ev = pygame.event.get() 
    for e in ev:
        if e.type == pygame.MOUSEBUTTONUP:
            pygame.quit()
    for i in balls: 
        x,y = pygame.mouse.get_pos()
        i.applyForces(x,y)
    for i in balls: i.applyPhisics()
    render(balls,screen)
    