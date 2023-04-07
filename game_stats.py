import pygame
#Aqui iremos armazenar as estatísticas do jogo
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Vamos agora criar uma flag que vai encerrar o jogo sempre que o jogador ficar sem espaçonaves
        #Isso aqui garante que o jogo so inicia quando o jogador aperta o play
        self.games_active = False
        #Pontuação máxima que um jogador pode atingir
        self.high_score = 0
        

#Aqui ele vai inicializar os dados estatísticos que podem mudar durante o jogo
#Vamos fazer em uma função fora do init porque assim conseguiremos reiniciar algumas estatísticas sempre que o jogador comelar um novo jogo
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 
        self.level = 1
        