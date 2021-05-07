import pygame
from objetos import Objetos, Nave, Tiro
import random

class Jogo:

    def __init__(self):
        self.fundo1 = Objetos("arquivos/espaco.png", 0, 0)
        self.fundo2 = Objetos("arquivos/espaco.png", 0, -960)
        self.nave = Nave("arquivos/nave1.png",630,750)
        self.comando = Objetos("arquivos/comando1.png", 40, 960)
        self.comandoo = Objetos("arquivos/comandoo1.png", 40, 960)
        self.comandooo = Objetos("arquivos/comandooo1.png", 40, 900)
        self.dialogo1 = Objetos("arquivos/dialogo1.png", 330, 120)
        self.dialogo2 = Objetos("arquivos/dialogo4.png", 330, 120)
        self.dialogo3 = Objetos("arquivos/dialogo6.png", 330,120)
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
        self.condecoracao2 = Objetos("arquivos/condecoracao2.png", 1100, 790)
        self.destreza0 = Objetos("arquivos/destreza0.png",823,101)
        self.gggg = Objetos("arquivos/gggg1.png",1000,-230)
        self.ggg = Objetos("arquivos/ggg1.png", 700, -180)
        self.gg = Objetos("arquivos/gg1.png", 400, -130)
        self.g = Objetos("arquivos/g1.png", 100, -100)
        self.r = Objetos("arquivos/r.png", 600, -50)
        self.tiro = Tiro("arquivos/x1.png", -10,-10)
        self.aste1 = Objetos("arquivos/aste1.png",840,-50)
        self.aste2 = Objetos("arquivos/aste2.png", 640, -120)
        self.aste3 = Objetos("arquivos/aste3.png", 440, -190)
        self.boleana_dialogo = False
        self.mudar_cena = False
        self.foi = False
        self.contagem_resili = 0
        self.contagem_destre = 0
        self.contagem_dialogo1 = 1
        self.contagem_paliados = 1
        self.contagem_pinimigos = 1
        self.inicio_asteroides = 0
        self.contagem_gggg = 1
        self.contagem_ggg = 1
        self.contagem_gg = 1
        self.contagem_g = 1
        self.contagem_r = 1

    def draw(self, tela):
        self.fundo1.draw(tela)
        self.fundo2.draw(tela)
        self.tiro.draw(tela)
        self.nave.draw(tela)
        self.comando.draw(tela)
        if self.nave.contagem_discernimento == 5 and self.contagem_paliados == 6:
            self.comandoo.draw(tela)
        if self.nave.contagem_resiliencia == 5 and self.contagem_gggg == 6:
            self.comandooo.draw(tela)
        self.armadura5.draw(tela)
        self.armadura4.draw(tela)
        self.armadura3.draw(tela)
        self.armadura2.draw(tela)
        self.armadura1.draw(tela)
        if self.contagem_dialogo1 == 3:
            self.planetaaliado.draw(tela)
        if self.contagem_dialogo1 == 3:
            self.planetainimigo.draw(tela)
            self.aste1.draw(tela)
            self.aste2.draw(tela)
            self.aste3.draw(tela)
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
        if self.nave.contagem_resiliencia == 1:
            self.resiliencia1.draw(tela)
        if self.nave.contagem_resiliencia == 2:
            self.resiliencia2.draw(tela)
        if self.nave.contagem_resiliencia == 3:
            self.resiliencia3.draw(tela)
        if self.nave.contagem_resiliencia == 4:
            self.resiliencia4.draw(tela)
        if self.nave.contagem_resiliencia == 5:
            self.resiliencia5.draw(tela)
        if self.comando.personagens.rect[1] == 370:
            self.dialogo1.draw(tela)
        if self.comandoo.personagens.rect[1] == 370:
            self.dialogo2.draw(tela)
        if self.comandooo.personagens.rect[1] == 370:
            self.dialogo3.draw(tela)
        if self.contagem_resili == 1:
            self.condecoracoes.draw(tela)
            self.condecoracao1.draw(tela)
            self.resiliencia0.draw(tela)
        if self.contagem_destre == 1:
            self.condecoracao2.draw(tela)
            self.destreza0.draw(tela)
        if self.inicio_asteroides == 1:
            self.gggg.draw(tela)
            self.ggg.draw(tela)
            self.gg.draw(tela)
            self.g.draw(tela)
            self.r.draw(tela)
        if self.nave.contagem_resiliencia == 6:
            self.comandooo.draw(tela)

    def atualizacoes(self):
        self.movimento_fundo()
        self.nave.animacoes("nave", 2, 2)
        self.comando.animacoes("comando", 2, 2)
        self.comandoo.animacoes("comandoo",2,2)
        self.comandooo.animacoes("comandooo",2,2)
        self.tiro.animacoes("x",2,2)
        self.planetas_inimigos()
        self.planetas_aliados()
        self.nave.colisao_planetas(self.planetainimigo.group, "planetainimigos")
        self.nave.colisao_planetas(self.aste1.group, "aste1.png")
        self.nave.colisao_planetas(self.aste2.group, "aste2.png")
        self.nave.colisao_planetas(self.aste3.group, "aste3.png")
        self.nave.colisao_planetas(self.planetaaliado.group, "planetaaliados")
        self.nave.colisao_asteroides(self.gggg.group, "gggg")
        self.nave.colisao_asteroides(self.ggg.group, "ggg")
        self.nave.colisao_asteroides(self.gg.group, "gg")
        self.nave.colisao_asteroides(self.g.group, "g")
        self.nave.colisao_asteroides(self.r.group, "r")
        self.tiro.colisao_tiro(self.planetainimigo.group, "planetainimigos")
        self.tiro.colisao_tiro(self.planetaaliado.group, "planetaaliados")
        self.tiro.colisao_tiroo(self.gggg.group, "gggg")
        self.tiro.colisao_tiroo(self.ggg.group, "ggg")
        self.tiro.colisao_tiroo(self.gg.group, "gg")
        self.tiro.colisao_tiroo(self.g.group, "g")
        self.quantidade_armadura()
        self.quantidade_disernimento()
        self.quantidade_resiliencia()
        self.movimento_primeira()
        self.movimento_segunda()
        self.movimento_terceira()
        self.asteroides()
        self.disparado()

    def movimento_primeira(self):
        if self.nave.contagem_enter == 1:
            self.comando.personagens.rect[1] -= 3
            if self.comando.personagens.rect[1] <= 370:
                self.comando.personagens.rect[1] = 370
                self.nave.contagem_enter += 1
                #pygame.mixer.init()
                #self.som_dialogo = pygame.mixer.Sound("arquivos/gravacao1.mpeg")
                #self.som_dialogo.play()
        if self.contagem_dialogo1 == 3:
            self.comando.personagens.rect[1] += 6
            if self.comando.personagens.rect[1] >= 960:
                self.comando.personagens.rect[1] = 960
                self.comando.personagens.kill()

    def movimento_segunda(self):
        if self.nave.contagem_discernimento == 5 and self.contagem_paliados == 6 and self.contagem_dialogo1 == 3:
            self.comandoo.personagens.rect[1] -= 3
            if self.comandoo.personagens.rect[1] <= 370:
                self.comandoo.personagens.rect[1] = 370
                self.contagem_resili += 1
                self.contagem_dialogo1 += 1
                #pygame.mixer.init()
                #self.som_dialogo = pygame.mixer.Sound("arquivos/gravacao3.mpeg")
                #self.som_dialogo.play()
        if self.contagem_dialogo1 == 5:
            self.comandoo.personagens.rect[1] += 6
            if self.comandoo.personagens.rect[1] >= 960:
                self.comandoo.personagens.rect[1] = 960
                self.comandoo.personagens.kill()

    def movimento_terceira(self):
        if self.nave.contagem_resiliencia == 5 and self.contagem_gggg == 6 and self.contagem_dialogo1 == 5:
            self.comandooo.personagens.rect[1] -= 3
            if self.comandooo.personagens.rect[1] <= 370:
                self.comandooo.personagens.rect[1] = 370
                self.contagem_destre += 1
                self.contagem_dialogo1 += 1
        if self.contagem_dialogo1 == 7:
            self.comandooo.personagens.rect[1] += 6
            if self.comandooo.personagens.rect[1] >= 960:
                self.comandooo.personagens.rect[1] = 960
                self.comandooo.personagens.kill()

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

    def quantidade_resiliencia(self):
        if self.nave.contagem_resiliencia == 1:
            self.resiliencia0.personagens.kill()
        if self.nave.contagem_resiliencia == 2:
            self.resiliencia1.personagens.kill()
        if self.nave.contagem_resiliencia == 3:
            self.resiliencia2.personagens.kill()
        if self.nave.contagem_resiliencia == 4:
            self.resiliencia3.personagens.kill()
        if self.nave.contagem_resiliencia == 5:
            self.resiliencia4.personagens.kill()

    def dialogo(self, event):
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
                #self.som_dialogo = pygame.mixer.Sound("arquivos/gravacao2.mpeg")
                #self.som_dialogo.play()
            print("Nº dialogo:", self.contagem_dialogo1)
        if self.contagem_dialogo1 == 5:
            self.dialogo2.personagens.kill()
            self.inicio_asteroides = 1

    def planetas_inimigos(self):
        if self.comando.personagens.rect[1] == 960 and self.contagem_pinimigos <= 5:
            self.planetainimigo.personagens.rect[1] += 6
            self.aste1.personagens.rect[1] += 7
            self.aste2.personagens.rect[1] += 7
            self.aste3.personagens.rect[1] += 7
        if self.aste1.personagens.rect[1] >= 960 and self.contagem_pinimigos <= 5:
            self.aste1.personagens.kill()
            if self.contagem_pinimigos <= 4:
                self.aste1 = Objetos("arquivos/aste1.png", random.randrange(50, 630), -50)
        if self.aste2.personagens.rect[1] >= 960 and self.contagem_pinimigos <= 5:
            self.aste2.personagens.kill()
            if self.contagem_pinimigos <= 4:
                self.aste2 = Objetos("arquivos/aste2.png", random.randrange(50, 630), -120)
        if self.aste3.personagens.rect[1] >= 960 and self.contagem_pinimigos <= 5:
            self.aste3.personagens.kill()
            if self.contagem_pinimigos <= 4:
                self.aste3 = Objetos("arquivos/aste3.png", random.randrange(50, 630), -190)
        if self.planetainimigo.personagens.rect[1] >= 960 and self.contagem_pinimigos <= 5:
            self.planetainimigo.personagens.kill()
            self.contagem_pinimigos += 1
            if self.contagem_pinimigos <= 5:
                self.planetainimigo = Objetos("arquivos/pr" + str(self.contagem_pinimigos) + ".png", random.randrange(50, 630), -320)

    def planetas_aliados(self):
        if self.comando.personagens.rect[1] == 960 and self.contagem_paliados <= 5:
            self.planetaaliado.personagens.rect[1] += 6
        if self.planetaaliado.personagens.rect[1] >= 960 and self.contagem_paliados <= 5:
            self.planetaaliado.personagens.kill()
            self.contagem_paliados += 1
            if self.contagem_paliados <= 5:
                self.planetaaliado = Objetos("arquivos/pb" + str(self.contagem_paliados) + ".png", random.randrange(50, 630), -440)

    def asteroides(self):
        if self.inicio_asteroides == 1:
            self.gggg.personagens.rect[1] += 4
            self.ggg.personagens.rect[1] += 4
            self.gg.personagens.rect[1] += 4
            self.g.personagens.rect[1] += 4
            self.r.personagens.rect[1] += 4
        if self.gggg.personagens.rect[1] >= 960 and self.contagem_gggg <= 5:
            self.gggg.personagens.kill()
            self.contagem_gggg += 1
            if self.contagem_gggg <= 5:
                self.gggg = Objetos("arquivos/gggg" + str(self.contagem_gggg) + ".png", random.randrange(50, 630), -230)
        if self.ggg.personagens.rect[1] >= 960 and self.contagem_ggg <= 5:
            self.ggg.personagens.kill()
            self.contagem_ggg += 1
            if self.contagem_ggg <= 5:
                self.ggg = Objetos("arquivos/ggg" + str(self.contagem_ggg) + ".png", random.randrange(50, 630), -180)
        if self.gg.personagens.rect[1] >= 960 and self.contagem_gg <= 5:
            self.gg.personagens.kill()
            self.contagem_gg += 1
            if self.contagem_gg <= 5:
                self.gg = Objetos("arquivos/gg" + str(self.contagem_gg) + ".png", random.randrange(50, 630), -130)
        if self.g.personagens.rect[1] >= 960 and self.contagem_g <= 5:
            self.g.personagens.kill()
            self.contagem_g += 1
            if self.contagem_g <= 5:
                self.g = Objetos("arquivos/g" + str(self.contagem_g) + ".png", random.randrange(50, 630), -100)
        if self.r.personagens.rect[1] >= 960 and self.contagem_r <= 5:
            self.r.personagens.kill()
            self.contagem_r += 1
            if self.contagem_r <= 5:
                self.r = Objetos("arquivos/r.png", random.randrange(50, 630), -50)

    def disparado(self):
        if self.tiro.tiro:
            self.tiro.personagens.rect[1] = (self.nave.personagens.rect[1] + 30)
            self.tiro.personagens.rect[0] = (self.nave.personagens.rect[0] + 62)
            self.foi = True
        if self.foi:
            if self.tiro.personagens.rect[1] >= -70:
                self.tiro.personagens.rect[1] -= 15
            if self.tiro.personagens.rect[1] == -70:
                self.tiro.personagens.kill()
                self.foi = False
            if self.tiro.tiro:
                self.tiro = Tiro("arquivos/x1.png", self.nave.personagens.rect[0] + 62, self.nave.personagens.rect[1] + 30)


