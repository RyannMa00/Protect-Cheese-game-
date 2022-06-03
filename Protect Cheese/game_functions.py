import sys
from time import sleep   # can pause the game
import pygame
from bullet import Bullet
from mouse import Mouse
from button import Button
from adding import Cheese_1, Cheese_2, Cheese_3, Intro, Title


i = 0      # Define a variable to record whether display hints


def check_keydown_events(stats, sb, mouses, event, ai_settings, screen, cat, bullets):
    '''Respond to keystrokes'''
    # use arrow keys to control the cat
    if event.key == pygame.K_RIGHT:
        cat.moving_right = True     # move cat right

    elif event.key == pygame.K_LEFT:
        cat.moving_left = True      # move cat left

    elif event.key == pygame.K_UP:
        cat.moving_up = True        # move cat up

    elif event.key == pygame.K_DOWN:
        cat.moving_down = True      # move cat down

    # use spacebar to control bullets
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, cat, bullets)

    # Press Q or Esc to end the game
    elif event.key == pygame.K_q:
        sys.exit()

    # Press S to start the game
    elif event.key == pygame.K_s and not stats.game_active:
        begin_game(ai_settings, stats, sb, mouses, bullets, cat, screen)


def check_keyup_events(event,cat):
    '''Respond to release'''
    if event.key == pygame.K_RIGHT:
        cat.moving_right = False
    elif event.key == pygame.K_LEFT:
        cat.moving_left = False

    elif event.key == pygame.K_UP:
        cat.moving_up = False
    elif event.key == pygame.K_DOWN:
        cat.moving_down = False


def check_events(ai_settings, screen, stats, sb, button_1, button_2, cat, mouses, bullets, button_3, intro):
    '''Respond to keypress and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(stats, sb, mouses, event, ai_settings, screen, cat, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cat)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Btn =event.button
            check_play_and_exit_button(ai_settings, screen, stats, sb, button_1, button_2, cat, mouses, bullets, mouse_x, mouse_y)
            #check_confirm(ai_settings, screen, button_1, button_2, confirm, mouse_x, mouse_y, stats)
            check_hint_button(ai_settings, screen, button_3, intro, mouse_x, mouse_y, stats)
            #ClearHint(ai_settings, screen, Btn, mouse_x, mouse_y, stats)
        elif event.type == pygame.MOUSEBUTTONUP:
            Btn = event.button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ClearHint(ai_settings, screen, Btn, mouse_x, mouse_y, stats)
        #elif event.type == pygame.MOUSEMOTION:
        #    mouse_x, mouse_y = pygame.mouse.get_pos()
        #    check_hint_button(ai_settings, screen, button_3, intro, mouse_x, mouse_y, stats)

def check_play_and_exit_button(ai_settings, screen, stats, sb, button_1, button_2, cat, mouses, bullets, mouse_x, mouse_y):
    '''play and exit button'''

    button_1.play_button(ai_settings, screen, 'Play')
    button_2.exit_button(ai_settings, screen, 'Exit')

    button_1_clicked = button_1.play_bg_rect.collidepoint(mouse_x, mouse_y)
    button_2_clicked = button_2.exit_bg_rect.collidepoint(mouse_x, mouse_y)

    if button_1_clicked and not stats.game_active:
        begin_game(ai_settings, stats, sb, mouses, bullets, cat, screen)
    if button_2_clicked and not stats.game_active:
        sys.exit()

def check_hint_button(ai_settings, screen, button_3, intro, mouse_x, mouse_y, stats):
  # help button
    button_3.hint_button(ai_settings, screen, 'Help')
    button_3_clicked = button_3.hint_bg_rect.collidepoint(mouse_x, mouse_y)

    if button_3_clicked and not stats.game_active:
       #intro.blit()
       global i
       i = 1    # Becomes 1 to represent the need of display

def ClearHint(ai_settings, screen, Btn, mouse_x, mouse_y, stats):

    #if Btn == 3: #right click
       global i
       i = 0    # becomes 0 to represent no longer display

def update_screen(ai_settings, screen, stats, sb, cat, mouses,intro, bullets,cheese_1, cheese_2, cheese_3, button_1, button_2, button_3,mouse_x, mouse_y, title):
    '''Update the image on the screen and switch to the new screen'''
    # Redraw the screen every time you loop
    screen.fill(ai_settings.bg_color)

   # Redraw all bullets behind cat and mouse
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    cheese_1.blit()
    cheese_2.blit()
    cheese_3.blit()
    cat.blitme()
    mouses.draw(screen)
    title.blit()

    if not stats.game_active:
        # Show three buttons
        button_1.play_button(ai_settings, screen, 'Play')
        button_2.exit_button(ai_settings, screen, 'Exit')
        button_3.hint_button(ai_settings, screen, 'Help')
        if i==1:
            intro.blit()

        # A prompt appears when the mouse hovers over 'help'
        # check_hint_button(ai_settings, screen, button_3, intro, mouse_x, mouse_y, stats)

    # show score
    sb.show_score()

    # Make the most recently drawn screen become visible
    pygame.display.flip()


def fire_bullet(ai_settings, screen, cat, bullets):
    '''If the limit has not been reached, fire a bullet'''
    # Create a bullet and add it to the grouped bullets
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, cat)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, stats, sb, cat, mouses, bullets):
    '''Update bullet positions and delete the disappeared bullets'''
    bullets.update()

    # delete the disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_mouse_collisions(ai_settings, screen, stats, sb, cat, mouses, bullets)

def check_bullet_mouse_collisions(ai_settings, screen, stats, sb, cat, mouses, bullets):
    '''Responding to collisions of bullets and mouse'''
    collisions = pygame.sprite.groupcollide(bullets, mouses, True, True)  # Remove these bullets and mouse

    if collisions:
        for mouses in collisions.values():
            stats.score += ai_settings.mouse_points * len(mouses)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(mouses) == 0:
        # If the entire group of mouse is wiped out, raise one level
        bullets.empty()
        ai_settings.increase_speed()

        # improve grade
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, cat, mouses)

def get_number_mouses_x(ai_settings, mouse_width):
    '''Calculate how many mouse can fit in each row'''
    available_space_x = ai_settings.screen_width - 2 * mouse_width
    number_aliens_x = int(available_space_x / (2 * mouse_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, mouse_height):
    '''Calculate how many rows of mouse the screen can hold'''
    available_space_y = (ai_settings.screen_height - (3 * mouse_height) - ship_height)
    number_rows = int(available_space_y / (2 * mouse_height))
    return number_rows

def create_mouse(ai_settings, screen, mouses, mouse_number, row_number):
    '''Create a mouse and place it on the current line'''
    mouse = Mouse(ai_settings, screen)
    mouse_width = mouse. rect. width
    mouse.x = mouse_width + 2 * mouse_width * mouse_number
    mouse.rect.x = mouse.x
    mouse.rect.y = mouse.rect.height + 2 * mouse.rect.height * row_number + 50
    mouses.add(mouse)

def create_fleet(ai_settings, screen, cat, mouses):
    '''Create a mouse group'''
    # Create a mouse and count how many mouse can fit in a row
    mouse = Mouse(ai_settings, screen)
    number_mouses_x = get_number_mouses_x(ai_settings, mouse.rect.width)
    number_rows = get_number_rows(ai_settings, cat.rect.height, mouse.rect.height)

    # Create a mouse group
    for row_number in range(number_rows):
        for mouse_number in range(number_mouses_x):
            create_mouse(ai_settings, screen, mouses, mouse_number, row_number)

def check_fleet_edges(ai_settings, mouses):
    '''What to do when any mouse reaches the edge of screen'''
    for mouse in mouses.sprites():
        if mouse.check_edges():
            change_fleet_direction(ai_settings, mouses)
            break

def change_fleet_direction(ai_settings, mouses):
    '''Move the whole group of mouse down and change their move direction'''
    for mouse in mouses.sprites():
        mouse.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def cat_hit(ai_settings, screen, stats, sb, cat, mouses, bullets):
    ''' Responding when a cat is hit by a mouse'''
    if stats.cats_left > 0:
        # reduce one life
        stats.cats_left -= 1

        # update scoreboard
        sb.prep_cats()

        # Clear the mouse list and bullet list
        mouses.empty()
        bullets.empty()

        # Create a new group of mouse and place the cat at the bottom center of the screen
        create_fleet(ai_settings, screen, cat, mouses)
        cat.center_cat()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(False)

def check_mouses_bottom(ai_settings, screen, stats, sb, cat, mouses, bullets):
    '''Check if a mouse has reached the bottom of the screen'''
    screen_rect = screen.get_rect()
    for mouse in mouses.sprites():
        if mouse.rect.bottom >= screen_rect.bottom:
            # If the mouse reaches the bottom, handle it like the cat gets hit by the mouse
            cat_hit(ai_settings, screen, stats, sb, cat, mouses, bullets)
            break

def update_mouses(ai_settings, screen, stats, sb, cat, mouses, bullets):
    '''Check if any mouse is at the edge of the screen and update the position of all mouse in the group'''
    check_fleet_edges(ai_settings, mouses)
    mouses.update()

    # Detect collision between mouses and cat
    if pygame.sprite.spritecollideany(cat, mouses):
        cat_hit(ai_settings, screen, stats, sb, cat, mouses, bullets)

    # Check if a mouse reaches the bottom of the screen
    check_mouses_bottom(ai_settings, screen, stats, sb, cat, mouses, bullets)

def check_high_score(stats, sb):
    '''Check if a new top score is created'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def begin_game(ai_settings, stats, sb, mouses, bullets, cat, screen):
    # Indicates the start of the game
    # check_events(ai_settings, screen, stats, sb, button_1, button_2, cat, mouses, bullets, confirm, intro, hint)

    # reset game settings
    ai_settings.initialize_dynamic_settings()

    # hide cursor
    pygame.mouse.set_visible(False)

    # Reset game statistics
    stats.reset_stats()
    stats.game_active = True

    # Reset scoreboard image
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_cats()

    # Clear the mouse list and bullet list
    mouses.empty()
    bullets.empty()

    # Create a new group of mouse and center the cat
    create_fleet(ai_settings, screen, cat, mouses)
    cat.center_cat()

    pygame.display.flip()

