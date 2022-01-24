#Copyright @SwaritChoudhari [-:

#Importing Stuff
import lichess.api
from lichess.format import PYCHESS
import printy
from printy import printy

#Important functions
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

#Introduction
printy("Hello!\n")
printy("Welcome to my lichess searcher!\n")
printy("You can either search someones lichess ratings (only support rapid, blitz, and bullet)\n")
printy("Or you can view a game (only support rapid, blitz, and bullet)\n")
printy("Make sure whatever input you give is valid!\n")
printy("1 for search rating or 2 for view game!\n")

#Main Input
usrInput = input("")

#What to do with the main input
if usrInput == "1":
  printy("Who would you like to search?\n")
  usr = input("")
  printy("What time control?\n")
  control = input("")
  if control == "blitz" or "Blitz":
    findBlitzPlayerRating(usr)
  elif control == "bullet" or "Bullet":
    findBulletPlayerRating(usr)
  elif control == "rapid" or "Rapid":
    findRapidPlayerRating(usr)
  else:
    printy("Run the program again, you typed a invalid command!")
elif usrInput == "2":
  printy("What is the game code? Remember, the game code is the code after the slash! -> (https://lichess.org/bv2gEbpr) in that case, bv2gEbpr would be the code! Make sure it is valid!")
  code = input("")
  findGame(code)