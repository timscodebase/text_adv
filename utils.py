from classes.Thief import Thief
from classes.Cleric import Cleric
from classes.Warrior import Warrior
from classes.Wizard import Wizard

import pprint

pp = pprint.PrettyPrinter(width=40, compact=True)

def create_character(type):
  name = input('Name your character: ')

  if type == 'Wizard':
    return Wizard(name)
  elif type == 'Warrior':
    return Warrior(name)
  elif type == 'Cleric':
    return Thief(name)
  elif type == 'Thief':
    return Cleric(name)
  
def cleric_story(name):
  pp.pprint('In the serene temples of the divine city of Luminaria, there walks a figure whose presence brings solace to the weary and hope to the downtrodden - Sister ' + name + ' Lightsworn.\nBorn into the priesthood of the radiant goddess Seraphia, ' + name + '\'s path was set from the moment she uttered her first prayer. Raised within the sacred walls of the temple, she learned the teachings of her goddess, her faith unwavering even in the face of adversity.\nFrom a young age, ' + name + ' displayed a gift for healing, her hands blessed with the divine touch of Seraphia herself. With each passing year, she delved deeper into the mysteries of her faith, her devotion burning brighter with every revelation.\nBut ' + name + '\'s calling extended beyond the confines of the temple walls. With a heart filled with compassion and a spirit as pure as the morning dew, she ventured out into the world, seeking to spread the light of Seraphia to those in need.\nArmed with her faith and her sacred rites, ' + name + ' traveled to the farthest corners of the realm, offering aid to the sick and comfort to the afflicted. Wherever she went, miracles followed in her wake, her presence a beacon of hope in a world shrouded in darkness.\nYet, for all her divine gifts, ' + name + ' knew that true strength lay not in the power of miracles, but in the kindness of the heart. With each act of compassion, she forged bonds of friendship and c' + name + 'derie that transcended the boundaries of race and creed.\nNow, as the world teeters on the brink of chaos, Sister ' + name + ' Lightsworn stands as a bastion of hope in the face of despair. With each prayer she offers and each hand she extends in friendship, she reaffirms her commitment to the teachings of Seraphia, her faith unshakable even in the darkest of times. And though the road ahead may be fraught with trials and tribulations, ' + name + ' knows that as long as she remains true to her calling, the light of Seraphia will guide her through the darkest of nights.')
  
def thief_story(name):
  print('In the labyrinthine streets of the bustling city of Duskwood, there exists a figure who moves with the grace of a shadow and the cunning of a fox - ' + name + ' Nightshade.\nBorn into poverty in the slums of Duskwood, ' + name + ' learned from an early age that survival often depended on one\'s ability to outwit and outmaneuver those who sought to exploit the weak. With no family to call her own, she forged her path through the city\'s underbelly, honing her skills as a thief and a rogue.\n' + name + '\'s nimble fingers and quick wit soon caught the attention of the city\'s underworld kingpins, who recognized her potential as a valuable asset. Under their tutelage, she learned the art of stealth and subterfuge, mastering the delicate balance between shadows and light.\nBut ' + name + ' was never content to remain a pawn in someone else\'s game. With each heist she pulled off, she grew bolder, her ambitions reaching ever greater heights. With a network of contacts and informants at her disposal, she navigated the treacherous politics of Duskwood\'s criminal underworld, always staying one step ahead of her rivals.\nYet, for all her skill and cunning, ' + name + ' harbored a secret longing for something more - a chance to break free from the shackles of her past and carve out a new destiny for herself. With each daring theft, she inched closer to that elusive dream, her heart ablaze with the promise of a future filled with riches and adventure.\nNow, as the moon casts its silvery light over the rooftops of Duskwood, ' + name + ' Nightshade emerges from the shadows once more, her eyes gleaming with determination. With each daring heist she undertakes, she inches closer to her ultimate goal, her name whispered in hushed tones by those who dare to dream of a life beyond the confines of the city\'s walls. And though the path she walks may be fraught with danger and betrayal, ' + name + ' knows that as long as she remains true to herself, the world will be hers for the taking.')
  
def warrior_story(name):
  print('In the realm of Thaloria, there exists a warrior whose name strikes fear into the hearts of even the most hardened adversaries - ' + name + ' Shadowthorn, the Darkblade.\nBorn under a crescent moon in the ancient city of Eldorath, ' + name + ' was destined for greatness from the moment she drew her first breath. Raised in the shadow of the city\'s towering citadel, she was imbued with a sense of purpose that set her apart from her peers.\nFrom a young age, ' + name + ' showed an aptitude for combat that bordered on the uncanny. Her movements were fluid, her strikes precise, as if guided by some unseen force. Under the guidance of the city\'s most skilled warriors, she mastered the art of war, her skill with blade and bow unmatched by any who dared to challenge her.\nBut ' + name + '\'s journey was not without its trials. In her quest for mastery, she delved deep into the forbidden arts of shadow magic, seeking power beyond that of mere mortals. Though the darkness threatened to consume her, she emerged from its grasp with a newfound understanding of her abilities, her resolve stronger than ever before.\nArmed with her newfound powers, ' + name + ', known as the Darkblade, embarked on a quest to carve out her own destiny in the world of Thaloria. Her travels took her to the farthest reaches of the kingdom, where she faced enemies both human and monstrous with equal ferocity. Along the way, she forged alliances with beings of great power, their influence shaping the course of her journey.\nYet, for all her prowess in battle, ' + name + ' bore the weight of a dark secret that threatened to unravel her at every turn. Haunted by visions of a future steeped in bloodshed and chaos, she struggled to reconcile her thirst for power with her sense of morality.\nNow, as the shadows gather and darkness looms on the horizon, ' + name + ' Shadowthorn, the Darkblade, stands as a figure of both awe and dread. With each step she takes, she inches closer to her ultimate destiny, her path shrouded in mystery and uncertainty. And though the road ahead may be fraught with peril, ' + name + ' knows that as long as she wields the power of the shadows, she will never falter in her quest for supremacy.')

def wizard_story(name):
  print('\nIn the rugged lands of Eldoria, ' + name + ' Stormblade was born under a blood-red moon, a harbinger of his destiny as a warrior. Raised in the small village of Arkanvale, nestled among the towering peaks of the Frostspire Mountains, ' + name + ' grew up amid tales of valor and adventure spun by the village elders.\nFrom a young age, ' + name + ' displayed an innate talent for combat, honing his skills with sword and shield under the tutelage of the village\'s veteran warriors. But it was not just his prowess in battle that set him apart; it was his unwavering sense of justice and compassion that endeared him to his fellow villagers.\nAs he matured, ' + name + ' embarked on a quest to seek out the truths of the world beyond the boundaries of Arkanvale. His travels took him to far-flung corners of the kingdom, where he faced trials that tested his strength, courage, and resolve. Along the way, he forged bonds with allies who shared his vision of a world free from tyranny and oppression.\nYet, amidst the triumphs and victories, ' + name + ' also tasted the bitter sting of loss. In a fateful encounter with a dark sorcerer, he suffered a grievous wound that left him scarred, both physically and emotionally. But from the depths of despair, ' + name + ' emerged stronger, his determination to vanquish evil burning brighter than ever before.\nNow, as a seasoned warrior, ' + name + ' Stormblade returns to Arkanvale not as a mere villager, but as a beacon of hope for those who dwell within its walls. With each passing day, he stands ready to face the challenges that lie ahead, guided by the principles of honor, courage, and duty. And though the path before him may be fraught with peril, ' + name + ' knows that as long as he draws breath, he will continue to fight for justice and righteousness, a true champion of the realm.')
  return
  
def greet(name, type):
  if type == 'Wizard':
    print(wizard_story(name))
  elif type == 'Warrior':
    print(warrior_story(name))
  elif type == 'Cleric':
    print(cleric_story(name))
  elif type == 'Thief':
    print(thief_story(name))
  print('\n\nGood luck on your adventure!')