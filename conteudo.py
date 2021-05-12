import pygame                                                        # Importando funções do Pygame

class Conteudo:                                                      # Criação da Classe Conteúdo

    def __init__(self, imagem, x, y):                                # Função para inicializar tudo dentro da classe (com referências)
        self.group = pygame.sprite.Group()                           # Criação do grupo
        self.personagens = pygame.sprite.Sprite(self.group)          # Para adicionar  os personagens (imagens) ao grupo
        self.personagens.image = pygame.image.load(imagem)           # Carregar uma imagem
        self.personagens.rect = self.personagens.image.get_rect()    # Recebe a variavel de cima para definir posição na tela
        self.personagens.rect[0] = x                                 # Posição da imagem no eixo X
        self.personagens.rect[1] = y                                 # Posição da imagem no eixo Y
        self.movimento_cima = False                                  #
        self.movimento_baixo = False                                 #
        self.movimento_esquerda = False                              #
        self.movimento_direita = False                               # Variáveis boleanas para teclas de movimentação da nave
        self.teclaenter = False                                      # Variável boleana quando for clicado tecla ENTER
        self.tiro = False                                            # Variável boleana quando for clicado tecla de atirar
        self.quadros = 1                                             #
        self.marcacao = 0                                            # Variáveis para que possa ser geradas animações

    def draw(self, janela):                                          # Função para mostrar imagens na tela
        self.group.draw(janela)                                      # Mostra o grupo de imagem na tela

    def animacoes(self, imagem, marcacao, quadros):                  # Função para gerar animação
        self.marcacao += 1
        if self.marcacao == marcacao:
            self.marcacao = 0
            self.quadros += 1
        if self.quadros > quadros:
            self.quadros = 1
        self.personagens.image = pygame.image.load("arquivos/" + imagem + str(self.quadros) + ".png")

class Nave(Conteudo):

    def __init__(self, imagem, x, y):
        super().__init__(imagem, x, y)
        self.contagem_armadura = 5
        self.contagem_discernimento = 0
        self.contagem_resiliencia = 0
        self.contagem_enter = 0

    def movimentacao_nave(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.movimento_cima = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                self.movimento_cima = False
        if self.movimento_cima:
            self.personagens.rect[1]-=10
        else:
            self.personagens.rect[1]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                self.movimento_baixo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_s:
                self.movimento_baixo = False
        if self.movimento_baixo:
            self.personagens.rect[1]+=10
        else:
            self.personagens.rect[1]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                self.movimento_esquerda = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                self.movimento_esquerda = False
        if self.movimento_esquerda:
            self.personagens.rect[0]-=10
        else:
            self.personagens.rect[0]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                self.movimento_direita = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_d:
                self.movimento_direita = False
        if self.movimento_direita:
            self.personagens.rect[0]+=10
        else:
            self.personagens.rect[0]+=0

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                self.teclaenter = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RETURN:
                self.teclaenter = False
        if self.teclaenter:
            self.contagem_enter += 1
        else:
            pass

    def colisao_planetas(self, group, nome):
        nome = nome
        colisao_planetas = pygame.sprite.spritecollide(self.personagens, group, True)
        if nome == "planetainimigos" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "planetaaliados" and colisao_planetas:
            self.contagem_discernimento += 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/ponto.wav")
            self.som.play()
        if nome == "aste1" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "aste2" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nome == "aste3" and colisao_planetas:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()

    def colisao_asteroides(self, group, name):
        name = name
        colisao_asteroides = pygame.sprite.spritecollide(self.personagens, group, True)
        if (name == "gggg" or name == "ggg" or name == "gg" or name == "g" or name == "aste11" or name == "aste22" or name == "aste33") and colisao_asteroides:
            self.contagem_armadura -= 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if name == "r" and colisao_asteroides:
            self.contagem_resiliencia += 1
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/ponto.wav")
            self.som.play()

class Tiro(Conteudo):

    def __init__(self, imagem, x, y):
        super().__init__(imagem, x, y)
        self.ok = False

    def disparo(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e:
                self.tiro = True
                pygame.mixer.init()
                pygame.mixer.music.set_volume(0.2)
                self.som_tiro = pygame.mixer.Sound("arquivos/tiro.ogg")
                self.som_tiro.play()
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_e:
                self.tiro = False
        if self.tiro:
            print("Tiro",self.tiro)
        else:
            pass

    def colisao_tiro(self, group, nomee):
        nomee = nomee
        colisao_tiro = pygame.sprite.spritecollide(self.personagens, group, False)
        if nomee == "planetainimigos" and colisao_tiro:
            self.personagens.kill()
        if nomee == "planetaaliados" and colisao_tiro:
            self.personagens.kill()

    def colisao_tiroast1(self, group, nomee):
        nomee = nomee
        colisao_tiro = pygame.sprite.spritecollide(self.personagens, group, True)
        if nomee == "aste1" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "aste2" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "aste3" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()

    def colisao_tiroo(self, group, nomee):
        nomee = nomee
        colisao_tiroo = pygame.sprite.spritecollide(self.personagens, group, True)
        if nomee == "gggg" and colisao_tiroo:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "ggg" and colisao_tiroo:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "gg" and colisao_tiroo:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "g" and colisao_tiroo:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()

    def colisao_tiroast2(self, group, nomee):
        nomee = nomee
        colisao_tiro = pygame.sprite.spritecollide(self.personagens, group, True)
        if nomee == "aste11" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "aste22" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()
        if nomee == "aste33" and colisao_tiro:
            self.personagens.kill()
            pygame.mixer.init()
            self.som = pygame.mixer.Sound("arquivos/explosao.flac")
            self.som.play()