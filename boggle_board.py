import random

class BoggleBoard:
  
  def __init__(self):
    self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    self.dice_variables = 'abcdefghijklmnop'
    self.dice = {}
    self.dice_result = {}
    self.set_initial_tiles()
  
  def set_initial_tiles(self):
    for letter in self.dice_variables:
      self.dice_result[letter] = '_'

  def new_dice(self):
    for value in self.dice_variables:
      self.dice[value] = ''
      for i in range(6):
        self.dice[value] += random.choice(self.alphabet)
    print(self.dice)

  def shake(self):
    pad = 3
    for value in self.dice:
      self.dice_result[value] = random.choice(self.dice[value])
      if self.dice_result[value] == 'Q':
        self.dice_result[value] = 'Qu'
      while (len(self.dice_result[value]) < 3):
        self.dice_result[value] += ' '

  def __str__(self):
    self.game_board = (f"""
  Python
  {self.dice_result['a']}{self.dice_result['b']}{self.dice_result['c']}{self.dice_result['d']}
  {self.dice_result['e']}{self.dice_result['f']}{self.dice_result['g']}{self.dice_result['h']}
  {self.dice_result['i']}{self.dice_result['j']}{self.dice_result['k']}{self.dice_result['l']}
  {self.dice_result['m']}{self.dice_result['n']}{self.dice_result['o']}{self.dice_result['p']}
  """)
    return self.game_board


game = BoggleBoard()
print(game)
game.new_dice()
game.shake()
print(game)