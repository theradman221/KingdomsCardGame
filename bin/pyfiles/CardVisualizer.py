import pygame
import os

RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

numberFont = pygame.font.Font("freesansbold.ttf", 58)
nameFont = pygame.font.Font("freesansbold.ttf", 32)
descriptionFont = pygame.font.Font("freesansbold.ttf", 24)
labelFont = pygame.font.Font("freesansbold.ttf", 16)

costText = numberFont.render("5", True, WHITE)
costRect = costText.get_rect()

costRect.center = (costRect.width//2, costRect.height//2)

attackText = numberFont.render("4", True, WHITE)
attackRect = attackText.get_rect()

healthText = numberFont.render("6", True, WHITE)
healthRect = healthText.get_rect()

nameText = nameFont.render("Elder Cleric", True, BLACK)
nameRect = nameText.get_rect()

descriptionText = descriptionFont.render("Description", True, BLACK)
descriptionRect = descriptionText.get_rect()

labelText = labelFont.render("Pawn - Human Magi", True, WHITE)
labelRect = labelText.get_rect()
# print(pygame.font.get_fonts())
# font = pygame.font.SysFont("freesansbold.ttf", 85)
# numberSurface = pygame.font.Font.render(font, "2", True, WHITE)


# cardImg = pygame.image.load("C:/Users/derrick/KingdomsDev/KingdomsCardGame/bin/cardtemplates/units/blueUnitTemplate.jpg")
cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueunitTemplate.jpg")
cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
cardRect = cardImg.get_rect()
cardRect.center = screenWidth // 2, screenHeight // 2

# rarityImg = pygame.image.load("C:/Users/derrick/KingdomsDev/KingdomsCardGame/bin/cardtemplates/Raritys/Uncommon.png")
rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
rarityRect = rarityImg.get_rect()


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

        # rarityRect.x, rarityRect.y = cardRect.x + 388, cardRect.y + 10
        rarityRect.center = cardRect.x + 403, cardRect.y + 25
        nameRect.center = cardRect.centerx, cardRect.centery + 138
        costRect.center = cardRect.x + 37, cardRect.y + 39
        attackRect.center = cardRect.x + 39, cardRect.y + 563
        healthRect.center = cardRect.x + 394, cardRect.y + 564
        descriptionRect.center = cardRect.centerx, cardRect.centery + 200
        labelRect.center = cardRect.centerx, cardRect.centery + 276

        screen.fill(GRAY)
        screen.blit(cardImg, cardRect)
        screen.blit(rarityImg, rarityRect)

        screen.blit(costText, costRect)
        screen.blit(nameText, nameRect)
        screen.blit(attackText, attackRect)
        screen.blit(healthText, healthRect)
        screen.blit(descriptionText, descriptionRect)
        screen.blit(labelText, labelRect)

        # screen.blit(numberSurface, (cardRect.x + 21, cardRect.y + 9))
        # screen.blit(numberSurface, (cardRect.x + 23, cardRect.y + 534))
        # screen.blit(numberSurface, (cardRect.x + 379, cardRect.y + 535))

        # screen.blit(costText, (cardRect.x + 21, cardRect.y + 9))
        # screen.blit(attackText, (cardRect.x + 23, cardRect.y + 534))
        # screen.blit(healthText, (cardRect.x + 379, cardRect.y + 535))

        # pygame.draw.rect(screen, WHITE, labelRect, 1)
        pygame.display.update()


visualizer()
pygame.quit()
quit()
