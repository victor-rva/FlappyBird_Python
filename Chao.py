import pygame
#biblioteca usada em criação de jogos
import os
#permite integrar o código com os arquivos do computador

IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        # x1 se refere ao chão 1 e o x2 se refere ao chão 2

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        # Está diminuindo por que o chão está se movendo para esquerda, como o ponto de referência do pygame
        #é a ponta esqeurda de cima, quando se quer mover algo para esquerda precisa diminuir ou ser negativo.

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA

        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))
