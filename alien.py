from pygame.sprite import Sprite
import pygame
#Essa classe irá guardar informações sobre os alienpigenas da frota
class Alien (Sprite):
    def __init__ (self,ai_settings,screen):
        #Primeiramente vamos definir a posição inicial
        super(Alien,self).__init__()
        #Carrega na tela a imagem do alienigina
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #Vamos agora iniciar cada novo alienígina no canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Ele vai armazenar a posição do exata do alienigina como um valor decimal
        self.center = float(self.rect.centerx)

        #Esse módulo aqui desenha o alienígina em sua posição atual
    def blitme(self):
            self.screen.blit(self.image ,self.rect)

    #Essa função aqui vai atualizar a posição dos alienígenas a medida que eles forem se movendo
    def update(self):
         #Controla a posição exata do alienígena
         self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
         #Sempre que atualizarmos a posição de um alienígena ele se move para a direita na mesma velocidade que foi armazenado pelo speed factor
         self.rect.x = self.x

    #Essa função aqui vai verificar quando os alienígenas atingiram as bordas
    #Quando eles atingem as bordas eles devem se mover para baixo
    def check_edges(self):
         screen_rect = self.screen.get_rect()
         #Retorna True sempre que a frota atinge as bordas da página
         if self.rect.right >= screen_rect.right:
              return True
         elif self.rect.left <= 0:
              return True
#Código para ver quantos alienígenas há na tela 
# espaço_disponivel = largura_da_tela - 2*largura_do_alienigina
#numero_de_aliens = espaço_disponivel / (2*largura_do_alienigena)

#Método sprite.groupcollide() - vai comparar o rect de cada projétil com o rect de cada alienígena e devolver um dicionário contendo os projéteis e os alienígenas que colidiram
#No caso cada key do dicionário vai ser um alienígena e os values vão ser os respectivos projéteis que colidiram
