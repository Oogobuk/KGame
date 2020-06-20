import pygame
import random
import sys
import time
pygame.font.init()
pygame.init()

WIDTH = 1300
HEIGHT = 700
#BG = pygame.image.load("BG3.png")
BG = pygame.transform.scale(pygame.image.load("BG.png"),(WIDTH,HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

redString = "#b5be19"

class kevin(object):
    """docstring for kevin."""
    def __init__(self, arg):
        super(kevin, self).__init__()
        self.arg = arg
        

def main():
    health = 100
    myfont = pygame.font.SysFont("modern", 35)
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_Window():
        screen.blit(BG,(0, 0))
        
        
        health_level = myfont.render(f"Health: {health}", 1, (255,255,255))
        screen.blit(health_level,(10,10))
        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_Window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
main()