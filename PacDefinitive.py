import pygame

pygame.init()
clock = pygame.time.Clock()

# Unfinished Code
#Cores
preto = (0, 0, 0)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
laranja = (255, 165, 0)

velocidade = 2

class Cenario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]


    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = preto
            if coluna == 2:
                cor = laranja
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, amarelo, (x + half, y + half),
                                   self.tamanho // 12, 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)


class Pacman:
    def __init__(self):
        self.centro = [10, 10]
        self.vel = [0, 0]
        self.intencao = [0, 0]
        self.raio = 9
        self.boca = True
        self.direcao = 'direita'

    def verificar_pintura(self, tempo):
        global agora
        if tempo - agora > 150:
            agora = pygame.time.get_ticks()
            self.boca = not self.boca

    def pintar(self, tela, tempo):
        self.verificar_pintura(tempo)
        if self.boca:
            pygame.draw.circle(tela, amarelo, (self.centro[0], self.centro[1]), self.raio, 0)

        else:
            #Esquerda
            if self.direcao == 'esquerda':

                pygame.draw.circle(tela, amarelo, (self.centro[0], self.centro[1]), self.raio, 0)

                # Olho Esquerdo
                olho_x = int(self.centro[0] - self.raio / 3)
                olho_y = int(self.centro[1] - self.raio / 2)
                olho_raio = int(self.raio / 5)

                pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

                # Boca Esquerda
                canto_boca = [self.centro[0], self.centro[1]]
                superior_boca = [self.centro[0] - self.raio, self.centro[1] - self.raio // 2]
                inferior_boca = [self.centro[0] - self.raio, self.centro[1] + self.raio // 2]
                pontos = [canto_boca, superior_boca, inferior_boca]
                pygame.draw.polygon(tela, preto, pontos, 0)

            # Direita
            elif self.direcao == 'direita':

                pygame.draw.circle(tela, amarelo, (self.centro[0], self.centro[1]), self.raio, 0)

                #Olho Direito
                olho_x = int(self.centro[0] + self.raio / 3)
                olho_y = int(self.centro[1] - self.raio / 2)
                olho_raio = int(self.raio / 5)

                pygame.draw.circle(tela, preto,(olho_x, olho_y), olho_raio, 0)

                #Boca Direito
                canto_boca = [self.centro[0], self.centro[1]]
                superior_boca = [self.centro[0] + self.raio, self.centro[1] - self.raio // 2 ]
                inferior_boca = [self.centro[0] + self.raio, self.centro[1] + self.raio // 2 ]
                pontos = [canto_boca, superior_boca, inferior_boca]
                pygame.draw.polygon(tela, preto, pontos, 0)

            # Cima
            elif self.direcao == 'cima':
                pygame.draw.circle(tela, amarelo, (self.centro[0], self.centro[1]), self.raio, 0)

                # Olho Cima
                olho_y = int(self.centro[1] - self.raio / 3)
                olho_x = int(self.centro[0] - self.raio / 2)
                olho_raio = int(self.raio / 5)

                pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

                # Boca Cima
                canto_boca = [self.centro[0], self.centro[1]]
                superior_boca = [self.centro[0] - self.raio// 2, self.centro[1] - self.raio]
                inferior_boca = [self.centro[0] + self.raio// 2, self.centro[1] - self.raio]
                pontos = [canto_boca, superior_boca, inferior_boca]
                pygame.draw.polygon(tela, preto, pontos, 0)

            elif self.direcao == 'baixo':
                # Baixo
                pygame.draw.circle(tela, amarelo, (self.centro[0], self.centro[1]), self.raio, 0)

                # Olho Baixo
                olho_y = int(self.centro[1] + self.raio / 3)
                olho_x = int(self.centro[0] + self.raio / 2)
                olho_raio = int(self.raio / 5)

                pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

                # Boca Baixo
                canto_boca = [self.centro[0], self.centro[1]]
                superior_boca = [self.centro[0] + self.raio // 2, self.centro[1] + self.raio]
                inferior_boca = [self.centro[0] - self.raio // 2, self.centro[1] + self.raio]
                pontos = [canto_boca, superior_boca, inferior_boca]
                pygame.draw.polygon(tela, preto, pontos, 0)

    def processar_regras(self):
        self.centro[0] += self.vel[0]
        self.centro[1] += self.vel[1]
        self.limites = [
            [self.centro[0], self.centro[1] - self.raio],  # Up
            [self.centro[0] + self.raio, self.centro[1]],  # Right
            [self.centro[0], self.centro[1] + self.raio],  # Down
            [self.centro[0] - self.raio, self.centro[1]],  # Left
        ]

    def evento(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.vel[1] = -velocidade
                    self.vel[0] = 0
                    self.direcao = 'cima'

                elif e.key == pygame.K_DOWN:
                    self.vel[1] = velocidade
                    self.vel[0] = 0
                    self.direcao = 'baixo'

                elif e.key == pygame.K_RIGHT:
                    self.vel[0] = velocidade
                    self.vel[1] = 0
                    self.direcao = 'direita'

                elif e.key == pygame.K_LEFT:
                    self.vel[0] = -velocidade
                    self.vel[1] = 0
                    self.direcao = 'esquerda'

    def modo_debug(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.centro[1] -= 20

                elif e.key == pygame.K_DOWN:
                    self.centro[1] += 20
                    self.direcao = 'baixo'

                elif e.key == pygame.K_RIGHT:
                    self.centro[0] += 20
                    self.direcao = 'direita'

                elif e.key == pygame.K_LEFT:
                    self.centro[0] -= 20
                    self.direcao = 'esquerda'

def texto(texto):
    font1 = pygame.font.SysFont('freesanbold.ttf', 50)
    text = font1.render(texto, True, (0, 255, 0))
    return text

tela = pygame.display.set_mode((560, 580))

pacman = Pacman()
cenario = Cenario(20)
agora = 0
print(f'{len(cenario.matriz)} linhas')
print(f'{len(cenario.matriz[0])} colunas')

while True:
    # Regras
    clock.tick(60)
    pacman.processar_regras()
    tempo = pygame.time.get_ticks()

    # Pintar a tela
    tela.fill(preto)
    cenario.pintar(tela)
    pacman.pintar(tela, tempo)
    text1 = texto(f'{pacman.centro[0]//20}, {pacman.centro[1]//20}')
    tela.blit(text1, (pacman.centro[0], pacman.centro[1]))
    pygame.display.update()


    # Capturar eventos
    eventos = pygame.event.get()
    # pacman.evento(eventos)
    pacman.modo_debug(eventos)

    for e in eventos:
        if e.type == pygame.QUIT:
            exit()

