import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 30
        self.vel_x = 1
        self.vel_y = 1
        self.RAIO = self.tamanho // 2

    def calcular_regras (self):
        self.centro_x = self.centro_x + self.vel_x
        self.centro_y = self.centro_y +self.vel_y

        if self.centro_x +self.RAIO >800:
            self.vel_x = -1
        if self.centro_x - self.RAIO <0:
            self.vel_x = 1

        if self.centro_y +self.RAIO >600:
            self.vel_y = -1
        if self.centro_y - self.RAIO <0:
            self.vel_y= 1







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

if __name__ == "__main__":
    pacman = Pacman()

    while True:
        #calcular as regras

        pacman.calcular_regras()


        #pintar na tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()

        #captura os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
