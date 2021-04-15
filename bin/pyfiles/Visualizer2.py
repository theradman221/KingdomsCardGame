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

cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
cardRect = cardImg.get_rect()
cardRect.center = screenWidth // 2, screenHeight // 2

rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
rarityRect = rarityImg.get_rect()

artworkImg = pygame.image.load(os.getcwd() + "/../cardart/bluepawn.jpg")
artworkImg = pygame.transform.scale(artworkImg.convert(), (312, 366))
artworkRect = artworkImg.get_rect()

numberFont = pygame.font.SysFont("gabriola", 75)
nameFont = pygame.font.SysFont("gabriola", 38)
descriptionFont = pygame.font.SysFont("gabriola", 20)
labelFont = pygame.font.SysFont("gabriola", 25)

namePlaceholder = pygame.Rect(0, 0, 410, 40)
nameText = "Elder Cleric"

descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
descriptionText = "Guard (While this card is rested you may redirect attacks to this card. While this card is in the Kingdom it cannot \"Guard\" units on the battlefield) \"To be healthy and look this good for 120? Not bad\""

labelPlaceholder = pygame.Rect(0, 0, 175, 25)
labelText = "Pawn - Human Magi"

costPlaceholder = pygame.Rect(0, 0, 75, 75)
costText = "5"

attackPlaceholder = pygame.Rect(0, 0, 75, 75)
attackText = "4"

healthPlaceholder = pygame.Rect(0, 0, 75, 75)
healthText = "6"
# going to need if statements to determine where to put the rectangles
# 1, 2 are center of box
# 3, 4, 5, 7, 9 are lower
# 6, 8 are upper


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
        while font.size(text[:i])[0] < placeholderRect.width and i < (len(text)):
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

        # Sets the position of images
        rarityRect.center = cardRect.x + 403, cardRect.y + 25
        artworkRect.center = cardRect.centerx + 16, cardRect.y + 226

        # Sets the rectangle position for text labels
        namePlaceholder.center = cardRect.centerx, cardRect.centery + 140
        descriptionPlaceholder.center = cardRect.centerx, cardRect.centery + 199
        labelPlaceholder.center = cardRect.centerx + 2, cardRect.centery + 275

        # If Statements determine where to put the rectangle based on which number is printed
        # Cost numbers
        if costText == "1" or costText == "2":
            costPlaceholder.center = cardRect.centerx - 178, cardRect.centery - 267
        elif costText == "6" or costText == "8":
            costPlaceholder.center = cardRect.centerx - 178, cardRect.centery - 260
        else:
            costPlaceholder.center = cardRect.centerx - 178, cardRect.centery - 272

        # Attack numbers
        if attackText == "1" or attackText == "2":
            attackPlaceholder.center = cardRect.centerx - 176, cardRect.centery + 259
        elif attackText == "6" or attackText == "8":
            attackPlaceholder.center = cardRect.centerx - 176, cardRect.centery + 265
        else:
            attackPlaceholder.center = cardRect.centerx - 176, cardRect.centery + 254

        # Health numbers
        if healthText == "1" or healthText == "2":
            healthPlaceholder.center = cardRect.centerx + 179, cardRect.centery + 261
        elif healthText == "6" or healthText == "8":
            healthPlaceholder.center = cardRect.centerx + 179, cardRect.centery + 266
        else:
            healthPlaceholder.center = cardRect.centerx + 179, cardRect.centery + 255

        # Images
        screen.fill(GRAY)
        screen.blit(cardImg, cardRect)
        screen.blit(rarityImg, rarityRect)
        screen.blit(artworkImg, artworkRect)

        # Text labels
        drawText(screen, nameText, BLACK, namePlaceholder, nameFont)
        drawText(screen, descriptionText, BLACK, descriptionPlaceholder, descriptionFont)
        drawText(screen, labelText, WHITE, labelPlaceholder, labelFont)

        # Number labels
        drawText(screen, costText, WHITE, costPlaceholder, numberFont)
        drawText(screen, attackText, WHITE, attackPlaceholder, numberFont)
        drawText(screen, healthText, WHITE, healthPlaceholder, numberFont)

        # Displays everything on the screen
        pygame.display.update()

visualizer()
pygame.quit()
quit()
