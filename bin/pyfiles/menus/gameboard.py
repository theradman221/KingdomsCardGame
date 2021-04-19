import pygame
import sys

def bg():
    pygame.init()
    win = pygame.display.set_mode((900,900))
    bg_img = pygame.image.load()
    bg = pygame.transform.scale(bg_img,(900,900))



    run =  True
    while run:
        for event in pygame.event.get():
            pygame.display.update()

bg()