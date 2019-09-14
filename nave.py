import pygame
from projetil import *

largura = 700
altura = 700

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._nave_imagem = pygame.image.load("nave.png")
        self._image = self._nave_imagem
        self._nave_obj = self._image.get_rect()
        self._direcao_nave = 0
        self._vida = True
        self._velocidade = 3

        self.colocar_nave_posicao(largura/2, altura/2)

    @property
    def nave_imagem(self):
        return self._nave_imagem

    @property
    def image(self):
        return self._image

    @property
    def nave_obj(self):
        return self._nave_obj

    @property
    def direcao_nave(self):
        return self._direcao_nave

    @property
    def vida(self):
        return self._vida

    @property
    def velocidade(self):
        return self._velocidade

    @image.setter
    def image(self, image):
        self._image = image

    @direcao_nave.setter
    def direcao_nave(self, direcao_nave):
        self._direcao_nave = direcao_nave

    def disparar(self, x_projetil, y_projetil):
        projetil = Projetil(x_projetil, y_projetil, self.direcao_nave)
        return projetil

    def update(self):
        centro_anterior = self.nave_obj.center
        self.image = pygame.transform.rotate(self.nave_imagem, self.direcao_nave)
        self.rect = self.image.get_rect()
        self.rect.center = centro_anterior

    def nave_saiu_tela(self):
        x, y = self.pegar_nave_posicao()

        if x <= 0: x = largura
        elif x > largura + 10: x = 1

        if y <= 0: y = altura
        elif y > altura + 10: y = 1

        self.colocar_nave_posicao(x, y)

    def mover(self):
        self.nave_saiu_tela()

        if self.direcao_nave == 0 or self.direcao_nave == 360: self.nave_obj.move_ip(0, -self.velocidade)
        elif self.direcao_nave == 45: self.nave_obj.move_ip(-self.velocidade, -self.velocidade)
        elif self.direcao_nave == 90: self.nave_obj.move_ip(-self.velocidade, 0)
        elif self.direcao_nave == 135: self.nave_obj.move_ip(-self.velocidade, self.velocidade)
        elif self.direcao_nave == 180: self.nave_obj.move_ip(0, self.velocidade)
        elif self.direcao_nave == 225: self.nave_obj.move_ip(self.velocidade, self.velocidade)
        elif self.direcao_nave == 270: self.nave_obj.move_ip(self.velocidade, 0)
        elif self.direcao_nave == 315: self.nave_obj.move_ip(self.velocidade, -self.velocidade)

    def girar_esquerda(self):
        self.nave_saiu_tela()

        self.direcao_nave += 45
        if self.direcao_nave > 360:
            self.direcao_nave = 45

    def girar_direita(self):
        self.nave_saiu_tela()

        self.direcao_nave -= 45
        if self.direcao_nave < 0:
            self.direcao_nave = 315

    def pegar_nave_posicao(self):
        return self.rect.center

    def colocar_nave_posicao(self, x, y):
        self.nave_obj.center = x, y