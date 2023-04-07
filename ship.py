import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,tela):
        #Carrega a imagem da espaçonave
        super(Ship,self).__init__()
        self.ai_settings = ai_settings
        self.tela = tela
        self.image = pygame.image.load('images/ship.bmp')
        #usamos a função get_rect() para acessar o atributo rect da superfície
        self.rect = self.image.get_rect()
        self.screen_rect = tela.get_rect()
        self.center = float(self.screen_rect.centerx)
        self.moving_right= False
        self.moving_left = False
        #Vamos iniciar cada mova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx #coordenada x do centro da espaçonave coincide com o atributo centerx do retangulo da tela
        self.rect.bottom = self.screen_rect.bottom
    #o método blitme desenha a imagem da tela na posição especificada
    def blitme(self):
        self.tela.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right <self.screen_rect.right:
           # self.rect.centerx+=1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx= self.center
            #self.rect.centerx -=1
    #Esse método aqui vai servir para centralizar a nave após uma colisão
    def center_ship (self):
        self.center = self.screen_rect.centerx


