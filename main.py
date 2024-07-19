import random
class Character:
    def __init__(self, name, health, energy, experience, level):
        self.name=name

class Python_hero(Character):
    experience=0
    level=1
    health=100
    energy=100
    def hero_attack(self):
        self.energy-=5
        self.experience+=1

class Java_monster(Character):
    experience=10
    level=3
    health=100
    energy=100
    def monster_attack(self):
        self.energy-=10

def gameplay(hero,monster):
    return Python_hero(hero)
    return Java_monster(monster)
    while Python_hero.health>0:
      option=input("Type 1 for attack, type 2 for run")
      if option not in [1,2]:
        raise ValueError("1 for attack, 2 for run only")
      else:
        if option==1:
          block1=randint(1,10)
          if block1 in [3,7]:
            monster.energy-=5
          else:
            hero_attack(hero)
            monster.health-=10
          block2=randint(1,10)
          if block2 in [2,8]:
            hero.energy-=2
          else:
            monster_attack(monster)
            hero.health-=15
          if hero.experience>=5:
            hero.level+=1
            hero.experience-=5
          if hero.health<=20:
            return "Warning!!! Your health is low!"
          elif hero.health<=0:
            return "You died."
            break
          if monster.health<=0:
            return "You win!"
        else:
          return 'Game over'