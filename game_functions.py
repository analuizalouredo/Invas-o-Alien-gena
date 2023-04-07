import sys
import pygame
from bullet import Bullet 
from alien import Alien
from pygame.sprite import Sprite
from time import sleep

#Quando pressionamos o espaço criamos uma nova instância de Bullet que é armazenada em new_bullet e adicionamos ao grupo bullets com o método add
def check_keydown_events (event,ai_settings, screen, ship,bullets):
         if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
                ship.moving_right= True 
         if event.key == pygame.K_LEFT:
                ship.rect.centerx-=1
                ship.moving_left= True 
         elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen,ship, bullets)
         elif event.key == pygame.K_q:
               sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
            ship.moving_right = False
    if event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_events(ai_settings, screen,stats,sb,play_button,ship,aliens,bullets):
    #Função que faz o programa responder ao pressionamento de telcas e de mouse
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
      #Aqui ele vai verificar quando o botão do play for apertado pra poder inicializar o jogo
        # O método MOUSEBUTTONDOWN vai deterctar sempre que voce clicar no mouse
        #A função check_play_button serve para que o jogo só inicializa quando o botão do play for apertado
         elif event.type == pygame.KEYDOWN:
             check_keydown_events(event,ai_settings,screen,ship,bullets)

         elif event.type == pygame.KEYUP:
             check_keyup_events(event,ship)
         elif event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_x, mouse_y = pygame.mouse.get_pos()
                  check_play_button (ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
        
def update_screen (ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    #atualiza as imagens na tela e alterna para uma nova tela
    screen.fill(ai_settings.cor_de_fundo)
    #Redesenha todos os projéteis atrás da espaçonave
    for bullet in bullets.sprites():
         #O método bullets.sprites() retorna uma lista de todos os sprites do grupo bullets
         bullet.draw_bullet()
    ship.blitme()
    #Isso daqui desenha os alienígenas na tela depois que a nave e os projéteis já tiverem sido desenhados 
    aliens.draw(screen)
    sb.show_score()
    #Exibe o botão só quando o jogo estiver inativo
    if not stats.games_active:
          play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
     bullets.update()
     #aqui ele vai se livrar ods projéteis que desapareceram para que eles não fiquem armazenando memória desnecessriamente
     for bullet in bullets.copy():
            #O método copy permite que a gente prepare o laço for e modifique oos bullets no laço
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
                # Esse print serve para a gente ver quantos projéteis ainda existem no jogo e se de fato eles foram removidos
                #print(len(bullets))
     # Aqui ele vai  verificar se algum proétil atingiu os alienígenas
     check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

      
def fire_bullet(ai_settings, screen,ship, bullets):
    #Aqui criamos um projétil e o adicionamos ao grupo de projéteis
            if len(bullets) < ai_settings.bullets_allowed:
                 new_bullet = Bullet(ai_settings,screen,ship)
                 bullets.add(new_bullet)

 #Esse código aqui calcula a quantidade de linhas disponivel para a frota, de modo que haja um espaçamento do tamanho de uma espaçonave disponivel entre cada linha
def get_number_rows(ai_settings,ship_height,alien_height):
      available_space_y = (ai_settings.altura_da_tela) - (3*alien_height) - (ship_height)
      number_rows = int(available_space_y/(2*alien_height))
      return number_rows
#Vai determinar quantos alienígenas cabem em uma linha
def get_number_aliens_x (ai_settings,alien_width):
      espaco_disponivel = ai_settings.tamanho_da_tela-2*alien_width
      numero_de_aliens = int(espaco_disponivel/(2*alien_width))
      return numero_de_aliens



def create_alien(ai_settings,screen,aliens,alien_number,row_number):
      #Cria um alienígena que não fará parte da frota, ele serve apenas para obtermos informações acerca do tamanho dos aliens
      alien = Alien (ai_settings,screen)
       #Usamos o atributo rect para obter a largura do alienígena
      alien_width = alien.rect.width
        #Define a coordenada x do alienígena
      alien.rect.x = alien.x = alien_width + 2*alien_width*alien_number
      alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
      
      aliens.add(alien)   

#Essa função aqui vai criar a frota de alienígenas
def create_fleet(ai_settings,screen,ship,aliens):
      #Primeiro ele vai criar um alienígena e vai calcular o número de alienígenas em uma linha
      #O espaçamento entre os alienígenas é igual a largura de um alienígena
      alien = Alien(ai_settings,screen)
      number_aliens_x = get_number_aliens_x (ai_settings,alien.rect.width)
      number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
      #Aqui vamos criar a primeira linha de alienígenas
      #Nesse laço for ele vai criar um número de alienígenas que seja suficiente para preencher toda a tela
      for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
                create_alien(ai_settings,screen,aliens,alien_number,row_number)
#Essa função aqui vai atualizar a posição dos alienígenas a cada passagem para o laço do while
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
     check_fleet_edges(ai_settings,aliens)
     aliens.update()
     #Aqui vamos verificar se houve colisão entre alienígena e espaçonave
     #O método spritecollideany verifica se houve colisão entre algum membro do grupo e a espaçonave
     # Caso ocorra essa colisão ele para imediatamente de percorrer o grupo
     #Repare que nesse caso ele vai devolver sempre o primeiro alienigena que tenha colidido com a nave
     #Caso nenhuma colisão tenha acontecido o método vai devolver None e então nem vai entrar nesse if
     if pygame.sprite.spritecollideany(ship,aliens):
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
     check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_fleet_edges(ai_settings, aliens):
      #Verifica se algum alienigena já alcançou as bordas
      for alien in aliens.sprites():
            if alien.check_edges():
                  change_fleet_direction(ai_settings,aliens)
                  break

#Quando o alienígena encontra a borda essa função aqui faz ele descer e mudar de direção
def change_fleet_direction(ai_settings,aliens):
      for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleet_drop_speed
      ai_settings.fleet_direction *= -1

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
      collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    # Os dois True vão fazer com que após a colisão os projéteis e os aliens que colidiramm sejam imediatamente destruídos
      if collisions:
            for aliens in collisions.values():
                  stats.score += ai_settings.alien_points * len(aliens)
                  sb.prep_score()
                  #Chamamos a função aqui pra que ela seja sempre atualizada quando um alienígena for atingido
            check_high_score(stats,sb)
      if len(aliens) == 0:
           #Aqui ele destroi os projéteis existentes e cria uma nova frota
           bullets.empty()
           ai_settings.increase_speed()
           # Quando a frota for destruída ele aumenta o nível
           stats.level += 1
           sb.prep_level()
           create_fleet(ai_settings,screen,ship,aliens)
                  
#Essa função aqui vai dar uma resposta sempre que a nave for atingida por um alienígena
def ship_hit (ai_settings,stats, screen,sb,ship, aliens, bullets):
      if stats.ships_left > 0 :
            stats.ships_left -= 1
            sb.prep_ship()
      else:
            stats.game_active = False
            #Assim que o jogo acabar ele vai deixar o cursor do mouse visível de novo
            pygame.mouse.set_visible(True)
      #Agora vamos esvaziar a lista de alienígenas e projéteis
      aliens.empty()
      bullets.empty()
       #Agora ele vai criar uma nova frota e centralizar de novo a nave
      create_fleet(ai_settings,screen,ship,aliens)
      ship.center_ship()
      sleep(0.5)

#Essa função aqui vai verificar se algum alienigena atingiu a parte inferior da tela
def check_aliens_bottom (ai_settings,stats,sb,screen,ship,aliens,bullets):
      screen_rect = screen.get_rect()
      for alien in aliens.sprites():
            #Aqui ele tá verificando se o alienígena já alcançou a parte inferior da tela
            if alien.rect.bottom >= screen_rect.bottom:
                  ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
                  break #Isso garante que uma nova frota apareça sempre que um alienígena alcançar a parte inferior da tela
def check_play_button (ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
#Esse método collidepoint serve para verificar se o ponto que o clique do mouse ocorreu se sobrepoe com o retangulo do botão de play
      button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
      if button_clicked and not stats.games_active:
            #Aqui ele vai reiniciar as configurações do jogo sempre que o jogador clicar play
            ai_settings.initialize_dynamic_settings()
            #Aqui ele vai ocultar o botão do mouse depois  que o jogo já tiver começado
            pygame.mouse.set_visible(False) #Passar o false para essa função set_visible() diz ao pygame para ocultar o mouse
           #Aqui ele vai reiniciar os dados estatísticos do jogo
            stats.reset_stats()
            stats.games_active = True
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ship()
            #Aqui ele vai esvaziar a lista de alienígenas e projéteis
            aliens.empty()
            bullets.empty()
            #Aqui ele vai criar uma nova frota
            create_fleet(ai_settings,screen,ship,aliens)
            #Aqui ele centraliza a nave 
            ship.center_ship()
#Essa função daqui vai verificar se há uma pontuação maxima e se o jogador já atingiu a pontuação máxima
def check_high_score(stats,sb):
      #Aqui ele verifica se a pontuação atual é maior que o máximo
      if stats.score > stats.high_score:
            # Se a pontuação atual for maior que o máximo a pontuação atual assume o valor do máximo
            stats.high_score = stats.score
            #Essa função aqui vai atualizar a imagem da pontuação máxima sempre que ela for modificada
            sb.prep_high_score()

