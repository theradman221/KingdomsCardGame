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
        # self.__numberFont = pygame.font.SysFont("gabriola", 25)
        # self.__nameFont = pygame.font.SysFont("gabriola", 12)
        # self.__descriptionFont = pygame.font.SysFont("gabriola", 6)
        # self.__labelFont = pygame.font.SysFont("gabriola", 7)
        self.__numberFont = pygame.font.SysFont("gabriola", 10) # 75
        self.__nameFont = pygame.font.SysFont("gabriola", 5) # 38
        self.__descriptionFont = pygame.font.SysFont("gabriola", 1) # 20
        self.__labelFont = pygame.font.SysFont("gabriola", 4) # 23
        self.__screen = screen
        self.__masterX = 20
        self.__masterY = 20
        # self.__masterWidth = 143 #430
        # self.__masterHeight = 200 #600
        self.__masterWidth = 107  # 430 / 4
        self.__masterHeight = 92  # 600 / 6.5
        # self.__namePlaceholder = pygame.Rect(0, 0, 137, 13)
        # self.__descriptionPlaceholder = pygame.Rect(0, 0, 137, 25)
        # self.__labelPlaceholder = pygame.Rect(0, 0, 58, 8)
        # self.__costPlaceholder = pygame.Rect(0, 0, 25, 25)
        # self.__attackPlaceholder = pygame.Rect(0, 0, 25, 25)
        # self.__healthPlaceholder = pygame.Rect(0, 0, 25, 25)
        self.__namePlaceholder = pygame.Rect(0, 0, 102, 6)
        self.__descriptionPlaceholder = pygame.Rect(0, 0, 102, 11)
        self.__labelPlaceholder = pygame.Rect(0, 0, 44, 4)
        self.__costPlaceholder = pygame.Rect(0, 0, 19, 11)
        self.__attackPlaceholder = pygame.Rect(0, 0, 19, 11)
        self.__healthPlaceholder = pygame.Rect(0, 0, 19, 11)
        self.__nameText = self.__card.get_name()
        self.__descriptionText = self.__card.get_description()
        self.__labelText = self.__card.get_label()
        self.__costText = None
        self.__attackText = None
        self.__healthText = None
        self.__scale_up = False
        self.__rotateCard = False
        self.__card_template_img, self.__card_template_rect = self.load_template()
        self.__rarity_loaded_img, self.__rarity_img_rect = self.load_rarity()
        self.__artwork_loaded_img, self.__artwork_img_rect = self.load_artwork()
        self.update_number_text_values()

    def get_card(self):
        return self.__card

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
        if self.__rotateCard:
            return pygame.transform.rotate(template_img, 90), template_rect
        else:
            return template_img, template_rect
    # cardImg = pygame.image.load(os.getcwd() + "/../cardtemplates/units/blueUnitTemplate.jpg")
    # cardImg = pygame.transform.scale(cardImg.convert(), (430, 600))
    # cardRect.templateRect = cardImg.get_rect()
    # cardRect.templateRect.center = screenWidth // 2, screenHeight // 2

    # Loads and puts the rarity image into a rectangle
    def load_rarity(self):
        rarity_img = pygame.image.load(self.__card.get_rarity())
        if self.__scale_up:
            rarity_img = pygame.transform.scale(rarity_img.convert(), (31, 31))
        else:
            # rarity_img = pygame.transform.scale(rarity_img.convert(), (10, 10))
            rarity_img = pygame.transform.scale(rarity_img.convert(), (8, 5))
        rarity_rect = rarity_img.get_rect()
        if self.__rotateCard:
            return pygame.transform.rotate(rarity_img, 90), rarity_rect
        else:
            return rarity_img, rarity_rect
    # rarityImg = pygame.image.load(os.getcwd() + "/../cardtemplates/Raritys/Uncommon.png")
    # rarityImg = pygame.transform.scale(rarityImg.convert(), (31, 31))
    # rarityRect = rarityImg.get_rect()

    # Loads and puts the artwork into a rectangle
    def load_artwork(self):
        artwork_img = pygame.image.load(self.__card.get_image())
        if self.__scale_up:
            artwork_img = pygame.transform.scale(artwork_img.convert(), (312, 366))
        else:
            # artwork_img = pygame.transform.scale(artwork_img.convert(), (104, 122))
            artwork_img = pygame.transform.scale(artwork_img.convert(), (78, 56))
        artwork_rect = artwork_img.get_rect()
        if self.__rotateCard:
            return pygame.transform.rotate(artwork_img, 90), artwork_rect
        else:
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
            # Rotate text here
            if self.__rotateCard:
                surface.blit(pygame.transform.rotate(image, 90), (text_rect.left, y))
            else:
                surface.blit(image, (text_rect.left, y))
            y += font_height + line_spacing

            # Removes the row of text from the text variable that was just blitted
            text = text[i:]
        return text

    def text_rectangle_positions(self):
        # Sets the position for the different images
        if self.__scale_up:
            if self.__rotateCard:
                self.__rarity_img_rect.center = self.__card_template_rect.x + 24, self.__card_template_rect.y + 25
            else:
                self.__rarity_img_rect.center = self.__card_template_rect.x + 403, self.__card_template_rect.y + 25
        else:
            if self.__rotateCard:
                self.__rarity_img_rect.center = self.__card_template_rect.x + 9, self.__card_template_rect.y + 8
            else:
                # self.__rarity_img_rect.center = self.__card_template_rect.x + 134, self.__card_template_rect.y + 9
                self.__rarity_img_rect.center = self.__card_template_rect.x + 100, self.__card_template_rect.y + 3.5
        if self.__scale_up:
            if self.__rotateCard:
                self.__artwork_img_rect.center = self.__card_template_rect.centerx - 16, self.__card_template_rect.y + 226
            else:
                self.__artwork_img_rect.center = self.__card_template_rect.centerx + 16, self.__card_template_rect.y + 226
        else:
            if self.__rotateCard:
                self.__artwork_img_rect.center = self.__card_template_rect.centerx - 4, self.__card_template_rect.y + 74
            else:
                # self.__artwork_img_rect.center = self.__card_template_rect.centerx + 6, self.__card_template_rect.y + 76
                self.__artwork_img_rect.center = self.__card_template_rect.centerx + 5, self.__card_template_rect.y + 35

        # Sets the rectangle position for text labels
        if self.__scale_up:
            if self.__rotateCard:
                self.__namePlaceholder.center = self.__card_template_rect.centerx + 314, self.__card_template_rect.centery - 180
            else:
                self.__namePlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 140
        else:
            if self.__rotateCard:
                self.__namePlaceholder.center = self.__card_template_rect.centerx + 103, self.__card_template_rect.centery - 58
            else:
                # self.__namePlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 46
                self.__namePlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 22
        if self.__scale_up:
            if self.__rotateCard:
                self.__descriptionPlaceholder.center = self.__card_template_rect.centerx + 450, self.__card_template_rect.centery - 250
            else:
                self.__descriptionPlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 199
        else:
            if self.__rotateCard:
                self.__descriptionPlaceholder.center = self.__card_template_rect.centerx + 151, self.__card_template_rect.centery - 86
            else:
                # self.__descriptionPlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 66
                self.__descriptionPlaceholder.center = self.__card_template_rect.centerx, self.__card_template_rect.centery + 31
        units = ["Bastion", "Terra", "TerraLandMark"]
        if self.__card.get_unit() not in units:
            if self.__scale_up:
                if self.__rotateCard:
                    self.__labelPlaceholder.center = self.__card_template_rect.centerx + 425, self.__card_template_rect.centery - 155
                else:
                    self.__labelPlaceholder.center = self.__card_template_rect.centerx + 4, self.__card_template_rect.centery + 277
            else:
                if self.__rotateCard:
                    self.__labelPlaceholder.center = self.__card_template_rect.centerx + 141, self.__card_template_rect.centery - 51
                else:
                    # self.__labelPlaceholder.center = self.__card_template_rect.centerx + 1, self.__card_template_rect.centery + 92
                    self.__labelPlaceholder.center = self.__card_template_rect.centerx + 1, self.__card_template_rect.centery + 43

        # If-Statements determine where to put the rectangle based on which number is printed due to the numbers
        # being different sizes because of the font
        # 1, 2 are center of box
        # 3, 4, 5, 7, 9 are lower
        # 6, 8 are upper
        # Cost numbers
        if self.__scale_up:
            if self.__costText == "1" or self.__costText == "2":
                if self.__rotateCard:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 208, self.__card_template_rect.centery + 118
                else:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 267
            elif self.__costText == "6" or self.__costText == "8":
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 260
            else:
                if self.__rotateCard:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 210, self.__card_template_rect.centery + 118
                else:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 178, self.__card_template_rect.centery - 272
        else:
            if self.__costText == "1" or self.__costText == "2":
                if self.__rotateCard:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 69, self.__card_template_rect.centery + 39
                else:
                    # self.__costPlaceholder.center = self.__card_template_rect.centerx - 58, self.__card_template_rect.centery - 90
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 43.5, self.__card_template_rect.centery - 42
            elif self.__costText == "6" or self.__costText == "8":
                # self.__costPlaceholder.center = self.__card_template_rect.centerx - 59, self.__card_template_rect.centery - 87
                self.__costPlaceholder.center = self.__card_template_rect.centerx - 43.5, self.__card_template_rect.centery - 40
            else:
                if self.__rotateCard:
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 69, self.__card_template_rect.centery + 38
                else:
                    # self.__costPlaceholder.center = self.__card_template_rect.centerx - 58, self.__card_template_rect.centery - 91
                    self.__costPlaceholder.center = self.__card_template_rect.centerx - 43.5, self.__card_template_rect.centery - 42

        # Attack numbers
        if self.__scale_up:
            if self.__attackText == "1" or self.__attackText == "2":
                if self.__rotateCard:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx + 319, self.__card_template_rect.centery + 115
                else:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 259
            elif self.__attackText == "6" or self.__attackText == "8":
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 265
            else:
                if self.__rotateCard:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx + 317, self.__card_template_rect.centery + 114
                else:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx - 176, self.__card_template_rect.centery + 254
        else:
            if self.__attackText == "1" or self.__attackText == "2" or self.__attackText == "0":
                if self.__rotateCard:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx + 107, self.__card_template_rect.centery + 38
                else:
                    # self.__attackPlaceholder.center = self.__card_template_rect.centerx - 58, self.__card_template_rect.centery + 86
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx - 43, self.__card_template_rect.centery + 40
            elif self.__attackText == "6" or self.__attackText == "8":
                # self.__attackPlaceholder.center = self.__card_template_rect.centerx - 59, self.__card_template_rect.centery + 88
                self.__attackPlaceholder.center = self.__card_template_rect.centerx - 43, self.__card_template_rect.centery + 41
            else:
                if self.__rotateCard:
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx + 106, self.__card_template_rect.centery + 37
                else:
                    # self.__attackPlaceholder.center = self.__card_template_rect.centerx - 57, self.__card_template_rect.centery + 84
                    self.__attackPlaceholder.center = self.__card_template_rect.centerx - 43, self.__card_template_rect.centery + 39

        # Health numbers
        if self.__scale_up:
            if self.__healthText == "1" or self.__healthText == "2":
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 319, self.__card_template_rect.centery - 240
                else:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 261
            elif self.__healthText == "6" or self.__healthText == "8":
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 329, self.__card_template_rect.centery - 240
                else:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 266
            else:
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 317, self.__card_template_rect.centery - 240
                else:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 179, self.__card_template_rect.centery + 255
        else:
            if self.__healthText == "1" or self.__healthText == "2" or self.__attackText == "0":
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 107, self.__card_template_rect.centery - 81
                else:
                    # self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 87
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 45, self.__card_template_rect.centery + 40
            elif self.__healthText == "6" or self.__healthText == "8":
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 110, self.__card_template_rect.centery - 81
                else:
                    # self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 89
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 45, self.__card_template_rect.centery + 41
            else:
                if self.__rotateCard:
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 106, self.__card_template_rect.centery - 81
                else:
                    # self.__healthPlaceholder.center = self.__card_template_rect.centerx + 60, self.__card_template_rect.centery + 85
                    self.__healthPlaceholder.center = self.__card_template_rect.centerx + 45, self.__card_template_rect.centery + 39

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

    def visualizer(self, rotate):
        self.__scale_up = False
        self.__rotateCard = rotate
        self.__card_template_img, self.__card_template_rect = self.load_template()
        self.__rarity_loaded_img, self.__rarity_img_rect = self.load_rarity()
        self.__artwork_loaded_img, self.__artwork_img_rect = self.load_artwork()
        self.text_rectangle_positions()
        self.blitting_card_values()

    def scale_card_up(self, rotate):
        self.__scale_up = True
        self.__rotateCard = rotate
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
