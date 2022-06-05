import pickle

class GameStats():
    '''Track game statistics'''

    def __init__(self, ai_settings):
        '''Initialize statistics'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # Make the game inactive at the beginning
        self.game_active = False

        # with open('high_score.txt') as file_object:
        #     hs = file_object.read()
        # self.high_score = int(hs)

        # The highest score will not be reset under any circumstances
        self.high_score = 0

    def reset_stats(self):
        '''Initialize statistics that may change during a game run'''
        self.cats_left = self.ai_settings.cats_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        f = open('score.txt', 'wb')
        pickle.dump(str(self.high_score), f, 0)
        f.close()

    def load_high_score(self):
        f = open('score.txt', 'rb')
        try:
            str_high_score = pickle.load(f)
            self.high_score = int(str_high_score)
        except EOFError:
            self.high_score = 0
        finally:
            f.close()
