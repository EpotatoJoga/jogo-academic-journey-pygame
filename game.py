from obj import Obj

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Obj("assets/nave1.png",640,800)
        self.ast1 = Obj("assets/asteroide4.png",610,250)
        self.skill1 = Obj("assets/skill1.png",1110,0)
        self.skill2 = Obj("assets/skill2.png", 950, 0)
        self.skill3 = Obj("assets/skill3.png", 790, 0)
        self.dial1 = Obj("assets/dialogo1.png",0,0)
        self.change_scene = False

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.nave.drawing(window)
        self.ast1.drawing(window)
        self.skill1.drawing(window)
        self.skill2.drawing(window)
        self.skill3.drawing(window)
        self.dial1.drawing(window)


    def update(self):
        self.move_bg()
        self.nave.amin()

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960
