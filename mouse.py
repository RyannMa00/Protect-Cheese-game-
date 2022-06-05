import pygame

from pygame.sprite import Sprite

class Mouse(Sprite):
    '''class representing mouse'''

    def __init__(self, ai_settings, screen):
        super(Mouse, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the mouse image and set its rect property
        self.image = pygame.image.load('images/mouse.png').convert()
        self.rect = self.image.get_rect()

        # Each mouse is initially near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact location of the mouse
        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw a mouse at the specified location'''
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        '''Returns True if the mouse is at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        '''Move mouse left or right'''
        self.x += (self.ai_settings.mouse_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


''