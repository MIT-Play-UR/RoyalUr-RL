import torch
import random
from collections import deque
import numpy as np
from game import UrGame
from model import Linear_QNet, QTrainer

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.game_count = 0
        self.epsilon = 0  # controls randomness
        self.gamma = 0.5  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(None, None, None)  # TODO
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)



    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, game_over):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, game_over):
        pass

    def get_action(self, state):
        pass

def train(game_limit = 1000):
    scores = []
    mean_scores = []
    total_score = 0
    best_score = 0
    agent = Agent()
    game = UrGame()
    while agent.game_count < game_limit:
        cur_state = agent.get_state(game)

        final_move = agent.get_action(cur_state)

        reward, game_over, score = game.play_step(final_move)
        new_state = agent.get_state(game)

        agent.train_short_memory(cur_state, final_move, reward, new_state, game_over)
        agent.remember(cur_state, final_move, reward, new_state, game_over)

        if game_over:
            # experience replay
            game.reset()
            agent.game_count += 1
            agent.train_long_memory()
            
            if score > best_score:
                best_score = score
                agent.model.save()

            print('Game', agent.game_count, 'Score', score, 'Record:', best_score)
            # TODO: plot


if __name__ == '__main__':
    train()