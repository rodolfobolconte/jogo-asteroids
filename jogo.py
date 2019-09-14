from nave import *
from inimigo import *
from asteroide import *

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