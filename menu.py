import pygame
import sys
import os

# Inicialização do Pygame
pygame.init()

# Definir as cores
preto = (0, 0, 0)  
branco = (250, 246, 241)
rosa = (254, 157, 208)
azul = (162, 210, 246)
azulclaro = (191,221,243)
roxo = (163, 73, 164)
lilas = (200, 162, 200)
rosapink = (255, 0, 127)

# Tamanho da tela
larguratela = 900
alturatela = 600
tela = pygame.display.set_mode((larguratela, alturatela))
pygame.display.set_caption("Menu Principal")

fundo = pygame.image.load("fundo.png")

# Função para desenhar um botão com bordas arredondadas
def draw_button(text, x, y, width, height, color, hover_color):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)

    # Mudança de cor quando o mouse passa sobre o botão
    if button_rect.collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(tela, hover_color, button_rect, border_radius=15)
    else:
        pygame.draw.rect(tela, color, button_rect, border_radius=15)

    # Carregar a fonte Quicksand-SemiBold.ttf corretamente
    try:
        font = pygame.font.Font("Quicksand-SemiBold.ttf", 30)  # Usando a fonte externa
    except FileNotFoundError:
        print("Fonte não encontrada! Verifique se o arquivo Quicksand-SemiBold.ttf está no diretório atual.")
        sys.exit()  # Fecha o programa se a fonte não for encontrada

    text_surf = font.render(text, True, preto)
    text_rect = text_surf.get_rect(center=button_rect.center)
    tela.blit(text_surf, text_rect)

# Função para desenhar o título
def draw_title():
    # Carregar a fonte Quicksand-SemiBold.ttf corretamente
    try:
        font = pygame.font.Font("Quicksand-SemiBold.ttf", 48)  # Usando a fonte externa
    except FileNotFoundError:
        print("Fonte não encontrada! Verifique se o arquivo Quicksand-SemiBold.ttf está no diretório atual.")
        sys.exit()  # Fecha o programa se a fonte não for encontrada

    title_surf = font.render("Match Numbers", True, preto)
    # Calculando a posição do título proporcionalmente acima dos botões
    title_rect = title_surf.get_rect(center=(larguratela // 2, 150))  # Posição ajustada
    tela.blit(title_surf, title_rect)

# Função principal do menu
def menu():
    while True:
        tela.blit(fundo, (0, 0))

        # Desenhar o título
        draw_title()

        # Coordenadas dos botões (centralizando)
        largura_botao = 300
        altura_botao = 50
        x_button = (larguratela - largura_botao) // 2  # Centralizando o botão
        y_button_1 = 250  # Posição do primeiro botão
        y_button_2 = 350  # Posição do segundo botão

        # Detectando os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Coordenadas dos botões
                if x_button < pygame.mouse.get_pos()[0] < x_button + largura_botao and y_button_1 < pygame.mouse.get_pos()[1] < y_button_1 + altura_botao:
                    # Clicar no botão "Jogo"
                    os.system('python main.py')  # Abre o jogo
                if x_button < pygame.mouse.get_pos()[0] < x_button + largura_botao and y_button_2 < pygame.mouse.get_pos()[1] < y_button_2 + altura_botao:
                    # Clicar no botão "Instruções"
                    os.system('python instrucoes.py')  # Abre as instruções

        # Desenhando os botões (centralizados)
        draw_button("Jogar", x_button, y_button_1, largura_botao, altura_botao, rosapink, rosa)
        draw_button("Instruções", x_button, y_button_2, largura_botao, altura_botao, roxo, lilas)

        # Atualizar a tela
        pygame.display.flip()

# Rodar o menu
if __name__ == "__main__":
    menu()