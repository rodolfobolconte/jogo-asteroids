import pygame

class Projetil:
    def __init__(self, posx, posy, direcao_projetil):
        self._projetil_imagem = pygame.image.load('projetil.png')
        self._projetil_obj = self._projetil_imagem.get_rect()
        self._velocidade = 10
        self._direcao_projetil = direcao_projetil

        if self.direcao_projetil == 0 or self.direcao_projetil == 360:
            self.projetil_obj.center = posx, posy - 40

        elif self.direcao_projetil == 45:
            self.projetil_obj.center = posx - 30, posy - 30

        elif self.direcao_projetil == 90:
            self.projetil_obj.center = posx - 40, posy

        elif self.direcao_projetil == 135:
            self.projetil_obj.center = posx - 30, posy + 30

        elif self.direcao_projetil == 180:
            self.projetil_obj.center = posx + 1, posy + 40

        elif self.direcao_projetil == 225:
            self.projetil_obj.center = posx + 30, posy + 30

        elif self.direcao_projetil == 270:
            self.projetil_obj.center = posx + 40, posy

        elif self.direcao_projetil == 315:
            self.projetil_obj.center = posx + 30, posy - 30

    @property
    def projetil_imagem(self):
        return self._projetil_imagem

    @property
    def projetil_obj(self):
        return self._projetil_obj

    @property
    def direcao_projetil(self):
        return self._direcao_projetil

    @property
    def velocidade(self):
        return self._velocidade

    def projetil_trajetoria(self):
        if self.direcao_projetil == 0 or self.direcao_projetil == 360: self.projetil_movimentar(0, -self.velocidade)
        elif self.direcao_projetil == 45: self.projetil_movimentar(-self.velocidade, -self.velocidade)
        elif self.direcao_projetil == 90: self.projetil_movimentar(-self.velocidade, 0)
        elif self.direcao_projetil == 135: self.projetil_movimentar(-self.velocidade, self.velocidade)
        elif self.direcao_projetil == 180: self.projetil_movimentar(0, self.velocidade)
        elif self.direcao_projetil == 225: self.projetil_movimentar(self.velocidade, self.velocidade)
        elif self.direcao_projetil == 270: self.projetil_movimentar(self.velocidade, 0)
        elif self.direcao_projetil == 315: self.projetil_movimentar(self.velocidade, -self.velocidade)

    def projetil_movimentar(self, x, y):
        self.projetil_obj.move_ip(x, y)

    def colocar_projetil_tela(self, superficie):
        superficie.blit(self.projetil_imagem, self.projetil_obj)