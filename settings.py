#Criando uma classe de configurações iniciais
class Settings():
    def __init__(self):
        self.tamanho_da_tela = 1200
        self.altura_da_tela = 800
        self.cor_de_fundo = (230,230,230)
        self.ship_limit = 3
        #adicionando as dimensões do projétil
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        #Isso daqui vai servir para limitar o número de projéteis que aparecem na tela
        self.bullets_allowed = 3
        #Isso daqui vai fazer com que a velocidade da nave aumente cada vez que ela mudar de fase
        self.speed_up_scale = 1.1
        #Taxa com que os pontos para cada alienígena morto aumentam
        self.score_scale = 1.5
        #Aqui a gente inicializa as configurações que permanecem constantes no método __init__()
        self.initialize_dynamic_settings()
        #Isso daqui serve para fazer a frota se mover para baixo também
        self.fleet_drop_speed = 1
        #fleet_direction =1 - nave se movimenta para a direita
        #fleet_direction = -1 - nave se movimenta para a esquerda

    def initialize_dynamic_settings(self):
                self.ship_speed_factor = 1.5
                self.bullet_speed_factor = 3
                self.alien_speed_factor = 0.5
                self.fleet_direction = 1
                self.alien_points = 50


    #Esse método aqui vai aumentar a velocidade do jogo
    def increase_speed (self):
           self.ship_speed_factor *= self.speed_up_scale
           self.bullet_speed_factor *= self.speed_up_scale
           self.alien_speed_factor *= self.speed_up_scale
           self.alien_points = int(self.alien_points*self.score_scale)
           print(self.alien_points)