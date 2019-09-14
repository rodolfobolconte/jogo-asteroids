import pygame
import random
from projetil_inimigo import *

largura = 700
altura = 700

class Inimigo:
    def __init__(self, x, y):
        self._inimigo_imagem = pygame.image.load("inimigo.png")
        self._inimigo_obj = self.inimigo_imagem.get_rect()
        self._velocidade = 1
        self._tempo_disparo = 0
        self.direcao_inimigo = random.randrange(0, 360, 45)

        self.inimigo_obj.centerx = x
        self.inimigo_obj.centery = y

    @property
    def inimigo_imagem(self):
        return self._inimigo_imagem

    @property
    def inimigo_obj(self):
        return self._inimigo_obj

    @property
    def velocidade(self):
        return self._velocidade

    @property
    def tempo_disparo(self):
        return self._tempo_disparo

    @tempo_disparo.setter
    def tempo_disparo(self, tempo_disparo):
        self._tempo_disparo = tempo_disparo

    def disparar(self, x_projetil, y_projetil):
        projetil = Projetil_Inimigo(x_projetil, y_projetil)
        return projetil

    def inimigo_saiu_tela(self):
        x, y = self.pegar_inimigo_posicao()

        if x <= 0: x = largura
        elif x > largura + 10: x = 1

        if y <= 0: y = altura
        elif y > altura + 10: y = 1

        self.colocar_inimigo_posicao(x, y)

    def inimigo_trajetoria(self):
        self.inimigo_saiu_tela()

        if self.direcao_inimigo == 0 or self.direcao_inimigo == 360: self.inimigo_movimentar(0, -self.velocidade)
        elif self.direcao_inimigo == 45: self.inimigo_movimentar(-self.velocidade, -self.velocidade)
        elif self.direcao_inimigo == 90: self.inimigo_movimentar(-self.velocidade, 0)
        elif self.direcao_inimigo == 135: self.inimigo_movimentar(-self.velocidade, self.velocidade)
        elif self.direcao_inimigo == 180: self.inimigo_movimentar(0, self.velocidade)
        elif self.direcao_inimigo == 225: self.inimigo_movimentar(self.velocidade, self.velocidade)
        elif self.direcao_inimigo == 270: self.inimigo_movimentar(self.velocidade, 0)
        elif self.direcao_inimigo == 315: self.inimigo_movimentar(self.velocidade, -self.velocidade)

        self.tempo_disparo += 1

    def inimigo_movimentar(self, x, y):
        self.inimigo_obj.move_ip(x, y)

    def colocar_inimigo_tela(self, superficie):
        superficie.blit(self.inimigo_imagem, self.inimigo_obj)

    def pegar_inimigo_posicao(self):
        return self.inimigo_obj.center

    def colocar_inimigo_posicao(self, x, y):
        self.inimigo_obj.center = x, y