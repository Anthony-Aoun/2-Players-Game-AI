# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.random_vs_random
import aiarena
from ..randomBrain import RandomBrain

brain1 = RandomBrain()
brain2 = RandomBrain()
timeLimit = 40 # each player will have 10 seconds to play
game = aiarena.Game(aiarena.checkers, brain1, timeLimit, brain2, timeLimit)
game.start()
print(game.pgn)


