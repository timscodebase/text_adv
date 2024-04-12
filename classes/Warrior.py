from classes.Character import Character

class Warrior(Character):
  def __init__(self, name):
    super().__init__(name, "Warrior", hp=10, mp=5, attack=15, defense=10, level=1, is_dead=False)

  def jab(self):
    print(f"{self.name} is jabbing.")