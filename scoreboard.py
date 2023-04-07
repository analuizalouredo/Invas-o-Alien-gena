import pygame.font
import pygame
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    #Essa  classe aqui irá mostrar informações sobre a pontuação
    def  __init__(self,screen,ai_settings,stats):
            self.screen = screen
            self.screen_rect = self.screen.get_rect()
            self.ai_settings = ai_settings
            self.stats = stats

            #Aqui estão as configurações para mostrar as informações da pontuação
            self.text_color = (30,30,30)
            self.font = pygame.font.SysFont (None,48)

            self.prep_score()
            self.prep_high_score()
            self.prep_level()
            self.prep_ship()
        
    def prep_score (self):
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.cor_de_fundo)
        #Aqui vamos configurar para ele exibir a configuração na parte superior da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        #Aqui ele desenha a imagem do nivel na tela
        self.screen.blit (self.level_image,self.level_image_rect)
        #Aqui vamos desenhar as espaçonaves na tela
        self.ships.draw(self.screen)
        
    #Transforma a pontuação máxima em uma imagem que vai renderizar na tela
    def prep_high_score(self):
        high_score = int (round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.cor_de_fundo)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.cor_de_fundo)
        self.level_image_rect = self.level_image.get_rect()
        #Aqui posicionamos o imagem do nivel logo abaixo da pontuação 
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    #Aqui queremos exibir quantas espaçonaves
    def prep_ship(self):
        #O Vai criar um grupo vazio para armazenar as instâncias das espaçonaves
        #Aqui estamos criando um grupo de espaçonaves
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship (self.ai_settings,self.screen)
            #Aqui definimos uma coordenada x para as espaçonaves para que elas apareçam lado a lado com uma distancia de 10 pixels entre si
            ship.rect.x = 10 + ship_number *ship.rect.width
            ship.rect.y = 10
            #Aqui adicionamos cada nova espaçonave ao grupo ships
            self.ships.add(ship)




         