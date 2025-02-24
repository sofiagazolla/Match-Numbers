import random
import pygame
import sys

pygame.init()
pygame.display.set_caption("Match Numbers")
larguratela, alturatela = 900, 600
tela = pygame.display.set_mode((larguratela, alturatela))
relogio = pygame.time.Clock()
mostrarcaixa = False
mostrargameover = False
mostrarvitoria = False

# Cores RGB
preto = (0, 0, 0)
branco = (250, 246, 241)
rosa = (254, 157, 208)
azul = (162, 210, 246)
azulclaro = (191,221,243)
roxo = (163, 73, 164)
lilas = (200, 162, 200)
    
fonte_nome = "Quicksand-SemiBold.ttf"
tamanho_fonte = 50
fonte = pygame.font.Font(fonte_nome, tamanho_fonte)

fonte_score = "Quicksand-SemiBold.ttf"
tamanho_fontescore = 45
fonte_score = pygame.font.Font(fonte_score, tamanho_fontescore)

fonte_botao = "Quicksand-SemiBold.ttf"
tamanho_fontebotao = 35
fontebotao = pygame.font.Font(fonte_botao, tamanho_fontebotao)

titulo = "Match numbers"

imagemtodos = pygame.image.load("todos.png")
imagemdois = pygame.image.load("dois.png")
imagemum = pygame.image.load("um.png")
imagemzero = pygame.image.load("zero.png")
imagematual = imagemtodos

class Botao:
    def __init__(self, x, y, altura, largura, cor, cor_hover, texto=''):
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.cor = cor
        self.cor_hover = cor_hover
        self.texto = texto

    # Função para criar o botão "Reiniciar"
    def desenhar_botao_reiniciar(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.largura and self.y <= mouse[1] <= self.y + self.altura:
            pygame.draw.rect(tela, self.cor_hover, (self.x, self.y, self.largura, self.altura), border_radius=20)
        else:
            pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura), border_radius=20)

        # Desenhar texto no botão
        texto = fontebotao.render(self.texto, True, preto)
        texto_rect = texto.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))
        tela.blit(texto, texto_rect)

    # Função para criar o botão "+"
    def desenhar_botao_mais(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] <= self.x + self.largura and self.y <= mouse[1] <= self.y + self.altura:
            pygame.draw.rect(tela, azul, (self.x, self.y, self.largura, self.altura), border_radius=20)
        else:
            pygame.draw.rect(tela, branco, (self.x, self.y, self.largura, self.altura), border_radius=20)
        texto = fonte.render(self.texto, True, preto)
        texto_rect = texto.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))
        tela.blit(texto, texto_rect)

        # Desenhar texto no botão
        texto = fontebotao.render(self.texto, True, preto)
        texto_rect = texto.get_rect(center=(self.x + self.largura // 2, self.y + self.altura // 2))
        tela.blit(texto, texto_rect)

class Grade:
        def __init__(self):
            self.LINHAS = 6
            self.COLUNAS = 6
            self.quadrado = 60
            self.grade = self.criar_grade(self.LINHAS, self.COLUNAS)

        # Função para criar a grade com números aleatórios
        def criar_grade(self, linhas, colunas):
            return [
                [random.randint(1, 9) for _ in range(colunas)]
                for _ in range(linhas)
            ]
        
        # Função para preencher espaços vazios com novos números
        def preencher_espacos_vazios(self):
            for x in range(self.LINHAS):
                for y in range(self.COLUNAS):
                    if self.grade[x][y] == 0:
                        self.grade[x][y] = random.randint(1, 9)

        numeros_adicionados = []  

        # Função para adicionar números aleatórios em posições vazias
        def adicionar_numeros_aleatorios(self, grade, quantidade):
            global numeros_adicionados
            self.numeros_adicionados = []  # Resetar a lista de números adicionados

            # Encontrar todas as posições vazias
            posicoes_vazias = [(x, y) for x in range(self.LINHAS) for y in range(self.COLUNAS) if grade[x][y] == 0]

            # Escolher aleatoriamente as posições a preencher
            if len(posicoes_vazias) > 0:
                escolhidas = random.sample(posicoes_vazias, min(quantidade, len(posicoes_vazias)))
                for pos in escolhidas:
                    x, y = pos
                    grade[x][y] = random.randint(1, 9)  # Adiciona um número aleatório
                    self.numeros_adicionados.append(pos)  # Rastrear posição adicionada

        # Função para verificar se dois números podem ser eliminados
        def pode_eliminar(self, pos1, pos2):
            x1, y1 = pos1
            x2, y2 = pos2
            num1 = self.grade[x1][y1]
            num2 = self.grade[x2][y2]

            # Verificar se os números são iguais ou se a soma é 10
            if (num1 != num2 and num1 + num2 != 10):
                return False
                
            # Caso 1: Mesma linha
            if x1 == x2:
                if (y1 < y2 or y1 > y2) and all(self.grade[x1][y] == 0 for y in range(min(y1, y2) + 1, max(y1, y2))):
                    return True
                # Verificar extremos da linha
                if (y1 == 0 and y2 == self.COLUNAS - 1) or (y2 == 0 and y1 == self.COLUNAS - 1):
                    return True
                
            # Caso 2: Mesma coluna
            if y1 == y2:
                if (x1 < x2 or x1 > x2) and all(self.grade[x][y1] == 0 for x in range(min(x1, x2) + 1, max(x1, x2))):
                    return True
                # Verificar extremos da coluna
                if (x1 == 0 and x2 == self.LINHAS - 1) or (x2 == 0 and x1 == self.LINHAS - 1):
                    return True
                
            # Diagonal
            if abs(x1 - x2) == abs(y1 - y2):  # Estão na mesma diagonal
                dx = 1 if x1 < x2 else -1
                dy = 1 if y1 < y2 else -1
                for step in range(1, abs(x1 - x2)):
                    if self.grade[x1 + step * dx][y1 + step * dy] != 0:
                        return False
                return True
            return False

        def ha_combinacoes(self):
            for x1 in range(self.LINHAS):
                for y1 in range(self.COLUNAS):
                    if self.grade[x1][y1] != 0:
                        for x2 in range(self.LINHAS):
                            for y2 in range(self.COLUNAS):
                                if (x1 != x2 or y1 != y2) and self.grade[x2][y2] != 0:
                                    if self.pode_eliminar((x1, y1), (x2, y2)):
                                        return True
            return False

        def verificar_vitoria(self):
            # Verifica se todos os valores da grade são 0
            return all(all(num == 0 for num in linha) for linha in self.grade)

        # Função para desenhar a grade na tela
        def desenhar_grade(self, grade, selecionados):
            for linha in range(self.LINHAS):
                for coluna in range(self.COLUNAS):
                    x = coluna * self.quadrado + 60
                    y = linha * self.quadrado + (alturatela - self.LINHAS * self.quadrado) // 2

                    # Cor do quadrado: destaque se selecionado
                    cor = branco if (linha, coluna) not in selecionados else azul

                    # Desenhar o quadrado
                    pygame.draw.rect(tela, cor, (x, y, self.quadrado, self.quadrado))
                    pygame.draw.rect(tela, preto, (x, y, self.quadrado, self.quadrado), 2)

                    # Desenhar o número
                    if grade[linha][coluna] != 0:  # Só desenha números não eliminados
                        cor_texto = roxo if (linha, coluna) in self.numeros_adicionados else preto
                        fonte = pygame.font.SysFont("Roboto", 45)
                        texto = fonte.render(str(grade[linha][coluna]), True, cor_texto)
                        tela.blit(texto, (x + self.quadrado // 3, y + self.quadrado // 4))

        # Função para criar a caixa de não há mais alternativas
        def desenhar_caixa(self, texto_linha1, texto_linha2):

            # Desenha o retângulo da caixa
            pygame.draw.rect(tela, lilas, (20, 220, 425, 135), border_radius=15)

            # Fonte e configuração
            fonte_caixa = pygame.font.Font("Quicksand-SemiBold.ttf", 20)

            # Renderiza e posiciona o texto da primeira linha
            texto_surface1 = fonte_caixa.render(texto_linha1, True, preto)
            texto_rect1 = texto_surface1.get_rect(center=(20 + 425 // 2, 220 + 135 // 3))
            tela.blit(texto_surface1, texto_rect1)

            # Renderiza e posiciona o texto da segunda linha
            texto_surface2 = fonte_caixa.render(texto_linha2, True, preto)
            texto_rect2 = texto_surface2.get_rect(center=(20 + 425 // 2, 220 + 2 * 135 // 3))
            tela.blit(texto_surface2, texto_rect2)             

class Sistema(Grade, Botao):
    def __init__(self, x, y, altura, largura, cor, cor_hover, texto=''):
        Botao.__init__(self, x, y, altura, largura, cor, cor_hover, texto)
        Grade.__init__(self)
        self.grade = self.criar_grade(self.LINHAS, self.COLUNAS)  # Criando Instância para usar na função da classe mãe (grade)
        self.fim_jogo = False
        self.selecionados = []
        self.tentativas = 3
        self.mostrarcaixa = False
        self.pontos = 0
        self.mostrargameover = False
        self.mostrarvitoria = False

    # Função principal do jogo
    def rodar_jogo(self):
        fim_jogo = False
        selecionados = []
        global imagematual
        global mostrarcaixa
        global mostrargameover
        global mostrarvitoria

        while not fim_jogo:
            tela.fill(rosa)

            #Escrevendo o título
            largura_caixa = 400
            altura_caixa = 40
            x_caixa = (larguratela - largura_caixa) // 2
            y_caixa = (altura_caixa)

            pygame.draw.rect(tela, rosa, (x_caixa, y_caixa, largura_caixa, altura_caixa), border_radius=10)
            pygame.draw.rect(tela, rosa, (x_caixa, y_caixa, largura_caixa, altura_caixa), 2, border_radius=10)

            # Renderizar o texto
            texto_surface = fonte.render(titulo, True, preto)
            texto_rect = texto_surface.get_rect(center=(x_caixa + largura_caixa // 2, y_caixa + altura_caixa // 2))
            tela.blit(texto_surface, texto_rect)

            #Escrevendo High Score:
            largura_caixa1 = 400
            altura_caixa1 = 360
            x1_caixa = (larguratela - largura_caixa1) // 2
            y1_caixa = (altura_caixa1)

            pygame.draw.rect(tela, rosa, (x1_caixa, y1_caixa, largura_caixa1, altura_caixa1), border_radius=10)
            pygame.draw.rect(tela, rosa, (x1_caixa, y1_caixa, largura_caixa1, altura_caixa1), 2, border_radius=10)

            # Renderizar o texto
            texto_surface = fonte_score.render(("Score: %d" % self.pontos), True, preto)
            texto_rect = texto_surface.get_rect(center=(x1_caixa + largura_caixa1 // 2, y1_caixa + altura_caixa1 // 2))
            tela.blit(texto_surface, texto_rect)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    coluna = (mouse_x - 60) // self.quadrado
                    linha = (mouse_y - (alturatela - self.LINHAS * self.quadrado) // 2) // self.quadrado

                    if 0 <= linha < self.LINHAS and 0 <= coluna < self.COLUNAS:
                        pos = (linha, coluna)

                        if self.grade[linha][coluna] != 0:  # Ignorar posições com valor 0
                            if pos in selecionados:
                                selecionados.remove(pos)
                            elif len(selecionados) < 2:
                                selecionados.append(pos)

                        # Verificar se dois números podem ser eliminados
                        if len(selecionados) == 2:
                            if self.pode_eliminar(selecionados[0], selecionados[1]):
                                print("Números eliminados!")
                                for sel in selecionados:
                                    x, y = sel
                                    self.grade[x][y] = 0
                                
                                # Calcular a distância entre os números
                                x1, y1 = selecionados[0]
                                x2, y2 = selecionados[1]
                                distancia = abs(x1 - x2) + abs(y1 - y2)

                                # Ajustar a pontuação com base na distância
                                totalpontos = distancia * 2  # Multiplicador de pontos
                                self.pontos += totalpontos
                            else:
                                print("Não podem ser combinados.")
                            selecionados = []

                if not self.ha_combinacoes():
                    if self.tentativas > 0 and not mostrarcaixa:
                        mostrarcaixa = True
                        
                    elif self.tentativas == 0 and not mostrargameover:
                        mostrargameover = True            

                self.desenhar_grade(self.grade, selecionados)

                #Criando botões usando classes
                botao_reiniciar = Botao(560, 200, 80, 200, branco, azulclaro, "Reiniciar")
                botao_mais = Botao(560, 310, 80, 80, branco, azulclaro, "+")
                
                # Modificar o botão de reiniciar para resetar as cores dos números
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_reiniciar.x <= evento.pos[0] <= botao_reiniciar.x + botao_reiniciar.largura and botao_reiniciar.y <= evento.pos[1] <= botao_reiniciar.y + botao_reiniciar.altura:
                        global numeros_adicionados
                        self.grade = self.criar_grade(self.LINHAS, self.COLUNAS)
                        self.tentativas = 3
                        imagematual = imagemtodos
                        self.pontos = 0
                        mostrargameover = False
                        mostrarvitoria = False
                        self.numeros_adicionados = []  # Resetar os números adicionados

                #Botão mais
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_mais.x <= evento.pos[0] <= botao_mais.x + botao_mais.largura and botao_mais.y <= evento.pos[1] <= botao_mais.y + botao_mais.altura:
                        if self.tentativas > 0:
                            if imagematual == imagemtodos:
                                imagematual = imagemdois
                            elif imagematual == imagemdois:
                                imagematual = imagemum
                            elif imagematual == imagemum:
                                imagematual = imagemzero
                            else:
                                imagematual = imagemtodos
                            self.adicionar_numeros_aleatorios(self.grade,10)
                            self.tentativas -= 1 
                            mostrarcaixa = False

                #Caixa de você ganhou
                if self.verificar_vitoria() and mostrarvitoria:
                    mostrarvitoria = True
                    self.desenhar_caixa("Parabéns, você venceu!", "Reinicie o jogo para jogar novamente!")
                    fim_jogo = True 

            botao_reiniciar.desenhar_botao_reiniciar()
            botao_mais.desenhar_botao_mais()
            self.desenhar_grade(self.grade, selecionados)
            self.ha_combinacoes()
            
            #Desenhar a imagem redimensionada ao lado do botão "+"
            imagem_x = botao_mais.x + botao_mais.largura + 10  # Ao lado direito do botão "+"
            imagem_y = botao_mais.y  # Alinhada verticalmente
            tela.blit(imagematual, (imagem_x, imagem_y))

            if mostrarcaixa:
                self.desenhar_caixa("Não há mais combinações possíveis!", "Adicione mais números ou reinicie!")

            if mostrargameover:
                self.desenhar_caixa("Game Over!", "Reinicie o jogo!")

            pygame.display.flip()
            relogio.tick(60)

        pygame.quit()
        sys.exit() 

# Executa o jogo
if __name__ == "__main__":
    sistema = Sistema(10, 10, 50, 100, branco, azul, "Reiniciar")
    sistema.rodar_jogo()