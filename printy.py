from sys import stdout
from time import sleep

def printy(text, pause=0.05):
  for character in text:
    stdout.write(character)
    stdout.flush()
    sleep(pause)