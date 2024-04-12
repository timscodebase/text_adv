import os
from art import *
from Colors import *
from utils import create_character, greet

game_over = False
game_won = False

TITLE = text2art('''
  Welcome to
  Papi's Text
  Adventure!
''')

def quit():
  print('Goodbye!')
  global game_over
  game_over = True

def game_menu(character):
  action = input('Choose your action:\n(W) Walk\n(A) Attack\n(D) Defend\n\n(Q) Quit:\n\n')

  if action == 'w' or action == 'W':
    print('You walk')
  elif action == 'a' or action == 'A':
    print('You attack')
  elif action == 'd' or action == 'D':
    print('You defend')
  elif action == 'q' or action == 'Q':
    quit()

os.system('clear')
print(green | TITLE)

input('Press any key to continue...')

os.system('clear')

my_character = None
character = input(green | 'Choice your character type:\n(A) Wizard\n(B) Warrior\n(C) Cleric\n(D) Thief\n\n')
while character not in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
  character = input(red |'Invalid character type. Please choice your character type:\n(A) Wizard\n(B) Warrior\n(C) Cleric\n(D) Thief\n\n')

if character == 'a' or character == 'A':
  print(green | 'You are a Wizard')
  my_character = create_character('Wizard')
  greet(my_character.name, my_character.description)

elif character == 'b' or character == 'B':
  print(blue | 'You are a Warrior')
  my_character = create_character('Warrior')
  greet(my_character.name, my_character.description)

elif character == 'c' or character == 'C':
  print(pink | 'You are a Cleric')
  my_character = create_character('Cleric') 
  greet(my_character.name, my_character.description)

elif character == 'd' or character == 'D':
  print(teal | 'You are a Thief')
  my_character = create_character('Thief')
  greet(my_character.name, my_character.description)

else:
  print(red | 'Invalid character type')

while not game_over and not game_won:
  game_menu(my_character)