from obj import Obj

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.nave = Obj("assets/nave1.png",630,750)
        self.comando = Obj("assets/comando1.png",50,960)
        self.dial1 = Obj("assets/dialogo1.png",40,220)
        self.change_scene = False

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.nave.drawing(window)
        self.comando.drawing(window)
        self.dial1.drawing(window)

    def update(self):
        self.move_bg()
        self.nave.aminanave()
        self.move_comando()
        self.comando.aminacomando()

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960

    def move_comando(self):
        self.comando.sprite.rect[1] -= 5
        if self.comando.sprite.rect[1] <= 570:
            self.comando.sprite.rect[1] = 570
            

