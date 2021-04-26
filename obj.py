import pygame

class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.frame = 1
        self.tick = 0

    def drawing(self,window):
        self.group.draw(window)

    def aminanave(self):
        self.tick += 1
        if self.tick >= 5:
            self.tick = 0
            self.frame += 1
        self.frame += 1
        if self.frame > 2:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/nave" + str(self.frame) + ".png")

    def aminacomando(self):
        self.tick += 1
        if self.tick >= 5:
            self.tick = 0
            self.frame += 1
        self.frame += 1
        if self.frame > 2:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/comando" + str(self.frame) + ".png")




