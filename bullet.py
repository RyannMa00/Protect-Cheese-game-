import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''bullet'''

    def __init__(self, ai_settings, screen, ship):
        ''' create a bullet object at the location where the cat fire'''
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rectangle representing the bullet at (0, 0) and set its correct position
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # create bullet at (0,0), top left corner
        self.rect.centerx = (ship.rect.centerx - 10)
        self.rect.top = ship.rect.top                      # put the bullet at the correct place

        # store bullet position in decimal
        self.y = float(self.rect.y)

        # self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        ''' move bullet up '''
        # Update the decimal value representing the bullet position
        self.y -= self.speed_factor
        # Update the position of the 'rect' representing the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw bullets on the screen'''
        self.screen.blit(self.image, self.rect)



