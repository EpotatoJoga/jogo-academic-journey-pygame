import pygame                                                      # Importando funções do Pygame
from menu import Menu                                              # Importando funções da Classe Menu
from jogo import Jogo                                              # Importando funções da Classe Jogo

class Principal:                                                   # Criação da Classe Principal

    def __init__(self, sizex, sizey, titulo):                      # Função de inicialização (com referências)
        #pygame.mixer.init()                                        # Inicializar sons
        #pygame.mixer.music.load("arquivos/tema.ogg")               # Carregar sons
        #pygame.mixer.music.set_volume(0.1)                         # Alterar volume do som
        #pygame.mixer.music.play(-1)                                # Número de repetições
        pygame.display.set_caption(titulo)                         # Gerar o título do jogo
        self.tela = pygame.display.set_mode([sizex, sizey])        # Gerar o tamanho da janela do jogo
        self.fps = pygame.time.Clock()                             # Função do pygame que gera um relogia interno
        self.menu = Menu()                                         # Importando a classe Menu para ser inicializada
        self.jogo = Jogo()                                         # Importando a classe Jogo para ser inicializada
        self.loop = True                                           # Variável boleana para que o jogo fique rodando

    def eventos(self):                                             # Função para analizar todos os eventos
        for eventos in pygame.event.get():                         # Laço FOR para obter os eventos
            if eventos.type == pygame.QUIT:                        # Se clicar no botão de fechar janela...
                self.loop = False                                  # A variável loop será mudada para falso e encerrará o jogo
            if not self.menu.mudar_cena:
                self.menu.eventos(eventos)
            elif not self.jogo.mudar_cena:
                self.jogo.nave.movimentacao_nave(eventos)
            self.jogo.nave.movimentacao_nave(eventos)
            self.jogo.dialogo(eventos)
            self.jogo.tiro.disparo(eventos)

    def draw(self):                                                 # Função para que seja gerado o fundo de tela corespondente
        self.tela.fill([0, 0, 0])                                   # Tela de game over
        if not self.menu.mudar_cena:                                # Se a variável de mudar tela do menu não for TRUE
            self.menu.draw(self.tela)                               # Continuar exibindo tela de fundo do menu
        elif not self.jogo.mudar_cena:                              # Se a variável de mudar tela do jogo não for TRUE
            self.jogo.draw(self.tela)                               # Continuar exibindo tela de fundo do jogo
            self.jogo.atualizacoes()                                # Continuar exibindo as atualizações do jogo

    def atualizacoes(self):
        while self.loop:
            self.fps.tick(60)
            self.draw()
            self.eventos()
            pygame.display.update()

game = Principal(1280, 960, "A C A D E M I C     J O U R N E Y")
game.atualizacoes()
