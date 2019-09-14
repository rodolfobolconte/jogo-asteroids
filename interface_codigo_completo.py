import pygame
from pygame.locals import *
import time
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

class Jogo:
    def __init__(self):
        self.nave = Nave()
        self.pontuacao = 0
        self.vidas = 3
        self.vidas_icones = []
        self.fase = 1
        self.asteroides = 3
        self.inimigos = 0
        self.lista_asteroides = []
        self.lista_inimigos = []
        self.lista_projeteis = []
        self.lista_projeteis_inimigos = []

        self.audio_disparo = pygame.mixer.Sound('disparo.wav')
        self.audio_explosao = pygame.mixer.Sound('explosao.wav')
        self.audio_passa_fase = pygame.mixer.Sound('passa_fase.wav')

        self.inicializar_asteroides(self.asteroides)

        self.colocar_vidas_icones()

    def colocar_vidas_icones(self):
        direita = largura
        for i in range(self.vidas):
            lista = []
            lista.append(pygame.image.load('coracao.png'))
            lista.append(lista[0].get_rect())

            lista[1].top = 0
            lista[1].right = direita

            direita -= 25

            self.vidas_icones.append(lista)

    def mover_nave(self):
        self.nave.mover()

    def girar_nave_esquerda(self):
        self.nave.girar_esquerda()

    def girar_nave_direita(self):
        self.nave.girar_direita()

    def disparar_nave(self):
        self.audio_disparo.play()
        x_projetil, y_projetil = self.nave.pegar_nave_posicao()
        self.lista_projeteis.append(self.nave.disparar(x_projetil, y_projetil))

    def disparar_inimigo_tempo(self):
        for inimigo in self.lista_inimigos:
            if inimigo.tempo_disparo == 100:
                self.disparar_inimigo()
                inimigo.tempo_disparo = 0
                return True

    def disparar_inimigo(self):
        for inimigo in self.lista_inimigos:
            self.audio_disparo.play()
            x_projetil, y_projetil = inimigo.pegar_inimigo_posicao()
            self.lista_projeteis_inimigos.append(inimigo.disparar(x_projetil, y_projetil))

    def multiplica_asteroides(self, x, y, tamanho_asteroide):
        if tamanho_asteroide != 0:
            asteroide = Asteroide(tamanho_asteroide, x, y)
            self.lista_asteroides.append(asteroide)

            asteroide2 = Asteroide(tamanho_asteroide, x, y)
            self.lista_asteroides.append(asteroide2)

    def compara_nave_destruiu_asteroide(self):
        for projetil in self.lista_projeteis:
            for asteroide in self.lista_asteroides:
                if projetil.projetil_obj.colliderect(asteroide.asteroide_obj):
                    tamanho_asteroide = asteroide.tamanho
                    x_asteroide, y_asteroide = asteroide.pegar_asteroide_posicao()

                    try: self.lista_projeteis.remove(projetil)
                    except ValueError: pass

                    try:
                        self.lista_asteroides.remove(asteroide)
                        self.multiplica_asteroides(x_asteroide, y_asteroide, tamanho_asteroide - 1)
                    except ValueError: pass

                    self.pontuacao += 25 * tamanho_asteroide

    def compara_nave_colidiu_asteroide(self, tela):
        for asteroide in self.lista_asteroides:
            if self.nave.rect.colliderect(asteroide.asteroide_obj):
                self.audio_explosao.play()
                explosao_imagem = pygame.image.load("explosao.png")
                explosao_obj = explosao_imagem.get_rect()
                explosao_obj.center = self.nave.nave_obj.center
                tela.blit(explosao_imagem, explosao_obj)

                tamanho_asteroide = asteroide.tamanho
                x_asteroide, y_asteroide = asteroide.pegar_asteroide_posicao()

                try:
                    self.lista_asteroides.remove(asteroide)
                    self.multiplica_asteroides(x_asteroide, y_asteroide, tamanho_asteroide - 1)
                except ValueError: pass

                self.nave.colocar_nave_posicao(largura / 2, altura / 2)

                self.vidas -= 1

                self.vidas_icones.pop(self.vidas)
                return True
        return False

    def compara_nave_destruiu_inimigo(self, tela):
        for projetil in self.lista_projeteis:
            for inimigo in self.lista_inimigos:
                if projetil.projetil_obj.colliderect(inimigo.inimigo_obj):
                    self.audio_explosao.play()
                    explosao_imagem = pygame.image.load("explosao.png")
                    explosao_obj = explosao_imagem.get_rect()
                    explosao_obj.center = inimigo.pegar_inimigo_posicao()
                    tela.blit(explosao_imagem, explosao_obj)

                    try: self.lista_inimigos.remove(inimigo)
                    except ValueError: pass

                    try: self.lista_projeteis.remove(projetil)
                    except ValueError: pass

                    self.pontuacao += 100
                    break

    def compara_nave_colidiu_inimigo(self, tela):
        for inimigo in self.lista_inimigos:
            if self.nave.rect.colliderect(inimigo.inimigo_obj):
                self.audio_explosao.play()
                explosao_imagem = pygame.image.load("explosao.png")
                explosao_obj = explosao_imagem.get_rect()
                explosao_obj.center = self.nave.nave_obj.center
                tela.blit(explosao_imagem, explosao_obj)

                try: self.lista_inimigos.remove(inimigo)
                except ValueError: pass

                self.nave.colocar_nave_posicao(largura/2, altura/2)

                self.vidas -= 1

                self.vidas_icones.pop(self.vidas)

                return True

    def compara_inimigo_destruiu_nave(self, tela):
        for projetil in self.lista_projeteis_inimigos:
            if projetil.projetil_obj.colliderect(self.nave.rect):
                self.audio_explosao.play()
                explosao_imagem = pygame.image.load("explosao.png")
                explosao_obj = explosao_imagem.get_rect()
                explosao_obj.center = self.nave.pegar_nave_posicao()
                tela.blit(explosao_imagem, explosao_obj)

                try: self.lista_projeteis_inimigos.remove(projetil)
                except ValueError: pass

                self.nave.colocar_nave_posicao(largura / 2, altura / 2)

                self.vidas -= 1

                self.vidas_icones.pop(self.vidas)
                return True

    def compara_inimigo_destruiu_asteroide(self):
        for projetil in self.lista_projeteis_inimigos:
            for asteroide in self.lista_asteroides:
                if projetil.projetil_obj.colliderect(asteroide.asteroide_obj):
                    tamanho_asteroide = asteroide.tamanho
                    x_asteroide, y_asteroide = asteroide.pegar_asteroide_posicao()

                    try: self.lista_projeteis_inimigos.remove(projetil)
                    except ValueError: pass

                    try:
                        self.lista_asteroides.remove(asteroide)
                        self.multiplica_asteroides(x_asteroide, y_asteroide, tamanho_asteroide - 1)
                    except ValueError: pass

    def compara_inimigo_colidiu_asteroide(self, tela):
        for asteroide in self.lista_asteroides:
            for inimigo in self.lista_inimigos:
                if inimigo.inimigo_obj.colliderect(asteroide.asteroide_obj):
                    self.audio_explosao.play()
                    explosao_imagem = pygame.image.load("explosao.png")
                    explosao_obj = explosao_imagem.get_rect()
                    explosao_obj.center = inimigo.pegar_inimigo_posicao()
                    tela.blit(explosao_imagem, explosao_obj)

                    tamanho_asteroide = asteroide.tamanho
                    x_asteroide, y_asteroide = asteroide.pegar_asteroide_posicao()

                    try: self.lista_inimigos.remove(inimigo)
                    except ValueError: pass

                    try:
                        self.lista_asteroides.remove(asteroide)
                        self.multiplica_asteroides(x_asteroide, y_asteroide, tamanho_asteroide - 1)
                    except ValueError: pass

    def inicializar_asteroides(self, quantidade):
        for i in range(quantidade):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            asteroide = Asteroide(3, x, y)
            self.lista_asteroides.append(asteroide)

    def inicializar_inimigos(self, quantidade):
        for i in range(quantidade):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            inimigo = Inimigo(x, y)
            self.lista_inimigos.append(inimigo)

    def remover_projeteis(self):
        for projetil in self.lista_projeteis:
            if projetil.projetil_obj.top < 0 or projetil.projetil_obj.top > altura:
                try: self.lista_projeteis.remove(projetil)
                except ValueError: pass

            if projetil.projetil_obj.left < 0 or projetil.projetil_obj.left > largura:
                try: self.lista_projeteis.remove(projetil)
                except ValueError: pass

    def remover_projeteis_inimigos(self):
        for projetil in self.lista_projeteis_inimigos:
            if projetil.projetil_obj.top < 0 or projetil.projetil_obj.top > altura:
                try: self.lista_projeteis_inimigos.remove(projetil)
                except ValueError: pass

            if projetil.projetil_obj.left < 0 or projetil.projetil_obj.left > largura:
                try: self.lista_projeteis_inimigos.remove(projetil)
                except ValueError: pass

    def proxima_fase(self):
        if len(self.lista_asteroides) == 0 and len(self.lista_inimigos) == 0:
            self.audio_passa_fase.play()
            self.asteroides += 1
            self.inimigos += 1
            self.inicializar_asteroides(self.asteroides)
            self.inicializar_inimigos(self.inimigos)
            self.fase += 1
            return True
        return False

    def colocar_vidas_tela(self, superficie):
        for i in self.vidas_icones:
            superficie.blit(i[0], i[1])

    def game_over(self):
        if self.vidas == 0:
            return True
        return False

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

class Projetil_Inimigo:
    def __init__(self, posx, posy):
        self._projetil_imagem = pygame.image.load('inimigo_projetil.png')
        self._projetil_obj = self._projetil_imagem.get_rect()
        self._velocidade = 10
        self._direcao_projetil = random.randrange(0, 360, 45)

        self.projetil_obj.center = posx, posy

    @property
    def projetil_imagem(self):
        return self._projetil_imagem

    @property
    def projetil_obj(self):
        return self._projetil_obj

    @property
    def velocidade(self):
        return self._velocidade

    @property
    def direcao_projetil(self):
        return self._direcao_projetil

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

def interface():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("STAR 'ASTEROIDS' WARS")
    background = pygame.image.load("background.png")

    jogo = Jogo()
    allSprites = pygame.sprite.Group(jogo.nave)

    relogio = pygame.time.Clock()

    pygame.font.init()
    font_game_over = pygame.font.SysFont(pygame.font.get_default_font(), 45)
    font_pontuacao = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    font_fase = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    font_jogo = pygame.font.SysFont(pygame.font.get_default_font(), 50)

    som_abertura = pygame.mixer.Sound("abertura.wav")
    som_game_over = pygame.mixer.Sound("game_over.wav")

    rodar_jogo = True

    key = {K_UP: False}

    som_abertura.play()
    texto_jogo = font_jogo.render("STAR 'ASTEROIDS' WARS", 1, (255, 255, 255))
    tela.blit(texto_jogo, (largura / 2 - 200, altura / 2 - 50))
    pygame.display.update()

    texto_fase = font_fase.render("FASE " + str(jogo.fase), 1, (255, 255, 255))
    tela.blit(texto_fase, (largura / 2 - 30, altura / 2))
    pygame.display.update()

    time.sleep(3)

    while rodar_jogo:
        relogio.tick(30)

        for evento in pygame.event.get([KEYUP, KEYDOWN]):
            valor = (evento.type == KEYDOWN)

            if evento.key in key.keys(): key[evento.key] = valor

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_ESCAPE: rodar_jogo = False

                elif evento.key == K_LEFT: jogo.girar_nave_esquerda()

                elif evento.key == K_RIGHT: jogo.girar_nave_direita()

                elif evento.key == K_SPACE: jogo.disparar_nave()

        tela.blit(background, (0, 0))

        if key[K_UP]: jogo.mover_nave()

        allSprites.clear(tela, background)
        allSprites.update()
        allSprites.draw(tela)

        jogo.colocar_vidas_tela(tela)

        if len(jogo.lista_asteroides) > 0:
            for asteroide in jogo.lista_asteroides:
                asteroide.colocar_asteroide_tela(tela)
                asteroide.asteroide_trajetoria()

        if len(jogo.lista_projeteis) > 0:
            for projetil in jogo.lista_projeteis:
                projetil.colocar_projetil_tela(tela)
                projetil.projetil_trajetoria()
                jogo.remover_projeteis()

        if len(jogo.lista_inimigos) > 0:
            for inimigo in jogo.lista_inimigos:
                inimigo.colocar_inimigo_tela(tela)
                inimigo.inimigo_trajetoria()

        if len(jogo.lista_projeteis_inimigos) > 0:
            for projetil in jogo.lista_projeteis_inimigos:
                projetil.colocar_projetil_tela(tela)
                projetil.projetil_trajetoria()
                jogo.remover_projeteis_inimigos()

        texto_pontuacao = font_pontuacao.render("Pontuação: " + str(jogo.pontuacao), 1, (255, 255, 255))
        tela.blit(texto_pontuacao, (0, 0))
        pygame.display.update()

        jogo.compara_nave_destruiu_asteroide()
        jogo.compara_nave_destruiu_inimigo(tela)
        jogo.disparar_inimigo_tempo()
        jogo.compara_inimigo_destruiu_asteroide()
        jogo.compara_inimigo_colidiu_asteroide(tela)

        pygame.display.update()

        if jogo.compara_nave_colidiu_asteroide(tela) or jogo.compara_nave_colidiu_inimigo(tela) or jogo.compara_inimigo_destruiu_nave(tela):
            pygame.display.update()

            if jogo.game_over():
                texto_game_over = font_game_over.render("GAME OVER", 1, (255,255,255))
                tela.blit(texto_game_over, (largura / 2 - 70, altura / 2))
                texto_game_over = font_game_over.render("TRY AGAIN", 1, (255, 255, 255))
                tela.blit(texto_game_over, (largura / 2 - 62, altura / 2 + 35))
                pygame.display.update()
                som_game_over.play()
                time.sleep(4.5)

                rodar_jogo = False

            time.sleep(0.5)

        if jogo.proxima_fase():
            texto_fase = font_fase.render("FASE "+str(jogo.fase), 1, (255, 255, 255))
            tela.blit(texto_fase, (largura/2-30, altura/2))
            pygame.display.update()

            time.sleep(4)

        pygame.display.update()

interface()
