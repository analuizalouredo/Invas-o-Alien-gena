import pygame.font
class Button():
    def __init__(self, ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width,self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        # O metodo pygame.font permite renderizar um texto na tela
        #O argumento None diz ao pygame para usar a fonte padrão e o 48 representa o tamanho
        self.font = pygame.font.SysFont(None,60)
        #Aqui ele vai construir e centralizar o objecto rect do botao
        self.rect = pygame.Rect(0,0,self.width,self.height)
        #Para centralizar o botão a gente coloca o rect dele para ser igual ao da tela
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    # O que ele vai fazer aqui é transformar o texto em imagem renderizada e exibir na tela
    def prep_msg(self,msg):
        # A função render transforma o texto armazenado em msg em uma imagem
        # Os argumentos são a msg que vc quer renderizar, o True serve para deixar as bordas mais suaves, a cor do texto e a cor do botão
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    #Esse método aqui vai desenhar o botão na tela
    def draw_button(self):
        # Aqui ele desenha o retânfulo do botão
        self.screen.fill(self.button_color,self.rect)
        #Aqui ele desenha a imagem do texto na tela
        self.screen.blit(self.msg_image,self.msg_image_rect)
