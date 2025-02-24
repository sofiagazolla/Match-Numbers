import pygame
import sys

pygame.init() # Inicialização do pygame
pygame.display.set_caption("Instruções")
tela = pygame.display.set_mode((900, 600))
relogio = pygame.time.Clock()

# Cores RGB
preto = (0, 0, 0)
lilas = (200, 162, 200)

# Carregar imagens e ajustá-las ao tamanho da tela
primeirapagina = pygame.image.load("imagemum.png")
segundapagina = pygame.image.load("imagemdois.png")
terceirapagina = pygame.image.load("imagemtres.png")
quartapagina = pygame.image.load("imagemquatro.png")
quintapagina = pygame.image.load("imagemcinco.png")
sextapagina = pygame.image.load("imagemseis.png")
setimapagina = pygame.image.load("imagemsete.png")
oitavapagina = pygame.image.load("imagemoito.png")

# Lista de páginas
paginas = [primeirapagina, segundapagina, terceirapagina, quartapagina, quintapagina, sextapagina, setimapagina, oitavapagina]
pagina_indice = 0  # Página inicial

fonte_botao = pygame.font.Font(None, 40) # Fonte para os botões

def desenhar_botoes(): #Desenha os botões de avançar e voltar na tela 
    # Botão avançar
    pygame.draw.rect(tela, lilas, (830, 530, 50, 50), border_radius=10)
    texto = fonte_botao.render(">", True, preto) 
    texto_rect = texto.get_rect(center=(830 + 50 // 2, 530 + 50 // 2))
    tela.blit(texto, texto_rect)
    # Botão voltar
    pygame.draw.rect(tela, lilas, (20, 20, 50, 50), border_radius=10)
    texto = fonte_botao.render("<", True, preto)
    texto_rect = texto.get_rect(center=(20 + 50 // 2, 20 + 50 // 2))
    tela.blit(texto, texto_rect)

def rodar_instrucoes(): #Loop principal das instruções
    global pagina_indice
    fim_instrucoes = False

    while not fim_instrucoes:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_instrucoes = True

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 830 <= evento.pos[0] <= 830 + 50 and 530 <= evento.pos[1] <= 530 + 50: # Detecta clique no botão de avançar
                    if pagina_indice < len(paginas) - 1:  # Não avança se já está na última página
                        pagina_indice += 1

                if 20 <= evento.pos[0] <= 20 + 50 and 20 <= evento.pos[1] <= 20 + 50: # Detecta clique no botão de voltar
                    if pagina_indice > 0:  # Não volta se já está na primeira página
                        pagina_indice -= 1
        
        tela.blit(paginas[pagina_indice], (0, 0)) # Desenha a página atual
        
        desenhar_botoes() # Desenha os botões

        pygame.display.flip() # Atualiza a tela
        
        relogio.tick(60) # Controla o FPS

    pygame.quit()
    sys.exit()

rodar_instrucoes() # Executa as instruções