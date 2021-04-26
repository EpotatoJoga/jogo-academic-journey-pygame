from obj import Obj, Nave
import pygame

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Nave("assets/nave1.png",630,750)
        self.comando = Obj("assets/comando1.png",40,960)
        self.dialogo1 = Obj("assets/dialogo1.png",-390,180)
        self.vida = Obj("assets/vida3.png",5,5)
        self.change_scene = False
        self.dialogo = False
        self.n = 1

    def draw(self,window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.nave.draw(window)
        self.comando.draw(window)
        self.dialogo1.draw(window)
        self.vida.draw(window)

    def update(self):
        self.move_bg()
        self.nave.amin("nave",2,2)
        self.comando.amin("comando",2,2)
        self.move_comando()

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960

    def move_comando(self):
        self.comando.sprite.rect[1] -= 3
        if self.comando.sprite.rect[1] <= 370:
            self.comando.sprite.rect[1] = 370

    def dial(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                self.dialogo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:
                self.dialogo = False
        if self.dialogo:
            self.dialogo1.sprite.kill()
            self.n +=1
            self.dialogo1 = Obj("assets/dialogo" + str(self.n) + ".png", 65, 30)
        else:
            pass


