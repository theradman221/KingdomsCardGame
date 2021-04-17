import pygame
import os
from bin.pyfiles.cardclasses.Card import Card

RED = (255,0,0)
GRAY = (150,150,150)
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
screenWidth = 1200
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Setting font and text size for each text type
numberFont = pygame.font.SysFont("gabriola", 75)
nameFont = pygame.font.SysFont("gabriola", 38)
descriptionFont = pygame.font.SysFont("gabriola", 20)
labelFont = pygame.font.SysFont("gabriola", 25)

# Placeholders for text
namePlaceholder = pygame.Rect(0, 0, 410, 40)
descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
labelPlaceholder = pygame.Rect(0, 0, 175, 25)
costPlaceholder = pygame.Rect(0, 0, 75, 75)
attackPlaceholder = pygame.Rect(0, 0, 75, 75)
healthPlaceholder = pygame.Rect(0, 0, 75, 75)

# Text values to be put on card
nameText = "Elder Cleric"
descriptionText = "Guard (While this card is rested you may redirect attacks to this card. While this card is in the Kingdom it cannot \"Guard\" units on the battlefield) \"To be healthy and look this good for 120? Not bad\""
labelText = "Pawn - Human Magi"
costText = "5"
attackText = "4"
healthText = "6"


# Loads and puts the card template into a rectangle
def load_template(template_path):
    template_img = pygame.image.load(os.getcwd() + template_path)
    template_img = pygame.transform.scale(template_img.convert(), (430, 600))
    template_rect = template_img.get_rect()
    template_rect.center = screenWidth // 2, screenHeight // 2
    return template_img, template_rect
# cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
# cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
# cardRect.templateRect = cardImg.get_rect()
# cardRect.templateRect.center = screenWidth // 2, screenHeight // 2


# Loads and puts the rarity image into a rectangle
def load_rarity(rarity_path):
    rarity_img = pygame.image.load(os.getcwd() + rarity_path)
    rarity_img = pygame.transform.scale(rarity_img.convert(), (31, 31))
    rarity_rect = rarity_img.get_rect()
    return rarity_img, rarity_rect
# rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
# rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
# rarityRect = rarityImg.get_rect()


# Loads and puts the artwork into a rectangle
def load_artwork(artwork_path):
    artwork_img = pygame.image.load(os.getcwd() + artwork_path)
    artwork_img = pygame.transform.scale(artwork_img.convert(), (312, 366))
    artwork_rect = artwork_img.get_rect()
    return artwork_img, artwork_rect
# artworkImg = pygame.image.load(os.getcwd() + "/../cardart/bluepawn.jpg")
# artworkImg = pygame.transform.scale(artworkImg.convert(), (312, 366))
# artworkRect = artworkImg.get_rect()


def draw_text(surface, text, color, placeholder_rect, font, aa=True):
    y = placeholder_rect.top
    line_spacing = -2

    # Gets the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # Determines if the row of text will be outside the rectangle
        if y + font_height > placeholder_rect.bottom:
            break

        # Determines maximum width of line
        while font.size(text[:i])[0] < placeholder_rect.width and i < (len(text)):
            i += 1

        # Adjusts the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # Render the line and blit it to the surface
        image = font.render(text[:i], aa, color)

        text_rect = image.get_rect()
        text_rect.centerx = placeholder_rect.centerx
        text_rect.centery = placeholder_rect.centery
        surface.blit(image, (text_rect.left, y))
        y += font_height + line_spacing

        # Removes the row of text from the text variable that was just blitted
        text = text[i:]

    return text


def visualizer():
    card_template_img, card_template_rect = load_template("/../cardtemplates/units/blueUnitTemplate.jpg")
    rarity_loaded_img, rarity_img_rect = load_rarity("/../cardtemplates/Raritys/Uncommon.png")
    artwork_loaded_img, artwork_img_rect = load_artwork("/../cardart/bluepawn.jpg")
    
    running = True
    moving = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Lets you move the card around the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if card_template_rect.collidepoint(event.pos):
                    moving = True
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
            elif event.type == pygame.MOUSEMOTION and moving:
                card_template_rect.move_ip(event.rel)

        # Sets the position for the different images
        rarity_img_rect.center = card_template_rect.x + 403, card_template_rect.y + 25
        artwork_img_rect.center = card_template_rect.centerx + 16, card_template_rect.y + 226

        # Sets the rectangle position for text labels
        namePlaceholder.center = card_template_rect.centerx, card_template_rect.centery + 140
        descriptionPlaceholder.center = card_template_rect.centerx, card_template_rect.centery + 199
        labelPlaceholder.center = card_template_rect.centerx + 2, card_template_rect.centery + 275

        # If-Statements determine where to put the rectangle based on which number is printed due to the numbers
        # being different sizes because of the font
        # 1, 2 are center of box
        # 3, 4, 5, 7, 9 are lower
        # 6, 8 are upper
        # Cost numbers
        if costText == "1" or costText == "2":
            costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 267
        elif costText == "6" or costText == "8":
            costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 260
        else:
            costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 272

        # Attack numbers
        if attackText == "1" or attackText == "2":
            attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 259
        elif attackText == "6" or attackText == "8":
            attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 265
        else:
            attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 254

        # Health numbers
        if healthText == "1" or healthText == "2":
            healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 261
        elif healthText == "6" or healthText == "8":
            healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 266
        else:
            healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 255

        # Images
        screen.fill(GRAY)
        screen.blit(card_template_img, card_template_rect)
        screen.blit(rarity_loaded_img, rarity_img_rect)
        screen.blit(artwork_loaded_img, artwork_img_rect)

        # Text labels
        draw_text(screen, nameText, BLACK, namePlaceholder, nameFont)
        draw_text(screen, descriptionText, BLACK, descriptionPlaceholder, descriptionFont)
        draw_text(screen, labelText, WHITE, labelPlaceholder, labelFont)

        # Number labels
        draw_text(screen, costText, WHITE, costPlaceholder, numberFont)
        draw_text(screen, attackText, WHITE, attackPlaceholder, numberFont)
        draw_text(screen, healthText, WHITE, healthPlaceholder, numberFont)

        # Displays everything on the screen
        pygame.display.update()


visualizer()
pygame.quit()
quit()
