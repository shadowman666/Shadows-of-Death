# code/Const.py
import pygame

# Configurações de Janela
LARGURA = 800
ALTURA = 600
TITULO_JOGO = "Shadows of Death"

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (138, 7, 7)
VERMELHO_CLARO = (255, 0, 0)
CINZA_ESCURO = (30, 30, 30)

# Estado do Jogo
MENU = 'MENU'
CONTROLES = 'CONTROLES'
JOGANDO = 'JOGANDO'
SAIR = 'SAIR'

# Caminhos de Assets
SND_MENU = 'asset/sounds/menu_terror.wav'
SND_GAME = 'asset/sounds/jogo_terror.wav'
IMG_FUNDO_MENU = 'asset/images/fundo_menu.png'
IMG_FUNDO_JOGO = 'asset/images/fundo_jogo.png'
SND_HIT = 'asset/sounds/hit.wav'      # Som de quando você é atingido
SND_DEATH = 'asset/sounds/death.wav'  # Som de morte do inimigo/player
IMG_ENEMY = 'asset/images/monster.png' # Sua imagem de monstro

# Camadas de Parallax
IMG_BG_LAYER_0 = 'asset/images/bg_longe.png' # Move-se devagar
IMG_BG_LAYER_1 = 'asset/images/bg_perto.png' # Move-se rápido