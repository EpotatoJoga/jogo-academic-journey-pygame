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
        self.moveup = False
        self.movedown = False
        self.moveleft = False
        self.moveright = False
        self.dialogo = False

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.moveup = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.moveup = False
        if self.moveup:
            self.sprite.rect[1]-=15
        else:
            self.sprite.rect[1]+=0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.movedown = False
        if self.movedown:
            self.sprite.rect[1]+=15
        else:
            self.sprite.rect[1]+=0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.moveleft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.moveleft = False
        if self.moveleft:
            self.sprite.rect[0]-=15
        else:
            self.sprite.rect[0]+=0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.moveright = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.moveright = False
        if self.moveright:
            self.sprite.rect[0]+=15
        else:
            self.sprite.rect[0]+=0

class Dialogo(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def muddialo(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.dialogo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.dialogo = False
        if self.dialogo:
            self.sprite.rect[0] -= 200
        else:
            self.sprite.rect[0] -= 0

