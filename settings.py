import pygame

class Settings():
    # Store all settings for this game

    def __init__(self):
        # Initialize the static settings of the game
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        # location of the cat
        self.cat_speed_factor = 1.5
        self.cats_limit = 2

        # bullet settings
        self.bullet_speed_factor = 0.8
        # self.bullet_width = 3
        # self.bullet_height = 15
        # self.bullet_color = 139, 125, 107
        self.bullet_allowed = 5

        # mouse settings
        self.mouse_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # fleet_direction     1 for right, -1 for left

        # Speed up the game (increase difficulty)
        self.speedup_scale = 1.3
        # increase score based on game level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change as the game progresses'''
        self.cat_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.mouse_speed_factor = 0.3

        # fleet_direction     1 for right, -1 for left
        self.fleet_direction = 1

        # record score
        self.mouse_points = 50


    def increase_speed(self):
        '''Improve speed settings and mouse points'''
        self.cat_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.mouse_speed_factor *=self.speedup_scale

        self.mouse_points = int(self.mouse_points * self.score_scale)
