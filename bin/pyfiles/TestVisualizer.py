import pygame
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)

# making cards 3x smaller


class TestVisualizer:
    def __init__(self, card, screen):
        pygame.init()
        self.__card = card
        self.__path = os.getcwd()
        self.__numberFont = pygame.font.SysFont("gabriola", 25)
        self.__nameFont = pygame.font.SysFont("gabriola", 12)
        self.__descriptionFont = pygame.font.SysFont("gabriola", 6)
        self.__labelFont = pygame.font.SysFont("gabriola", 7)
        self.__screen = screen
        self.__masterX = 20
        self.__masterY = 20
        self.__masterWidth = 143 #430
        self.__masterHeight = 200 #600
        self.__namePlaceholder = pygame.Rect(0, 0, 137, 13)
        self.__descriptionPlaceholder = pygame.Rect(0, 0, 137, 25)
        self.__labelPlaceholder = pygame.Rect(0, 0, 58, 8)
        self.__costPlaceholder = pygame.Rect(0, 0, 25, 25)
        self.__attackPlaceholder = pygame.Rect(0, 0, 25, 25)
        self.__healthPlaceholder = pygame.Rect(0, 0, 25, 25)
        self.__nameText = self.__card.get_name()
        self.__descriptionText = self.__card.get_description()
        self.__labelText = self.__card.get_label()
        self.__costText = None
        self.__attackText = None
        self.__healthText = None
        self.__card_template_img, self.__card_template_rect = self.load_template()
        self.__rarity_loaded_img, self.__rarity_img_rect = self.load_rarity()
        self.__artwork_loaded_img, self.__artwork_img_rect = self.load_artwork()
        self.update_number_text_values()

    def set_master_x(self, x):
        self.__masterX = x

    def set_master_y(self, y):
        self.__masterY = y

    def get_master_x(self):
        return self.__masterX

    def get_master_y(self):
        return self.__masterY

    def update_number_text_values(self):
        self.__costText = str(self.__card.get_cost())
        units = ["Hero", "Lord", "Pawn", "Token"]
        if self.__card.get_unit() in units:
            self.__attackText = str(self.__card.get_attack())
            self.__healthText = str(self.__card.get_health())

    # Loads and puts the card template into a rectangle
    def load_template(self):
        template_img = pygame.image.load(self.__card.get_template())
        template_img = pygame.transform.scale(template_img.convert(), (self.__masterWidth, self.__masterHeight))
        template_rect = template_img.get_rect()
        template_rect.topleft = self.__masterX, self.__masterY
        return template_img, template_rect
    # cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
    # cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
    # cardRect.templateRect = cardImg.get_rect()
    # cardRect.templateRect.center = screenWidth // 2, screenHeight // 2

    # Loads and puts the rarity image into a rectangle
    def load_rarity(self):
        rarity_img = pygame.image.load(self.__card.get_rarity())
        if self.scale_card_up():
            rarity_img = pygame.transform.scale(rarity_img.convert(), (31, 31))
        else:
            rarity_img = pygame.transform.scale(rarity_img.convert(), (10, 10))
        rarity_rect = rarity_img.get_rect()
        return rarity_img, rarity_rect
    # rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
    # rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
    # rarityRect = rarityImg.get_rect()

    # Loads and puts the artwork into a rectangle
    def load_artwork(self):
        artwork_img = pygame.image.load(self.__card.get_image())
        if self.scale_card_up():
            artwork_img = pygame.transform.scale(artwork_img.convert(), (312, 366))
        else:
            artwork_img = pygame.transform.scale(artwork_img.convert(), (104, 122))
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

            # Rendering the line and putting it into a rect object
            image = font.render(text[:i], aa, color)
            text_rect = image.get_rect()

            # Centering the rendered text
            text_rect.centerx = placeholder_rect.centerx
            text_rect.centery = placeholder_rect.centery

            # Blitting the text to the screen
            surface.blit(image, (text_rect.left, y))
            y += font_height + line_spacing

            # Removes the row of text from the text variable that was just blitted
            text = text[i:]
        return text

    def text_rectangle_positions(self):
        # Sets the position for the different images
        if self.scale_card_up():
            self.__rarity_img_rect.center = self.__card_template_rect.x + 403, self.__card_template_rect.y + 25
        else:
            self.__rarity_img_rect.center = self.__card_template_rect.x + 134, self.__card_template_rect.y + 9
        if self.scale_card_up():
            self.__artwork_img_rect.center = self.__card_template_rect.centerx + 16, self.__card_template_rect.y + 226
        else:
            self.__artwork_img_rect.center = self.__card_template_rect.centerx + 6, self.__card_template_rect.y + 76

        # Sets the rectangle position for text labels
        if self.scale_card_up():
            self.__namePlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 140
        else:
            self.__namePlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 46
        if self.scale_card_up():
            self.__descriptionPlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 199
        else:
            self.__descriptionPlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 66
        units = ["Bastion", "Terra", "TerraLandMark"]
        if self.__card.get_unit() not in units:
            if self.scale_card_up():
                self.__labelPlaceholder.center = self.__card_template_rect.centerx + 4, self.__card_template_rect.centery + 277
            else:
                self.__labelPlaceholder.center = self.__card_template_rect.centerx + 1, self.__card_template_rect.centery + 92

        # If-Statements determine where to put the rectangle based on which number is printed due to the numbers
        # being different sizes because of the font
        # 1, 2 are center of box
        # 3, 4, 5, 7, 9 are lower
        # 6, 8 are upper
        # Cost numbers
        if self.scale_card_up():
            if self.__costText == "1" or self.__costText == "2":
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 267
            elif self.__costText == "6" or self.__costText == "8":
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 260
            else:
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 272
        else:
            if self.__costText == "1" or self.__costText == "2":
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 59, self.__card_template_rect.centery - 90
            elif self.__costText == "6" or self.__costText == "8":
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 59, self.__card_template_rect.centery - 87
            else:
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 58, self.__card_template_rect.centery - 91

        # Attack numbers
        if self.scale_card_up():
            if self.__attackText == "1" or self.__attackText == "2":
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 259
            elif self.__attackText == "6" or self.__attackText == "8":
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 265
            else:
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 254
        else:
            if self.__attackText == "1" or self.__attackText == "2" or self.__attackText == "0":
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 58, self.__card_template_rect.centery + 86
            elif self.__attackText == "6" or self.__attackText == "8":
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 59, self.__card_template_rect.centery + 88
            else:
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 57, self.__card_template_rect.centery + 84

        # Health numbers
        if self.scale_card_up():
            if self.__healthText == "1" or self.__healthText == "2":
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 261
            elif self.__healthText == "6" or self.__healthText == "8":
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 266
            else:
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 255
        else:
            if self.__healthText == "1" or self.__healthText == "2" or self.__attackText == "0":
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 87
            elif self.__healthText == "6" or self.__healthText == "8":
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 89
            else:
                self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 85

    def blitting_card_values(self):
        # Images
        #self.__screen.fill(GRAY)
        self.__screen.blit(self.__card_template_img, self.__card_template_rect)
        self.__screen.blit(self.__rarity_loaded_img, self.__rarity_img_rect)
        self.__screen.blit(self.__artwork_loaded_img, self.__artwork_img_rect)

        # Text labels
        self.draw_text(self.__screen, self.__nameText, BLACK, self.__namePlaceholder, self.__nameFont)
        self.draw_text(self.__screen, self.__descriptionText, BLACK, self.__descriptionPlaceholder,
                       self.__descriptionFont)
        units = ["Bastion", "Terra", "TerraLandMark"]
        if self.__card.get_unit() not in units:
            self.draw_text(self.__screen, self.__labelText, WHITE, self.__labelPlaceholder, self.__labelFont)

        # Number labels
        self.draw_text(self.__screen, self.__costText, WHITE, self.__costPlaceholder, self.__numberFont)
        self.draw_text(self.__screen, self.__attackText, WHITE, self.__attackPlaceholder, self.__numberFont)
        self.draw_text(self.__screen, self.__healthText, WHITE, self.__healthPlaceholder, self.__numberFont)

        # pygame.display.update()

    def visualizer(self):
        self.__card_template_img, self.__card_template_rect = self.load_template()
        self.__rarity_loaded_img, self.__rarity_img_rect = self.load_rarity()
        self.__artwork_loaded_img, self.__artwork_img_rect = self.load_artwork()
        self.text_rectangle_positions()
        self.blitting_card_values()

    def scale_card_up(self):
        self.__numberFont = pygame.font.SysFont("gabriola", 75)
        self.__nameFont = pygame.font.SysFont("gabriola", 38)
        self.__descriptionFont = pygame.font.SysFont("gabriola", 20)
        self.__labelFont = pygame.font.SysFont("gabriola", 23)
        self.__masterWidth = 430
        self.__masterHeight = 600
        self.__namePlaceholder = pygame.Rect(0, 0, 410, 40)
        self.__descriptionPlaceholder = pygame.Rect(0, 0, 410, 75)
        self.__labelPlaceholder = pygame.Rect(0, 0, 175, 25)
        self.__costPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__attackPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__healthPlaceholder = pygame.Rect(0, 0, 75, 75)
        self.__card_template_img, self.__card_template_rect = self.load_template()
        self.__rarity_loaded_img, self.__rarity_img_rect = self.load_rarity()
        self.__artwork_loaded_img, self.__artwork_img_rect = self.load_artwork()
        self.text_rectangle_positions()
        self.blitting_card_values()