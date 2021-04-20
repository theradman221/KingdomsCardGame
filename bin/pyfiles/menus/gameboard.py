import pygame
import sys
import os


WIDTH, HEIGHT = 1920,1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gameboard")
GRAY = (75,75,75)
FPS = 60
print(os.getcwd())
backGround_Image = pygame.image.load(os.getcwd() + '\gameboard\gameboard.jpg')
backGround_Image = pygame.transform.scale(backGround_Image, (1520, 1080))

def draw_window():
    WIN.fill(GRAY)
    WIN.blit(backGround_Image, (200, 0))
    pygame.display.update()

def bg():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()



if __name__ == "__main__":
    bg()