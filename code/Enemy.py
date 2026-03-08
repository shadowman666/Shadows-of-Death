import pygame
from code.Const import *


class Enemy:
    def __init__(self, x, y):
        try:
            self.image = pygame.image.load(IMG_ENEMY).convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
        except:
            self.image = pygame.Surface((80, 80))
            self.image.fill(VERMELHO)

        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocidade = 3

    def mover(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.rect.left = LARGURA  # Reseta o monstro para a direita

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)