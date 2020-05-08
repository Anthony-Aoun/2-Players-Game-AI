# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain
import argparse

parser = argparse.ArgumentParser(description='Add game type')
parser.add_argument('game', type=str,
                    help='add the game\'s name')
args = parser.parse_args()
game_name = args.game

brain1 = aiarena.ManualBrain()
human_time = 40

ai_time = 200
if game_name == 'checkers':
    brain2 = MinimaxBrain(aiarena.checkers)
    brain2.depth = 5
    game = aiarena.Game(aiarena.checkers, brain1, human_time, brain2, ai_time)
elif game_name == 'connect4':
    brain2 = MinimaxBrain(aiarena.connect4)
    brain2.depth = 5
    game = aiarena.Game(aiarena.connect4, brain1, human_time, brain2, ai_time)
else:
    print("ERROR : invalid game's name")

game.displayLevel = 1
game.start()
print(game.pgn)

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames
