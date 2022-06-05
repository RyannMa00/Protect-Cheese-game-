import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        '''Initialize button properties'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

         # Set button dimensions and other properties
        self.width, self.height = 200, 50
        self.button_color = (54,54,54)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('inkfree', 28)   # comicsansms, georgia, inkfree

    # play button
    def play_button(self, ai_settings, screen, msg):
        # button border
        self.play_bg_rect = pygame.Rect(0, 0, self.width, self.height)
        self.play_bg_rect.centerx = self.screen_rect.centerx
        self.play_bg_rect.centery = self.screen_rect.centery - 100

        # text on button
        self.play_button_image = self.font.render('Play', True, self.text_color, self.button_color)
        self.play_button_image_rect = self.play_button_image.get_rect()
        self.play_button_image_rect.centerx = self.screen_rect.centerx
        self.play_button_image_rect.centery = (self.screen_rect.centery - 100)

        # show the entire button
        self.screen.fill(self.button_color, self.play_bg_rect)
        self.screen.blit(self.play_button_image, self.play_button_image_rect)


    # exit button
    def exit_button(self, ai_settings, screen, msg):
        # button border
        self.exit_bg_rect = pygame.Rect(0, 0, self.width, self.height)
        self.exit_bg_rect.centerx = self.screen_rect.centerx
        self.exit_bg_rect.centery = (self.screen_rect.centery + 100)

        # text on button
        self.exit_button_image = self.font.render('Exit', True, self.text_color, self.button_color)
        self.exit_button_image_rect = self.exit_button_image.get_rect()
        self.exit_button_image_rect.centerx = self.screen_rect.centerx
        self.exit_button_image_rect.centery = (self.screen_rect.centery + 100)

        # show the entire button
        self.screen.fill(self.button_color, self.exit_bg_rect)
        self.screen.blit(self.exit_button_image, self.exit_button_image_rect)

    # 帮助按钮
    def hint_button(self, ai_settings, screen, msg):
        # button border
        self.hint_bg_rect = pygame.Rect(0, 0, self.width, self.height)
        self.hint_bg_rect.centerx = self.screen_rect.centerx
        self.hint_bg_rect.centery = self.screen_rect.centery

        # text on button
        self.hint_button_image = self.font.render('Help', True, self.text_color, self.button_color)
        self.hint_button_image_rect = self.hint_button_image.get_rect()
        self.hint_button_image_rect.centerx = self.screen_rect.centerx
        self.hint_button_image_rect.centery = self.screen_rect.centery

        # show the entire button
        self.screen.fill(self.button_color, self.hint_bg_rect)
        self.screen.blit(self.hint_button_image, self.hint_button_image_rect)




