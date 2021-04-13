import pygame
import os

RED = (255,0,0)
GRAY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screenWidth = 1200
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

numberFont = pygame.font.SysFont("gabriola", 70)
nameFont = pygame.font.SysFont("gabriola", 38)
descriptionFont = pygame.font.SysFont("gabriola", 30)
labelFont = pygame.font.SysFont("gabriola", 25)

cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
cardRect = cardImg.get_rect()
cardRect.center = screenWidth // 2, screenHeight // 2

# descriptionText = descriptionFont.render("This is my description", True, BLACK)
# descriptionBox = descriptionText.get_rect()

text = "Guard (While this card is rested you may redirect attacks to this\ncard. While this card is in the Kingdom it cannot \"Guard\" units on\nthe battlefield)\n\"To be healthy and look this good for 120? Not bad\""




def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def visualizer():
    running = True
    moving = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cardRect.collidepoint(event.pos):
                    moving = True
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
            elif event.type == pygame.MOUSEMOTION and moving:
                cardRect.move_ip(event.rel)

        # descriptionBox.center = cardRect.centerx, cardRect.centery + 190

        screen.fill(GRAY)
        screen.blit(cardImg, cardRect)
        # screen.blit(descriptionText, descriptionBox)

        blit_text(screen, text, (cardRect.centerx - 50, cardRect.centery + 172), descriptionFont, BLACK)

        pygame.display.update()

visualizer()
pygame.quit()
quit()
