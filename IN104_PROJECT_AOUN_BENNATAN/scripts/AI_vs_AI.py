import aiarena
from ..minimaxTimeBrain import MinimaxBrain

import aiarena
from ..minimaxTimeBrain import MinimaxBrain
import argparse

parser = argparse.ArgumentParser(description='Add game type')
parser.add_argument('game', type=str,
                    help='add the game\'s name')
args = parser.parse_args()
game_name = args.game

ai_time = 0.55
if game_name == 'checkers':
    brain = MinimaxBrain(aiarena.checkers)
    brain.depth = 12
    game = aiarena.Game(aiarena.checkers, brain, ai_time, brain, ai_time)
elif game_name == 'connect4':
    brain = MinimaxBrain(aiarena.connect4)
    brain.depth = 12
    game = aiarena.Game(aiarena.connect4, brain, ai_time, brain, ai_time)
else:
    print("ERROR : invalid game's name")

game.displayLevel = 1
game.start()
print(game.pgn)