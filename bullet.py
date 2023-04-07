from pygame.sprite import Sprite
import pygame
#Essa classe vai administrar os projéteis disparados pela espaçonave
class Bullet (Sprite):
    #A classe Bullet vai herdar do Sprite. Com ele podemos agrupar os elementos relacionados ao jogo e atuar em todos eles de uma só vez
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        #Vamos agora criar um retangulo para definir a posição do projetil na origem 
        # Como o projétil não está baseado em uma imagem, precisamos, além de colocar as coordenadas em x e em y, também colocar a largura e altura
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #Aqui colocamos o rect do projétil para que sua parte superior coincida com o rect da nave, dando a impressão de que o projétil foi disparado pela nave
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #agora vamos armazenar a posição do projetil como um numero decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
    #Essa função vai servir para mover o projétil para cima na tela
    #Aqui ele vai atualizar a posição decimal do projétil
    # O projétil se mover para cima representa um decrescimo na coordenada y
        self.y -= self.speed_factor
    #Aqui ele vai atualizar a posição do rect
        self.rect.y = self.y
    
    #Essa função aqui vai desenhar o projétil na tela
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)