import pygame
from menu import Menu
from jogo import Jogo

class Principal:

    def __init__(self, sizex, sizey, titulo):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("arquivos/tema.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.tela = pygame.display.set_mode([sizex, sizey])
        self.titulo = pygame.display.set_caption(titulo)
        self.fps = pygame.time.Clock()
        self.menu = Menu()
        self.jogo = Jogo()
        self.loop = True

    def eventos(self):
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                self.loop = False
            if not self.menu.mudar_cena:
                self.menu.eventos(eventos)
            elif not self.jogo.mudar_cena:
                self.jogo.nave.movimentacao_nave(eventos)
            self.jogo.nave.movimentacao_nave(eventos)
            self.jogo.dialogo(eventos)

    def draw(self):
        self.tela.fill([0, 0, 0])
        if not self.menu.mudar_cena:
            self.menu.draw(self.tela)
        elif not self.jogo.mudar_cena:
            self.jogo.draw(self.tela)
            self.jogo.atualizacoes()

    def atualizacoes(self):
        while self.loop:
            self.fps.tick(60)
            self.draw()
            self.eventos()
            pygame.display.update()

game = Principal(1280, 960, "A C A D E M I C     J O U R N E Y")
game.atualizacoes()
