import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from cat import Cat
from mouse import Mouse
from adding import Cheese_1, Cheese_2, Cheese_3, Intro, Title
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen objects
    pygame.init()  # initialize
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption('Protect Cheese')

    # play, exit and help button
    button_1 = Button(ai_settings, screen, 'Play')
    button_2 = Button(ai_settings, screen, 'Exit')
    button_3 = Button(ai_settings, screen, 'Help')

    # Create an instance to store game statistics, and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create a cat, a heart bullet group, a mouse group
    cat = Cat(ai_settings, screen)  # cat
    bullets = Group()   # heart bullet
    mouses = Group()   # mouse
    cheese_1 = Cheese_1(ai_settings, screen)
    cheese_2 = Cheese_2(ai_settings, screen)
    cheese_3 = Cheese_3(ai_settings, screen)
    intro = Intro(ai_settings, screen)
    title = Title(ai_settings, screen)

    # create a mouse group
    gf.create_fleet(ai_settings, screen, cat, mouses)

    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, button_1, button_2, cat, mouses, bullets, button_3, intro)

        if stats.game_active:
            cat.update()
            gf.update_bullets(ai_settings, screen, stats, sb, cat, mouses, bullets)
            gf.update_mouses(ai_settings, screen, stats, sb, cat, mouses, bullets)

        else:
            pygame.mouse.set_visible(True)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        gf.update_screen(ai_settings, screen, stats, sb, cat, mouses,intro, bullets,cheese_1, cheese_2, cheese_3, button_1, button_2, button_3,mouse_x, mouse_y, title)


run_game()

input('please input any key to exit!')

