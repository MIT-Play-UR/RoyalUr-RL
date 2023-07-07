# import pygame  # probably used to visualize game
import random

class UrGame:

    def __init__(self):
        # TODO
        self.reset()

    def reset(self):
        # TODO - game state
        self.board = [[]]
        self.score = [0, 0]
        self.turn_count = 0
        self.cur_player = 0

    def roll_dice(self):
        # TODO
        return 0
    
    def play_step(self, action):
        # TODO: fill in sections with dummy variables/functions
        '''
        runs one turn of the game
        - ends game if too many turns have happened without much progress 
          (100 turns per token scored) to prevent infinite loops
        '''
        self.turn_count += 1

        reward = 0
        game_over = False

        if not self.valid_move(action) or self.turn_count > 100 * self.score[self.cur_player]:
            reward = -10
            game_over = True
            return reward, game_over, self.score[self.cur_player]
        
        score_a_point = False
        if score_a_point:
            reward = 10
            self.update_score()

        self.move_piece(action)
        self.cur_player = self.cur_player ^ 1
        return reward, game_over, self.score[self.cur_player]
    

    def update_score(self):
        # TODO
        pass

    def valid_move(self, action):
        # TODO - game state
        return False
    
    def move_piece(self, action):
        # TODO - game state
        pass