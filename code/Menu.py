import pygame
import random
from code.Const import *


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.fonte_titulo = pygame.font.SysFont("arial", 70, bold=True)
        self.fonte_menu = pygame.font.SysFont("arial", 30)

        # Carregamento da imagem de fundo do Menu
        try:
            self.fundo = pygame.image.load(IMG_FUNDO_MENU).convert()
            self.fundo = pygame.transform.scale(self.fundo, (LARGURA, ALTURA))
        except pygame.error:
            self.fundo = None  # Caso não encontre a imagem, usa fundo preto

    def desenhar_texto(self, texto, fonte, cor, y):
        img = fonte.render(texto, True, cor)
        self.tela.blit(img, (LARGURA // 2 - img.get_width() // 2, y))

    def desenhar_titulo_animado(self):
        """Efeito de tremor e pisca no título Shadows of Death"""
        offset_x = random.randint(-3, 3)  #
        offset_y = random.randint(-3, 3)

        if (pygame.time.get_ticks() // 500) % 2 == 0:
            cor_atual = VERMELHO
        else:
            cor_atual = VERMELHO_CLARO

        img = self.fonte_titulo.render(TITULO_JOGO, True, cor_atual)
        self.tela.blit(img, (LARGURA // 2 - img.get_width() // 2 + offset_x, 100 + offset_y))

    def mostrar_principal(self):
        if self.fundo:
            self.tela.blit(self.fundo, (0, 0))  # Desenha a imagem de fundo
        else:
            self.tela.fill(PRETO)

        self.desenhar_titulo_animado()
        self.desenhar_texto("[1] INICIAR JOGO", self.fonte_menu, BRANCO, 320)
        self.desenhar_texto("[2] CONTROLES", self.fonte_menu, BRANCO, 380)
        self.desenhar_texto("[ESC] SAIR", self.fonte_menu, BRANCO, 440)

    def mostrar_controles(self):
        self.tela.fill(CINZA_ESCURO)
        self.desenhar_texto("COMO SOBREVIVER", self.fonte_titulo, BRANCO, 80)

        # Requisito: Exibir comandos na tela
        comandos = [
            "MOUSE - Lanterna",
            "ESPAÇO - Ação",
            "SHIFT - Correr",
            "F - Luz",
            "",
            "Pressione [V] para Voltar"
        ]

        y_pos = 220
        for linha in comandos:
            self.desenhar_texto(linha, self.fonte_menu, BRANCO, y_pos)
            y_pos += 45