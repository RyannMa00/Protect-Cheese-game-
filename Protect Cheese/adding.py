import pygame

class Cheese_1():
    '''bottom middle cheese'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.cheese = pygame.image.load('images/cheese.png').convert()
        self.cheese_rect = self.cheese.get_rect()

        self.cheese_rect.centerx = self.screen_rect.centerx
        self.cheese_rect.centery = (self.screen_rect.bottom - 25)

    def blit(self):
        self.screen.blit(self.cheese, self.cheese_rect)

class Cheese_2():
    '''bottom right cheese'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.cheese = pygame.image.load('images/cheese.png').convert()
        self.cheese_rect = self.cheese.get_rect()

        self.cheese_rect.centerx = (self.screen_rect.centerx + 200)
        self.cheese_rect.centery = (self.screen_rect.bottom - 25)

    def blit(self):
        self.screen.blit(self.cheese, self.cheese_rect)

class Cheese_3():
    '''bottom left cheese'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.cheese = pygame.image.load('images/cheese.png').convert()
        self.cheese_rect = self.cheese.get_rect()

        self.cheese_rect.centerx = (self.screen_rect.centerx - 200)
        self.cheese_rect.centery = (self.screen_rect.bottom - 25)

    def blit(self):
        self.screen.blit(self.cheese, self.cheese_rect)

class Intro():
    '''introduction part'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.intro_image = pygame.image.load('images/intro.png').convert()
        self.intro_image_rect = self.intro_image.get_rect()
        self.intro_image_rect.centerx = self.screen_rect.centerx
        self.intro_image_rect.centery = self.screen_rect.centery

    def blit(self):
        # show
        self.screen.blit(self.intro_image, self.intro_image_rect)

class Title():
    '''title'''
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.title_image= pygame.image.load('images/title.png').convert()
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.top = self.screen_rect.top

    def blit(self):
        self.screen.blit(self.title_image, self.title_image_rect)




