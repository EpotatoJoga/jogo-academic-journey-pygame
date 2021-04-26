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

    def draw(self,window):
        self.group.draw(window)

    def amin(self, image, tick, frames):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0
            self.frame += 1
        if self.frame > frames:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")

class Nave(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def move_nave(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0]
            self.sprite.rect[1] = pygame.mouse.get_pos()[1]


