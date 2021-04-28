# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:56:33 2021

@author: Bernardo
"""

from random import randint
import pygame
from constants import *


class Circle():
    def __init__(self):
        self.position = [randint(200,800),randint(400,500)]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.force = [0,0]
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.radius = randint(10,100)
        
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,0)
        
    def applyPhisics(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position = list(map(int,self.position))
        
    def applyForces(self,x,y):
        self.force[0] = (x-self.position[0])-(self.velocity[0]*amortConst*self.radius)
        self.force[1] = (y-self.position[1])-(self.velocity[1]*amortConst*self.radius)
        self.acceleration[0] = self.force[0]/((self.radius**2)*massConst)
        self.acceleration[1] = self.force[1]/((self.radius**2)*massConst)