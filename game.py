import pygame
from obj import Obj, Nave
import random

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Nave("assets/nave1.png",630,750)
        self.comando = Obj("assets/comando1.png",40,960)
        self.dialogo = Obj("assets/dialogo0.png",0,0)
        self.armadura5 = Obj("assets/armadura5.png",10,10)
        self.armadura4 = Obj("assets/armadura4.png", 10, 10)
        self.armadura3 = Obj("assets/armadura3.png", 10, 10)
        self.armadura2 = Obj("assets/armadura2.png", 10, 10)
        self.armadura1 = Obj("assets/armadura1.png", 10, 10)
        self.planetar = Obj("assets/pr1.png",910,-440)
        self.planetab = Obj("assets/pb1.png",10,-320)
        self.change_scene = False
        self.dialog = False
        self.comand = False
        self.comand1 = False
        self.dn = 0
        self.pbn = 1
        self.prn = 1

    def draw(self,window):
        self.bg.draw(window)
        self.bg2.draw(window)
        self.nave.draw(window)
        self.comando.draw(window)
        self.dialogo.draw(window)
        self.armadura5.draw(window)
        self.armadura4.draw(window)
        self.armadura3.draw(window)
        self.armadura2.draw(window)
        self.armadura1.draw(window)
        self.planetar.draw(window)
        self.planetab.draw(window)

    def update(self):
        self.move_bg()
        self.nave.amin("nave",2,2)
        self.comando.amin("comando",2,2)
        self.planetasruins()
        self.planetasbons()
        self.nave.colisaoplanetas(self.planetar.group, "planetar")
        self.quarmadura()

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960

    def quarmadura(self):
        if self.nave.qarmadura == 4:
            self.armadura5.sprite.kill()
        if self.nave.qarmadura == 3:
            self.armadura4.sprite.kill()
        if self.nave.qarmadura == 2:
            self.armadura3.sprite.kill()
        if self.nave.qarmadura == 1:
            self.armadura2.sprite.kill()
        if self.nave.qarmadura == 0:
            self.change_scene = True

    def move_comando(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                self.comand = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP1:
                self.comand = False
        if self.comand:
            self.comando.sprite.rect[1] -= 3
            if self.comando.sprite.rect[1] <= 370:
                self.comando.sprite.rect[1] = 370
        else:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP0:
                self.comand1 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP0:
                self.comand1 = False
        if self.comand1:
            self.comando.sprite.rect[1] += 6
        else:
            pass

    def move_dialiogo(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                self.dialog = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:
                self.dialog = False
        if self.dialog:
            self.dialogo.sprite.kill()
            self.dn +=1
            self.dialogo = Obj("assets/dialogo" + str(self.dn) + ".png", 330, 120)
            #if self.n <= 2:
                #pygame.mixer.init()
                #self.sound_dialogo = pygame.mixer.Sound("assets/g" + str(self.n) + ".mpeg")
                #self.sound_dialogo.play()
        else:
            pass

    def planetasruins(self):
        if self.dn == 3:
            self.planetar.sprite.rect[1] += 7
        if self.planetar.sprite.rect[1] >= 660:
            if self.prn <= 4:
                self.planetar.sprite.kill()
                self.prn += 1
                self.planetar = Obj("assets/pr" + str(self.prn) + ".png", random.randrange(50,630), -440)

    def planetasbons(self):
        if self.dn == 3:
            self.planetab.sprite.rect[1] += 7
        if self.planetab.sprite.rect[1] >= 660:
            if self.pbn <= 5:
                self.planetab.sprite.kill()
                self.pbn += 1
                self.planetab = Obj("assets/pb" + str(self.prn) + ".png", random.randrange(50,630), -320)


