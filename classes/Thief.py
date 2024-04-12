from classes.Character import Character

class Thief(Character):
  def __init__(self, name):
    super().__init__(name, 'Thief', hp=10, mp=10, attack=5, defense=5, level=1, is_dead=False)

  def steal(self):
    print(f"{self.name} is stealing.")

  