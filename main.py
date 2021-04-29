import pygame
from menu import Menu
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/tema.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.menu = Menu()
        self.game = Game()
        self.loop = True
        self.fps = pygame.time.Clock()

    def eventos(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.nave.move_nave(events)

            self.game.nave.move_nave(events)
            self.game.move_dialiogo(events)
            self.game.move_comando(events)

    def draw(self):
        self.window.fill([0,0,0])
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.eventos()
            pygame.display.update()

game = Main(1280, 960, "A C A D E M I C     J O U R N E Y")
game.update()
