import pygame

RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

# print(pygame.font.get_fonts())
font = pygame.font.SysFont("freesansbold.ttf", 85)
numberSurface = pygame.font.Font.render(font, "2", True, WHITE)

cardImg = pygame.image.load("C:/Users/logan/KingdomsDevFiles/KingdomsCardGame/bin/cardtemplates/units/blueUnitTemplate.jpg")
cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))

cardRect = cardImg.get_rect()
cardRect.center = screenWidth // 2, screenHeight // 2

rarityImg = pygame.image.load("C:/Users/logan/KingdomsDevFiles/KingdomsCardGame/bin/cardtemplates/Raritys/Common.png")
rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))

rarityRect = rarityImg.get_rect()

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

    rarityRect.x = cardRect.x + 388
    rarityRect.y = cardRect.y + 10

    screen.fill(GRAY)
    screen.blit(cardImg, cardRect)
    screen.blit(rarityImg, rarityRect)
    # pygame.draw.rect(screen, WHITE, (cardRect.x + 6, cardRect.y + 5, 62, 62),1)
    screen.blit(numberSurface, (cardRect.x + 21, cardRect.y + 9))
    screen.blit(numberSurface, (cardRect.x + 23, cardRect.y + 534))
    screen.blit(numberSurface, (cardRect.x + 379, cardRect.y + 535))

    pygame.display.update()

pygame.quit()
quit()
