import pygame
from pygame.locals import *
import time
from jogo import *

largura = 700
altura = 700

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