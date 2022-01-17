import pygame

pygame.init()
clock = pygame.time.Clock()


#Cores
preto = (0, 0, 0)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

velocidade = 2

class Cenario:
    def __init__(self, tamanho, pac):
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
                cor = azul
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, amarelo, (x + half, y + half),
                                   self.tamanho // 12, 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)




class Pacman:
    def __init__(self):
        self.centro_x = 255
        self.centro_y = 255
        self.raio = 9
        self.vel_x = 0
        self.vel_y = 0
        self.direcao = 'direita'
        self.intencao_x = 0
        self.intencao_y = 0


    def pintar_boca(self, tela):
        #Esquerda
        if self.direcao == 'esquerda':

            pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

            # Olho Esquerdo
            olho_x = int(self.centro_x - self.raio / 3)
            olho_y = int(self.centro_y - self.raio / 2)
            olho_raio = int(self.raio / 5)

            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

            # Boca Esquerda
            canto_boca = [self.centro_x, self.centro_y]
            superior_boca = [self.centro_x - self.raio, self.centro_y - self.raio // 2]
            inferior_boca = [self.centro_x - self.raio, self.centro_y + self.raio // 2]
            pontos = [canto_boca, superior_boca, inferior_boca]
            pygame.draw.polygon(tela, preto, pontos, 0)

        # Direita
        elif self.direcao == 'direita':

            pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

            #Olho Direito
            olho_x = int(self.centro_x + self.raio / 3)
            olho_y = int(self.centro_y - self.raio / 2)
            olho_raio = int(self.raio / 5)

            pygame.draw.circle(tela, preto,(olho_x, olho_y), olho_raio, 0)

            #Boca Direito
            canto_boca = [self.centro_x, self.centro_y]
            superior_boca = [self.centro_x + self.raio, self.centro_y - self.raio // 2 ]
            inferior_boca = [self.centro_x + self.raio, self.centro_y + self.raio // 2 ]
            pontos = [canto_boca, superior_boca, inferior_boca]
            pygame.draw.polygon(tela, preto, pontos, 0)

        # Cima
        elif self.direcao == 'cima':
            pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

            # Olho Cima
            olho_y = int(self.centro_y - self.raio / 3)
            olho_x = int(self.centro_x - self.raio / 2)
            olho_raio = int(self.raio / 5)

            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

            # Boca Cima
            canto_boca = [self.centro_x, self.centro_y]
            superior_boca = [self.centro_x - self.raio// 2, self.centro_y - self.raio]
            inferior_boca = [self.centro_x + self.raio// 2, self.centro_y - self.raio]
            pontos = [canto_boca, superior_boca, inferior_boca]
            pygame.draw.polygon(tela, preto, pontos, 0)

        elif self.direcao == 'baixo':
            # Baixo
            pygame.draw.circle(tela, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

            # Olho Baixo
            olho_y = int(self.centro_y + self.raio / 3)
            olho_x = int(self.centro_x + self.raio / 2)
            olho_raio = int(self.raio / 5)

            pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

            # Boca Baixo
            canto_boca = [self.centro_x, self.centro_y]
            superior_boca = [self.centro_x + self.raio // 2, self.centro_y + self.raio]
            inferior_boca = [self.centro_x - self.raio // 2, self.centro_y + self.raio]
            pontos = [canto_boca, superior_boca, inferior_boca]
            pygame.draw.polygon(tela, preto, pontos, 0)

    def processar_regras(self):
        self.centro_x += self.vel_x
        self.centro_y += self.vel_y

    def evento(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.vel_y = -velocidade
                    self.vel_x = 0
                    self.direcao = 'cima'

                elif e.key == pygame.K_DOWN:
                    self.vel_y = velocidade
                    self.vel_x = 0
                    self.direcao = 'baixo'

                elif e.key == pygame.K_RIGHT:
                    self.vel_x = velocidade
                    self.vel_y = 0
                    self.direcao = 'direita'

                elif e.key == pygame.K_LEFT:
                    self.vel_x = -velocidade
                    self.vel_y = 0
                    self.direcao = 'esquerda'

tela = pygame.display.set_mode((560, 580))
pacman = Pacman()
cenario = Cenario(20, pacman)

while True:

    # Regras
    clock.tick(60)
    pacman.processar_regras()

    # Pintar a tela
    tela.fill(preto)
    cenario.pintar(tela)
    pacman.pintar_boca(tela)
    pygame.display.update()


    # Capturar eventos
    eventos = pygame.event.get()
    pacman.evento(eventos)

    for e in eventos:
        if e.type == pygame.QUIT:
            exit()





