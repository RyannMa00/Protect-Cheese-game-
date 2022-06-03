import pygame.font


from pygame.sprite import Group
from cat import Cat

class Scoreboard():
    '''Class showing score information'''

    def __init__(self, ai_settings, screen, stats):
        '''Properties involved in initializing the reality score'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings to use when displaying score information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('inkfree', 25)

        # Prepare an image containing the highest score and the current score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_cats()
        self.prep_left_lives()


    def prep_score(self):
        '''Convert the current score to a rendered image'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = '{:,}' .format(rounded_score)
        self.score_image = self.font.render('Current Score: ' + score_str, True, self.text_color, self.ai_settings.bg_color)

        # Put the score in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 40

    def prep_high_score(self):
        '''Convert the highest score to a rendered image'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}' .format(high_score)
        self.high_score_image = self.font.render('Highest Score: ' + high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Put the highest score in the upper right corner of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.screen_rect.top

    def show_score(self):
        '''Show score and cat on screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.screen.blit(self.left_lives_image, self.left_lives_rect)

        # draw cat
        self.cats.draw(self.screen)

    def prep_level(self):
        '''Convert grades to rendered images'''
        self.level_image = self.font.render('Level: ' + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Put rank below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_cats(self):
        '''show remaining cats(lifes)'''
        self.cats = Group()
        for cat_number in range(self.stats.cats_left):
            cat = Cat(self.ai_settings, self.screen)
            cat.rect.x = 125 + cat_number * cat.rect.width
            cat.rect.y = 5
            self.cats.add(cat)

    def prep_left_lives(self):
        '''Show remaining life '''
        self.left_lives_image = self.font.render('Your Lives: ', True, self.text_color, self.ai_settings.bg_color)

        # Put life in the upper left corner of the screen
        self.left_lives_rect = self.left_lives_image.get_rect()
        self.left_lives_rect.centerx = 70
        self.left_lives_rect.centery = 40



