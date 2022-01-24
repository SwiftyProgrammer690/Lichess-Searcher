#Copyright @SwaritChoudhari [-:
import lichess.api
from lichess.format import PYCHESS

def findBlitzPlayerRating(a):
  user = lichess.api.user(a)
  print(user['perfs']['blitz']['rating'])
def findRapidPlayerRating(a):
  user = lichess.api.user(a)
  print(user['perfs']['rapid']['rating'])
def findBulletPlayerRating(a):
  user = lichess.api.user(a)
  print(user['perfs']['bullet']['rating'])
def findGame(a):
  game = lichess.api.game(a, format=PYCHESS)
  print(game.end().board())
