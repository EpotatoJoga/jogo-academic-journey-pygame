import pygame
from objetos import Objetos, Nave

class Menu:

    def __init__(self):
        self.menu = Objetos("arquivos/menu.png", 0, 0)
        self.mudar_cena = False

    def draw(self, tela):
        self.menu.group.draw(tela)

    def eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.mudar_cena = True
