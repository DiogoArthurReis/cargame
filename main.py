import pygame  # indica que utilizaremos pygame
from scripts.cenas import Partida
from scripts.cenas import Menu

pygame.init()  

tamanhoTela = [350, 500]  
tela = pygame.display.set_mode(tamanhoTela)  
pygame.display.set_caption("Car Game")  
relogio = pygame.time.Clock()  
corFundo = (0, 0, 0) 

offset_pista = 0
velocidade_pista = 5

def desenhar_pista(tela, offset):

    pygame.draw.rect(tela, (0, 0, 0), (50, 0, 250, 500))  
    

listaCenas = {
    'partida': Partida(tela),  
    'menu': Menu(tela)
}

cenaAtual = 'menu'
while True:
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT:  
            pygame.quit()  

    tela.fill(corFundo)  

    offset_pista += velocidade_pista
    if offset_pista >= 40: 
        offset_pista = 0

    desenhar_pista(tela, offset_pista)  

    cenaAtual = listaCenas[cenaAtual].atualizar()
    relogio.tick(60)  
    pygame.display.flip() 
