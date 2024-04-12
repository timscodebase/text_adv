from classes.Character import Character

class Cleric(Character):
  def __init__(self, name):
    super().__init__(name, 'Cleric', hp=10, attack=2, mp=10, defense=15, level=1, is_dead=False)

  def heal(self):
    print(f"{self.name} is healing.")