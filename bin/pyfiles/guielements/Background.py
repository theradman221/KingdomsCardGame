import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        print("Made it into the background")
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        print("Left the background")