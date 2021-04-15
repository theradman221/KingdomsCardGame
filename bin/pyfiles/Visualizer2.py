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
descriptionFont = pygame.font.SysFont("gabriola", 20)
labelFont = pygame.font.SysFont("gabriola", 25)

cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
cardRect = cardImg.get_rect()
cardRect.center = screenWidth // 2, screenHeight // 2

namePlaceholder = pygame.Rect(0, 0, 410, 40)
nameText = "Elder Cleric"

descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
descriptionText = "Guard (While this card is rested you may redirect attacks to this card. While this card is in the Kingdom it cannot \"Guard\" units on the battlefield) \"To be healthy and look this good for 120? Not bad\""


def drawText(surface, text, color, placeholderRect, font, aa=True, bkg=None):
    y = placeholderRect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > placeholderRect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < placeholderRect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        textRect = image.get_rect()
        textRect.centerx = placeholderRect.centerx
        textRect.centery = placeholderRect.centery
        surface.blit(image, (textRect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


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

        namePlaceholder.center = cardRect.centerx, cardRect.centery + 140
        descriptionPlaceholder.center = cardRect.centerx, cardRect.centery + 199

        screen.fill(GRAY)
        screen.blit(cardImg, cardRect)

        drawText(screen, nameText, BLACK, namePlaceholder, nameFont)
        pygame.draw.rect(screen, BLACK, namePlaceholder, 1)

        drawText(screen, descriptionText, BLACK, descriptionPlaceholder, descriptionFont)
        pygame.draw.rect(screen, BLACK, descriptionPlaceholder, 1)

        pygame.display.update()

visualizer()
pygame.quit()
quit()
