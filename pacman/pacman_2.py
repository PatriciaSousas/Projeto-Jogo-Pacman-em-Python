import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1  # type: int

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.coluna = 2
        self.linha = 2
        self.tamanho = 800//50
        self.vel_x = 0
        self.vel_y = 0
        self.RAIO = self.tamanho // 2

    def calcular_regras (self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha +self.vel_y
        self.centro_x = int(self.coluna* self.tamanho + self.RAIO)
        self.centro_y = int(self.linha* self.tamanho + self. RAIO)



    def pintar(self, tela):
        self.RAIO = self.tamanho
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.RAIO)

        #boca Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_sup = (self.centro_x + self.RAIO, self.centro_y - self.RAIO)
        labio_inf = (self.centro_x + self.RAIO, self.centro_y)
        pontos = [canto_boca, labio_sup, labio_inf]

        pygame.draw.polygon(tela, PRETO, pontos, 0)

        #olhos do pacman
        olho_x = int(self.centro_x + self.RAIO /3)
        olho_y = int(self.centro_y - self.RAIO * 0.70)
        olho_raio = int(self.RAIO / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio)

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                if e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                if e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                if e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if e.key == pygame.K_LEFT:
                    self.vel_x = 0
                if e.key == pygame.K_UP:
                    self.vel_y = 0
                if e.key == pygame.K_DOWN:
                    self.vel_y = 0


if __name__ == "__main__":
    pacman = Pacman()

    while True:
        #calcular as regras

        pacman.calcular_regras()


        #pintar na tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()
        pygame. time. delay(100)

        #captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type ==pygame.QUIT:
                exit()

        pacman.processar_eventos(eventos)

