import pygame

from pygame.sprite import Sprite

class Cat(Sprite):
    def __init__(self, ai_settings, screen):
        '''Initialize cat and set its initial position'''
        super(Cat, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load cat image and get its bounding rectangle
        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()  # rect represents a rectangle object, where the bounding rectangle of the cat is obtained
        self.screen_rect = screen.get_rect()

        # Place each new cat in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value in cat's property center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''Adjust the cat's position based on the moving sign'''
        # Update the center value of the cat, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.cat_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.cat_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.cat_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.cat_speed_factor

        # Update the rect object based on self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def blitme(self):
        '''draw cat at specified location'''
        self.screen.blit(self.image, self.rect)

    def center_cat(self, ):
        '''Center the cat on the screen'''
        self.centerx = self.screen_rect.centerx
        self.centery = (self.screen_rect.bottom - 35)


