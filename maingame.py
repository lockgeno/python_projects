import numpy
import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox
import time
class Rectangle(object):
    """docstring for Rectangle."""
    def __init__(self, x , y ):
        self.rect = pygame.rect.Rect((x, y,  20, 20))
        self.head = self.rect
        self.rect.x = x
        self.rect.y = y
        self.velx = 0
        self.vely = 0
        self.hposx = []
        self.hposy =[]
        self.tposx = []
        self.tposy =[]
        self.tail_snake_len = 0
        self.snake_len = 1
        self.hposx.append(x)
        self.hposy.append(y)
        self.tposx.append(x)
        self.tposy.append(y)



    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_LEFT]:
            if self.head.x > 0:
                self.velx = -10
            else:
                self.velx = 0
            self.vely = 0

        if key[pygame.K_RIGHT]:
            if self.head.x < 480:
                self.velx = 10
            else:
                self.velx = 0
            self.vely = 0
        if key[pygame.K_UP]:
            if self.head.y > 0:
                self.vely = -10
            else:
                self.vely = 0
            self.velx = 0
        if key[pygame.K_DOWN]:
            if self.head.y < 480:
                self.vely = 10
            else:
                self.vely = 0
            self.velx = 0
    def draw(self, surface):

        self.rect.x += self.velx
        self.rect.y += self.vely
        self.hposx.append(self.rect.x)
        self.hposy.append(self.rect.y)
        self.tposx.append(self.hposx[0])
        self.tposy.append(self.hposy[0])
        del self.hposx[0]
        del self.hposy[0]
        if self.snake_len > self.tail_snake_len:
            del self.tposx[0]
            del self.tposy[0]
        else:
            self.snake_len = self.snake_len + 1

        pygame.draw.rect(surface, (255, 255, 255), (self.hposx[0], self.hposy[0],  20, 20))
        if self.tail_snake_len > 0:
            for i in range(0, self.tail_snake_len, 1):
                pygame.draw.rect(surface, (255, 255, 255), (self.tposx[i], self.tposy[i],  20, 20))
    def grow(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.tposx[0], self.tposy[0],  20, 20))


class Random_box(object):
    """docstring forRandom_box."""

    def __init__(self):
        x = 200
        y = 200
        self.rect = pygame.rect.Rect((x, y,  15, 15))
        self.rect.x = x
        self.rect.y = y



    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

def main():

    pygame.init()
    Game_over = False
    x = 500
    y = 500
    display_surface = pygame.display.set_mode((x, y))
    player = Rectangle(250, 250)
    target = Random_box()
    clock = pygame.time.Clock()
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    count = 0


    font_style = pygame.font.SysFont(None, 50)
    def message(msg,color, x, y):
        mesg = font_style.render(msg, True, color)
        display_surface.blit(mesg, [x, y])
    while Game_over == False:
        Grow = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                player.handle_keys();

        display_surface.fill((0, 0, 0))
        player.draw(display_surface)
        target.draw(display_surface)
        if player.rect.x <= 0 or player.rect.x >= 480 or player.rect.y <= 0 or player.rect.y >= 480:
            Game_over = True
        if player.rect.colliderect(target.rect):
            #print(count)
            count = count + 1
            target.rect.x = random.randrange(70, 470)
            target.rect.y = random.randrange(70, 470)

            Grow = True

        #player.move()
        if Grow == True:
            player.grow(display_surface)
            player.tail_snake_len = player.tail_snake_len +1
        message("Score: " + str(count),red, 350, 0)
        pygame.display.update()
        clock.tick(30)
        while Game_over == True:
            message("You lost",red, 150, 200)
            message("Press r for new game",blue, 50, 250)
            message("Press e to exit",green, 100, 300)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        #print("test1")
                        main()
                    if event.key == pygame.K_e:
                        pygame.quit()
                        quit()


main()
