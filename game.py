import pygame
from obj import Obj, Nave, Comando

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Nave("assets/nave1.png",630,750)
        self.comando = Comando("assets/comando1.png",50,760)
        #self.dial1 = Obj("assets/dialogo1.png",-400,220)
        self.vida = Obj("assets/vida3.png",0,0)
        self.change_scene = False

    def draw(self,window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.nave.draw(window)
        self.comando.draw(window)
        #self.dial1.draw(window)
        self.vida.draw(window)

    def update(self):
        self.move_bg()
        self.nave.amin("nave",2,2)
        self.comando.amin("comando",2,2)

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960



