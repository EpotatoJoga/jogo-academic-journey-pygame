import pygame
from objetos import Objetos, Nave
import random

class Jogo:

    def __init__(self):
        self.fundo1 = Objetos("arquivos/espaco.png", 0, 0)
        self.fundo2 = Objetos("arquivos/espaco.png", 0, -960)
        self.nave = Nave("arquivos/nave1.png",630,750)
        self.comando = Objetos("arquivos/comando1.png", 40, 960)
        self.comandoo = Objetos("arquivos/comandoo1.png", 40, 960)
        self.dialogo1 = Objetos("arquivos/dialogo1.png", 330, 120)
        self.dialogo2 = Objetos("arquivos/dialogo4.png", 330, 120)
        self.armadura5 = Objetos("arquivos/armadura5.png", 10, 10)
        self.armadura4 = Objetos("arquivos/armadura4.png", 10, 10)
        self.armadura3 = Objetos("arquivos/armadura3.png", 10, 10)
        self.armadura2 = Objetos("arquivos/armadura2.png", 10, 10)
        self.armadura1 = Objetos("arquivos/armadura1.png", 10, 10)
        self.discernimento0 = Objetos("arquivos/disc0.png", 820, 10)
        self.discernimento1 = Objetos("arquivos/disc1.png", 820, 10)
        self.discernimento2 = Objetos("arquivos/disc2.png", 820, 10)
        self.discernimento3 = Objetos("arquivos/disc3.png", 820, 10)
        self.discernimento4 = Objetos("arquivos/disc4.png", 820, 10)
        self.discernimento5 = Objetos("arquivos/disc5.png", 820, 10)
        self.planetainimigo = Objetos("arquivos/pr1.png", 910, -320)
        self.planetaaliado = Objetos("arquivos/pb1.png", 10, -600)
        self.resiliencia0 = Objetos("arquivos/resili0.png", 824, 55)
        self.resiliencia1 = Objetos("arquivos/resili1.png", 824, 55)
        self.resiliencia2 = Objetos("arquivos/resili2.png", 824, 55)
        self.resiliencia3 = Objetos("arquivos/resili3.png", 824, 55)
        self.resiliencia4 = Objetos("arquivos/resili4.png", 824, 55)
        self.resiliencia5 = Objetos("arquivos/resili5.png",824,55)
        self.condecoracoes = Objetos("arquivos/condecoracoes.png", 1010, 755)
        self.condecoracao1 = Objetos("arquivos/condecoracao1.png", 1010, 790)
        #self.condecoracao2 = Objetos("arquivos/condecoracao2.png", 1100, 790)
        #self.condecoracao3 = Objetos("arquivos/condecoracao3.png", 1190, 790)
        self.mudar_cena = False
        self.boleana_dialogo = False
        self.contagem_dialogo1 = 1
        self.contagem_paliados = 1
        self.contagem_pinimigos = 1
        self.movimento_primeira()

    def draw(self, tela):
        self.fundo1.draw(tela)
        self.fundo2.draw(tela)
        self.nave.draw(tela)
        self.comando.draw(tela)
        if self.nave.contagem_discernimento == 5 and self.contagem_paliados == 6:
            self.comandoo.draw(tela)
        self.armadura5.draw(tela)
        self.armadura4.draw(tela)
        self.armadura3.draw(tela)
        self.armadura2.draw(tela)
        self.armadura1.draw(tela)
        if self.contagem_dialogo1 == 3:
            self.planetainimigo.draw(tela)
        if self.contagem_dialogo1 == 3:
            self.planetaaliado.draw(tela)
        if self.contagem_dialogo1 == 3:
            self.discernimento0.draw(tela)
        if self.nave.contagem_discernimento == 1:
            self.discernimento1.draw(tela)
        if self.nave.contagem_discernimento == 2:
            self.discernimento2.draw(tela)
        if self.nave.contagem_discernimento == 3:
            self.discernimento3.draw(tela)
        if self.nave.contagem_discernimento == 4:
            self.discernimento4.draw(tela)
        if self.nave.contagem_discernimento == 5:
            self.discernimento5.draw(tela)
        if self.comando.personagens.rect[1] == 370:
            self.dialogo1.draw(tela)
        if self.comandoo.personagens.rect[1] == 370:
            self.dialogo2.draw(tela)
            self.condecoracoes.draw(tela)
            self.condecoracao1.draw(tela)
            self.resiliencia0.draw(tela)

    def atualizacoes(self):
        self.movimento_fundo()
        self.nave.animacoes("nave", 2, 2)
        self.comando.animacoes("comando", 2, 2)
        self.comandoo.animacoes("comando",2,2)
        self.planetas_inimigos()
        self.planetas_aliados()
        self.nave.colisao_planetas(self.planetainimigo.group, "planetainimigos")
        self.nave.colisao_planetas(self.planetaaliado.group, "planetaaliados")
        self.quantidade_armadura()
        self.quantidade_disernimento()
        self.movimento_primeira()
        self.movimento_segunda()

    def movimento_primeira(self):
        if self.nave.contagem_enter == 1:
            self.comando.personagens.rect[1] -= 3
            if self.comando.personagens.rect[1] <= 370:
                self.comando.personagens.rect[1] = 370
                self.nave.contagem_enter += 1
                #pygame.mixer.init()
                #self.som_dialogo = pygame.mixer.Sound("arquivos/g1.mpeg")
                #self.som_dialogo.play()
        if self.contagem_dialogo1 == 3:
            self.comando.personagens.rect[1] += 6
            if self.comando.personagens.rect[1] >= 960:
                self.comando.personagens.rect[1] = 960
                self.comando.personagens.kill()

    def movimento_segunda(self):
        if self.nave.contagem_discernimento == 5 and self.contagem_dialogo1 == 3:
            self.comandoo.personagens.rect[1] -= 3
            if self.comandoo.personagens.rect[1] <= 370:
                self.comandoo.personagens.rect[1] = 370
                self.contagem_dialogo1 += 1
                pygame.mixer.init()
                self.som_dialogo = pygame.mixer.Sound("arquivos/g3.mpeg")
                self.som_dialogo.play()
            if self.contagem_dialogo1 == 5:
                self.comandoo.personagens.rect[1] += 6
                if self.comandoo.personagens.rect[1] >= 960:
                    self.comandoo.personagens.rect[1] = 960
                    self.comandoo.personagens.kill()

    def movimento_fundo(self):
        self.fundo1.personagens.rect[1] += 4
        self.fundo2.personagens.rect[1] += 4
        if self.fundo1.personagens.rect[1] >= 960:
            self.fundo1.personagens.rect[1] = 0
        if self.fundo2.personagens.rect[1] >= 0:
            self.fundo2.personagens.rect[1] = -960

    def quantidade_armadura(self):
        if self.nave.contagem_armadura == 4:
            self.armadura5.personagens.kill()
        if self.nave.contagem_armadura == 3:
            self.armadura4.personagens.kill()
        if self.nave.contagem_armadura == 2:
            self.armadura3.personagens.kill()
        if self.nave.contagem_armadura == 1:
            self.armadura2.personagens.kill()
        if self.nave.contagem_armadura == 0:
            self.mudar_cena = True

    def quantidade_disernimento(self):
        if self.nave.contagem_discernimento == 1:
            self.discernimento0.personagens.kill()
        if self.nave.contagem_discernimento == 2:
            self.discernimento1.personagens.kill()
        if self.nave.contagem_discernimento == 3:
            self.discernimento2.personagens.kill()
        if self.nave.contagem_discernimento == 4:
            self.discernimento3.personagens.kill()
        if self.nave.contagem_discernimento == 5:
            self.discernimento4.personagens.kill()

    def dialogo_primeira(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                self.boleana_dialogo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:
                self.boleana_dialogo = False
        if self.boleana_dialogo:
            self.dialogo1.personagens.kill()
            self.contagem_dialogo1 +=1
            self.dialogo1 = Objetos("arquivos/dialogo" + str(self.contagem_dialogo1) + ".png", 330, 120)
            #if self.contagem_dialogo1 <= 2:
                #pygame.mixer.init()
                #self.som_dialogo = pygame.mixer.Sound("arquivos/g2.mpeg")
                #self.som_dialogo.play()
            print("Nº dialogo:", self.contagem_dialogo1)
        if self.contagem_dialogo1 == 5:
            self.dialogo2.personagens.kill()


    def planetas_inimigos(self):
        if self.comando.personagens.rect[1] == 960 and self.contagem_pinimigos <= 5:
            self.planetainimigo.personagens.rect[1] += 6
        if self.planetainimigo.personagens.rect[1] >= 960 and self.contagem_pinimigos <= 5:
            self.planetainimigo.personagens.kill()
            self.contagem_pinimigos += 1
            print("Nº inimigos:",self.contagem_pinimigos)
            if self.contagem_pinimigos <= 5:
                self.planetainimigo = Objetos("arquivos/pr" + str(self.contagem_pinimigos) + ".png", random.randrange(50, 630), -320)

    def planetas_aliados(self):
        if self.comando.personagens.rect[1] == 960 and self.contagem_paliados <= 5:
            self.planetaaliado.personagens.rect[1] += 6
        if self.planetaaliado.personagens.rect[1] >= 960 and self.contagem_paliados <= 5:
            self.planetaaliado.personagens.kill()
            self.contagem_paliados += 1
            print("Nº aliados:", self.contagem_paliados)
            if self.contagem_paliados <= 5:
                self.planetaaliado = Objetos("arquivos/pb" + str(self.contagem_paliados) + ".png", random.randrange(50, 630), -440)
