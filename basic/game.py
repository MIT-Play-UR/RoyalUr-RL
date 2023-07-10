# import pygame  # probably used to visualize game
import numpy as np
import random

class UrGame:

    rosette = [4, 8, 14]
    shared = list(range(5, 13))

    def __init__(self):
        # TODO
        self.reset()

    def reset(self):
        # TODO - game state
        self.board = list(np.zeros((2, 16)))
        self.board[0][0] = 7
        self.board[1][0] = 7
        self.turn_count = 0
        self.cur_player = 0

    def roll_dice(self):
        # TODO
        return 0
    
    def play_step(self, action):
        # TODO: fill in sections with dummy variables/functions
        '''
        action: a 2 element list describing:
        - the current position of the token to be moved (idx 0 - 14)
        - the direction (+/- 1)
        runs one turn of the game
        - ends game if too many turns have happened without much progress 
          (100 turns per token scored) to prevent infinite loops
        '''
        self.turn_count += 1

        reward = 0
        game_over = False

        cur_pos = action[0]
        new_pos = action[0] + self.cur_roll * action[1]
        cur = self.cur_player
        opp = self.cur_player ^ 1

        if not self.valid_move(new_pos) or self.turn_count > 100 * self.board[cur][15]:  # score is held in 15th cell (dummy end cell)
            reward = -10
            game_over = True
            return reward, game_over, self.board[cur][15]
        
        turn_ends = True

        if new_pos in self.rosette:
            self.move_piece(cur_pos, new_pos, cur)
            turn_ends = False
        elif cur_pos == 0:
            self.move_piece(cur_pos, new_pos, cur, all = False)
        else:
            if self.board[opp][new_pos] and new_pos in self.shared:
                self.move_piece(new_pos, 0, opp)
            self.move_piece(cur_pos, new_pos, cur)

        if self.board[cur][15] == 7:
            reward = 10
            game_over = True
            return reward, game_over, self.board[cur][15]
        
        if turn_ends:
            self.cur_player = opp
        self.cur_roll = self.roll_dice()
        return reward, game_over, self.board[cur][15]
    

    def has_valid_move(self):
        ''' Checks whether a valid move actually exists. '''
        if self.cur_roll == 0:
            return False
        pass

    def valid_move(self, new_pos):
        # check out of bounds
        if new_pos < 1 or new_pos > 16:
            return False
        
        if new_pos in self.rosette:
            opp = self.cur_player ^ 1
            if self.board[opp][new_pos] and new_pos in self.shared:
                return False
        else:
            if self.board[self.cur_player][new_pos] and new_pos != 15:
                return False

        return True
    
    def move_piece(self, cur_pos, new_pos, player, all = True):
        if all:
            count = self.board[player][cur_pos]
        else:
            count = 1
        self.board[player][cur_pos] -= count
        self.board[player][new_pos] += count