import pygame
import os
from pyfiles.cardclasses.Card import Card

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)


class Visualizer:
    def __init__(self, card, screen):
        pygame.init()
        self.__card = card
        self.__path = os.getcwd()
        self.__numberFont = pygame.font.SysFont("gabriola", 75)
        self.__nameFont = pygame.font.SysFont("gabriola", 38)
        self.__descriptionFont = pygame.font.SysFont("gabriola", 20)
        self.__labelFont = pygame.font.SysFont("gabriola", 25)
        self.__screen = screen
        self.__namePlaceholder = pygame.Rect(0, 0, 410, 40)
        self.__descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
        self.__labelPlaceholder = pygame.Rect(0, 0, 175, 25)
        self.__costPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__attackPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__healthPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__nameText = self.__card.get_name()
        self.__descriptionText = self.__card.get_description()
        self.__labelText = self.__card.get_label()
        self.__costText = None
        self.__attackText = None
        self.__healthText = None
        self.update_number_text_values()
        print(self.__card.get_rarity())

    def update_number_text_values(self):
        self.__costText = str(self.__card.get_cost())
        units = ["Bastion", "Hero", "Lord", "Pawn", "Token"]
        if self.__card.get_unit() in units:
            if self.__card.get_unit() == "Bastion":
                self.__attackText = None
                self.__healthText = str(self.__card.get_health())
            else:
                self.__attackText = str(self.__card.get_attack())
                self.__healthText = str(self.__card.get_health())

    # Loads and puts the card template into a rectangle
    def load_template(self):
        template_img = pygame.image.load(self.__card.get_template())
        template_img = pygame.transform.scale(template_img.convert(), (430, 600))
        template_rect = template_img.get_rect()
        # template_rect.center = screenWidth // 2, screenHeight // 2
        return template_img, template_rect
    # cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
    # cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
    # cardRect.templateRect = cardImg.get_rect()
    # cardRect.templateRect.center = screenWidth // 2, screenHeight // 2

    # Loads and puts the rarity image into a rectangle
    def load_rarity(self):
        rarity_img = pygame.image.load(self.__card.get_rarity())
        rarity_img = pygame.transform.scale(rarity_img.convert(), (31, 31))
        rarity_rect = rarity_img.get_rect()
        return rarity_img, rarity_rect
    # rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
    # rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
    # rarityRect = rarityImg.get_rect()

    # Loads and puts the artwork into a rectangle
    def load_artwork(self):
        artwork_img = pygame.image.load(self.__card.get_image())
        artwork_img = pygame.transform.scale(artwork_img.convert(), (312, 366))
        artwork_rect = artwork_img.get_rect()
        return artwork_img, artwork_rect
    # artworkImg = pygame.image.load(os.getcwd() + "/../cardart/bluepawn.jpg")
    # artworkImg = pygame.transform.scale(artworkImg.convert(), (312, 366))
    # artworkRect = artworkImg.get_rect()

    def draw_text(self, surface, text, color, placeholder_rect, font, aa=True):
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

    def visualizer(self):
        card_template_img, card_template_rect = self.load_template()
        rarity_loaded_img, rarity_img_rect = self.load_rarity()
        artwork_loaded_img, artwork_img_rect = self.load_artwork()

        running = True
        # moving = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Lets you move the card around the screen
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if card_template_rect.collidepoint(event.pos):
                #         moving = True
                # elif event.type == pygame.MOUSEBUTTONUP:
                #     moving = False
                # elif event.type == pygame.MOUSEMOTION and moving:
                #     card_template_rect.move_ip(event.rel)

            # Sets the position for the different images
            rarity_img_rect.center = card_template_rect.x + 403, card_template_rect.y + 25
            artwork_img_rect.center = card_template_rect.centerx + 16, card_template_rect.y + 226

            # Sets the rectangle position for text labels
            self.__namePlaceholder.center = card_template_rect.centerx, card_template_rect.centery + 140
            self.__descriptionPlaceholder.center = card_template_rect.centerx, card_template_rect.centery + 199
            self.__labelPlaceholder.center = card_template_rect.centerx + 2, card_template_rect.centery + 275

            # If-Statements determine where to put the rectangle based on which number is printed due to the numbers
            # being different sizes because of the font
            # 1, 2 are center of box
            # 3, 4, 5, 7, 9 are lower
            # 6, 8 are upper
            # Cost numbers
            if self.__costText == "1" or self.__costText == "2":
                self.__costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 267
            elif self.__costText == "6" or self.__costText == "8":
                self.__costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 260
            else:
                self.__costPlaceholder.center = card_template_rect.centerx - 178, card_template_rect.centery - 272

            # Attack numbers
            if self.__attackText == "1" or self.__attackText == "2":
                self.__attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 259
            elif self.__attackText == "6" or self.__attackText == "8":
                self.__attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 265
            else:
                self.__attackPlaceholder.center = card_template_rect.centerx - 176, card_template_rect.centery + 254

            # Health numbers
            if self.__healthText == "1" or self.__healthText == "2":
                self.__healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 261
            elif self.__healthText == "6" or self.__healthText == "8":
                self.__healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 266
            else:
                self.__healthPlaceholder.center = card_template_rect.centerx + 179, card_template_rect.centery + 255

            # Images
            self.__screen.fill(GRAY)
            self.__screen.blit(card_template_img, card_template_rect)
            self.__screen.blit(rarity_loaded_img, rarity_img_rect)
            self.__screen.blit(artwork_loaded_img, artwork_img_rect)

            # Text labels
            self.draw_text(self.__screen, self.__nameText, BLACK, self.__namePlaceholder, self.__nameFont)
            self.draw_text(self.__screen, self.__descriptionText, BLACK, self.__descriptionPlaceholder, self.__descriptionFont)
            self.draw_text(self.__screen, self.__labelText, WHITE, self.__labelPlaceholder, self.__labelFont)

            # Number labels
            self.draw_text(self.__screen, self.__costText, WHITE, self.__costPlaceholder, self.__numberFont)
            self.draw_text(self.__screen, self.__attackText, WHITE, self.__attackPlaceholder, self.__numberFont)
            self.draw_text(self.__screen, self.__healthText, WHITE, self.__healthPlaceholder, self.__numberFont)

            # Displays everything on the screen
            pygame.display.update()


# pygame.init()
# screenWidth = 1200
# screenHeight = 800
# screen = pygame.display.set_mode((screenWidth, screenHeight))

# Setting font and text size for each text type
# numberFont = pygame.font.SysFont("gabriola", 75)
# nameFont = pygame.font.SysFont("gabriola", 38)
# descriptionFont = pygame.font.SysFont("gabriola", 20)
# labelFont = pygame.font.SysFont("gabriola", 25)

# Placeholders for text
# namePlaceholder = pygame.Rect(0, 0, 410, 40)
# descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
# labelPlaceholder = pygame.Rect(0, 0, 175, 25)
# costPlaceholder = pygame.Rect(0, 0, 75, 75)
# attackPlaceholder = pygame.Rect(0, 0, 75, 75)
# healthPlaceholder = pygame.Rect(0, 0, 75, 75)

# Text values to be put on card
# nameText = "Elder Cleric"
# descriptionText = "Guard (While this card is rested you may redirect attacks to this card. While this card is in the Kingdom it cannot \"Guard\" units on the battlefield) \"To be healthy and look this good for 120? Not bad\""
# labelText = "Pawn - Human Magi"
# costText = "5"
# attackText = "4"
# healthText = "6"