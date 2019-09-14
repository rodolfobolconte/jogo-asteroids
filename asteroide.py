import pygame
import random

largura = 700
altura = 700

class Asteroide:
    def __init__(self, tamanho, x, y):
        self._tamanho = tamanho

        if self.tamanho == 3:
            self._asteroide_imagem = pygame.image.load('asteroide3.png')
        elif self.tamanho == 2:
            self._asteroide_imagem = pygame.image.load('asteroide2.png')
        elif self.tamanho == 1:
            self._asteroide_imagem = pygame.image.load('asteroide1.png')

        self._asteroide_obj = self.asteroide_imagem.get_rect()
        self._velocidade = 1

        self.asteroide_obj.centerx = x
        self.asteroide_obj.centery = y

        self.direcao_asteroide = random.randrange(0, 360, 45)

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def asteroide_imagem(self):
        return self._asteroide_imagem

    @property
    def asteroide_obj(self):
        return self._asteroide_obj

    @property
    def velocidade(self):
        return self._velocidade

    def asteroide_saiu_tela(self):
        x, y = self.pegar_asteroide_posicao()

        if x <= 0: x = largura
        elif x > largura + 10: x = 1

        if y <= 0: y = altura
        elif y > altura + 10: y = 1

        self.colocar_asteroide_posicao(x, y)

    def asteroide_trajetoria(self):
        self.asteroide_saiu_tela()

        if self.direcao_asteroide == 0 or self.direcao_asteroide == 360: self.asteroide_movimentar(0, -self.velocidade)
        elif self.direcao_asteroide == 45: self.asteroide_movimentar(-self.velocidade, -self.velocidade)
        elif self.direcao_asteroide == 90: self.asteroide_movimentar(-self.velocidade, 0)
        elif self.direcao_asteroide == 135: self.asteroide_movimentar(-self.velocidade, self.velocidade)
        elif self.direcao_asteroide == 180: self.asteroide_movimentar(0, self.velocidade)
        elif self.direcao_asteroide == 225: self.asteroide_movimentar(self.velocidade, self.velocidade)
        elif self.direcao_asteroide == 270: self.asteroide_movimentar(self.velocidade, 0)
        elif self.direcao_asteroide == 315: self.asteroide_movimentar(self.velocidade, -self.velocidade)

    def asteroide_movimentar(self, x, y):
        self.asteroide_obj.move_ip(x, y)

    def colocar_asteroide_tela(self, superficie):
        superficie.blit(self.asteroide_imagem, self.asteroide_obj)

    def pegar_asteroide_posicao(self):
        return self.asteroide_obj.center

    def colocar_asteroide_posicao(self, x, y):
        self.asteroide_obj.center = x, y