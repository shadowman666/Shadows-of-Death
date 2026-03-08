import pygame
import sys
from code.Const import *
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
        self.relogio = pygame.time.Clock()

        self.menu = Menu(self.tela)
        self.estado = MENU
        self.escuridao = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)

        # Carregamento da imagem de fundo da fase
        try:
            self.fundo_jogo = pygame.image.load(IMG_FUNDO_JOGO).convert()
            self.fundo_jogo = pygame.transform.scale(self.fundo_jogo, (LARGURA, ALTURA))
        except pygame.error:
            self.fundo_jogo = None

        self.carregar_musica()

    def carregar_musica(self):
        try:
            pygame.mixer.music.load(SND_MENU)
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.sair()
                if evento.type == pygame.KEYDOWN:
                    if self.estado == MENU:
                        if evento.key == pygame.K_1: self.estado = JOGANDO
                        if evento.key == pygame.K_2: self.estado = CONTROLES
                        if evento.key == pygame.K_ESCAPE: self.sair()
                    elif self.estado == CONTROLES:
                        if evento.key == pygame.K_v: self.estado = MENU
                    elif self.estado == JOGANDO:
                        if evento.key == pygame.K_ESCAPE: self.estado = MENU

            if self.estado == MENU:
                self.menu.mostrar_principal()
            elif self.estado == CONTROLES:
                self.menu.mostrar_controles()
            elif self.estado == JOGANDO:
                self.jogar()

            pygame.display.flip()
            self.relogio.tick(60)

    def jogar(self):
        # Desenha o fundo da fase antes da escuridão
        if self.fundo_jogo:
            self.tela.blit(self.fundo_jogo, (0, 0))
        else:
            self.tela.fill(CINZA_ESCURO)

        # Objeto de teste (Monstro)
        pygame.draw.rect(self.tela, VERMELHO, (400, 300, 50, 50))

        # Lanterna (Máscara de transparência)
        self.escuridao.fill((0, 0, 0, 255))
        pygame.draw.circle(self.escuridao, (0, 0, 0, 0), pygame.mouse.get_pos(), 130)
        self.tela.blit(self.escuridao, (0, 0))

    def sair(self):
        pygame.quit()
        sys.exit()