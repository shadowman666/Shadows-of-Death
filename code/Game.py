import pygame
import sys
from code.Const import *
from code.Menu import Menu
from code.Enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
        self.relogio = pygame.time.Clock()

        self.menu = Menu(self.tela)
        self.estado = MENU

        # Sistema de Lanterna
        self.escuridao = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)

        # Parallax e Inimigos
        self.carregar_parallax()
        self.inimigo = Enemy(LARGURA, 400)
        self.snd_hit = pygame.mixer.Sound(SND_HIT)

        # Inicia música do Menu
        self.trocar_musica(SND_MENU)

    def carregar_parallax(self):
        try:
            self.bg_longe = pygame.image.load(IMG_BG_LAYER_0).convert()
            self.bg_perto = pygame.image.load(IMG_BG_LAYER_1).convert_alpha()
            self.bg_longe = pygame.transform.scale(self.bg_longe, (LARGURA, ALTURA))
            self.bg_perto = pygame.transform.scale(self.bg_perto, (LARGURA, ALTURA))
        except:
            self.bg_longe = self.bg_perto = None
        self.scroll_longe = 0
        self.scroll_perto = 0

    def trocar_musica(self, caminho):
        """Para a música atual e inicia a nova"""
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play(-1)
        except:
            print(f"Erro ao carregar som: {caminho}")

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT: self.sair()

                if evento.type == pygame.KEYDOWN:
                    if self.estado == MENU:
                        if evento.key == pygame.K_1:
                            self.estado = JOGANDO
                            self.trocar_musica(SND_GAME)  # ✅ Troca para música do jogo
                        if evento.key == pygame.K_2: self.estado = CONTROLES
                        if evento.key == pygame.K_ESCAPE: self.sair()
                    elif self.estado == CONTROLES:
                        if evento.key == pygame.K_v: self.estado = MENU
                    elif self.estado == JOGANDO:
                        if evento.key == pygame.K_ESCAPE:
                            self.estado = MENU
                            self.trocar_musica(SND_MENU)  # ✅ Volta para música do menu

            if self.estado == MENU:
                self.menu.mostrar_principal()
            elif self.estado == CONTROLES:
                self.menu.mostrar_controles()
            elif self.estado == JOGANDO:
                self.jogar()

            pygame.display.flip()
            self.relogio.tick(60)

    def jogar(self):
        # 1. Movimento Parallax (Camadas)
        self.scroll_longe -= 1
        self.scroll_perto -= 3
        if abs(self.scroll_longe) > LARGURA: self.scroll_longe = 0
        if abs(self.scroll_perto) > LARGURA: self.scroll_perto = 0

        if self.bg_longe:
            self.tela.blit(self.bg_longe, (self.scroll_longe, 0))
            self.tela.blit(self.bg_longe, (self.scroll_longe + LARGURA, 0))
            self.tela.blit(self.bg_perto, (self.scroll_perto, 0))
            self.tela.blit(self.bg_perto, (self.scroll_perto + LARGURA, 0))
        else:
            self.tela.fill(CINZA_ESCURO)

        # 2. Inimigo e Colisão
        self.inimigo.mover()
        self.inimigo.desenhar(self.tela)

        pos_mouse = pygame.mouse.get_pos()
        if self.inimigo.rect.collidepoint(pos_mouse):
            self.snd_hit.play()

        # 3. Lanterna
        self.escuridao.fill((0, 0, 0, 255))
        pygame.draw.circle(self.escuridao, (0, 0, 0, 0), pos_mouse, 130)
        self.tela.blit(self.escuridao, (0, 0))

    def sair(self):
        pygame.quit()
        sys.exit()