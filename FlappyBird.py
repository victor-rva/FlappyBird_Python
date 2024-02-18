import pygame
#biblioteca usada em criação de jogos
import os
#permite integrar o código com os arquivos do computador

from Chao import Chao
from Cano import Cano
from Passaro import Passaro

TELA_LAREGURA = 500
TELA_ALTURA = 800
#São constantes e não variáveis
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0)) # o que está dentro da tipla é a posição da imagem.
    for passaro in passaros:
        passaro.desenhar(tela)

    for cano in canos:
        cano.desenhar(tela)

    texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
    tela.blit(texto, (TELA_LAREGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()
 

def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((TELA_LAREGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        relogio.tick(30) # O parametro são quantos frames por segundo o jogo vai passar

        # Interação com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Para sair do jogo
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN: # Para pular com o passáro ao clicar na barra de espaço
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        # Mover as coisas
        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros): # O i é para pegar a posição do passaro dentro da lista
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)
        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_canos:
            canos.remove(cano)

        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or (passaro.y < 0):
                passaros.pop(i)

        desenhar_tela(tela, passaros, canos, chao, pontos)

if __name__ == '__main__':
    main()