import sys #contem as funcionalidades do pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from pygame.sprite import Group
from scoreboard import Scoreboard
import pygame #usamos para sair do jogo caso o funcionario desista
#nesse arquivo vamos criar uma pasta que abre uma janela no pygame
def run_game():
    pygame.init() #inicializa as configurações de segundo plano que o pygame precisa pra funcionar de maneira adequada
    ai_settings = Settings ()
    tela = pygame.display.set_mode((ai_settings.tamanho_da_tela,ai_settings.altura_da_tela))
    pygame.display.set_caption('Invasão Alienigina')
    play_button = Button(ai_settings,tela,"Play")
    ship = Ship(ai_settings,tela)
    # Aqui ele vai criar uma frota de alienigenas
    aliens  = Group() #Cria um grupo vazio para armazenar todos os alienígenas da frota
    gf.create_fleet(ai_settings,tela,ship,aliens)
    #Vai criar um grupo para armazenar todos os projéteis ativos
    bullets = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(tela,ai_settings,stats)
    while True:
        gf.check_events(ai_settings, tela,stats,sb, play_button,ship,aliens,bullets)
        bullets.update()
        if stats.games_active:
            ship.update()
            gf.update_bullets(ai_settings,tela,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,tela,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,tela,stats,sb,ship,aliens,bullets,play_button)
        pygame.display.flip()
#Todo pressionamento de tecla fica registrado como um evento KEYDOWN, assim devemos verificar se a tecla pressionada dispara um determinado evento
run_game()  
