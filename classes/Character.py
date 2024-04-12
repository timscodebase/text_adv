from chalky import sty, fg
red_bold = sty.bold & fg.red
red = fg.red
green = fg.green


class Character:
  def __init__(self, name, description, hp, mp, attack, defense, level, is_dead=False):
    self.name = name
    self.description = description
    self.hp = hp
    self.mp = mp
    self.attack = attack
    self.defense = defense
    self.level = level
    self.is_dead = is_dead
    self.max_hp = 100

  def take_damage(self, damage):
    self.hp -= damage
    print(red_bold | f"{self.name} takes {damage} damage.")

  def walk(self):
    print(green | f"{self.name} is walking.")

  def attack(self):
    print(red |f"{self.name} is attacking.")

  def defend(self):
    print(f"{self.name} is defending.")

  def level_up(self):
    print(f"{self.name} is level up.")

  def die(self):
    self.is_dead = True
    print(f"{self.name} is dead.")

  def tell_story(self):
    print(f"{self.description}")

  