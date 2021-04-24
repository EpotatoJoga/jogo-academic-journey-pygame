from obj import Obj

class Game:

    def __init__(self):

        self.bg = Obj("assets/espaco.png",0,0)
        self.bg2 = Obj("assets/espaco.png", 0, -960)
        self.change_scene = False

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)

    def update(self):
        self.bg.sprite.rect[1] += 5
        self.bg2.sprite.rect[1] += 5

        if self.bg.sprite.rect[1] >= 960:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -960

