import pygame
from menu import Menu

class Main:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu()

        self.loop = True

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            self.menu.events(events)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

game = Main(1280, 960, "A C A D E M I C     J O U R N E Y")
game.update()
