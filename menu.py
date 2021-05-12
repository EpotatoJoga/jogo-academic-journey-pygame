import pygame                                             # Importando funções do Pygame
from conteudo import Conteudo                             # Importando funções da Classe Conteudo

class Menu:                                               # Criação da Classe Menu

    def __init__(self):                                   # Função para inicializar tudo dentro da classe
        self.menu = Conteudo("arquivos/menu.png", 0, 0)
        self.mudar_cena = False

    def draw(self, tela):
        self.menu.group.draw(tela)

    def eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.mudar_cena = True
