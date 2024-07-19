import random
class Character:
    def __init__(self, name, health, energy, experience, level):
        self.name=name
        self.health=health
        self.energy=energy
        self.experience=experience
        self.level=level

    def hero_attack(self):
        self.energy-=5
        self.experience+=1

    def monster_attack(self):
        self.energy-=10

    def __repr__(self):
      return f'\nCharacter: {self.name}\nHealth: {self.health}\nEnergy: {self.energy}\nExperience: {self.experience}\nLevel: {self.level}'

hero=Character("Python hero",100,100,0,1)
monster=Character("Java monster",100,100,10,3)

def gameplay(hero,monster):
    print(hero)
    print(monster)
    while hero.health>0:
        option=input("\nType 1 for attack, type 2 for run ")
        if int(option) not in [1,2]:
            raise ValueError("1 for attack, 2 for run only")
        else:
            if int(option)==1:
                print('The hero is attacking the monster')
                block1=random.randint(1,10)
                if int(block1) in [3,7]:
                    monster.energy-=5
                    print("The monster blocked the hero's attack")
                else:
                    Character.hero_attack(hero)
                    monster.health-=10
                    print("The hero successfully landed a hit!")
                block2=random.randint(1,10)
                if int(block2) in [2,8]:
                    hero.energy-=2
                    print("The hero blocked the monster's attack")
                else:
                    Character.monster_attack(monster)
                    hero.health-=15
                    print("The monster attacked the hero")
                if hero.experience>=5:
                    hero.level+=1
                    hero.experience-=5
                    print('Hero leveled up!')
                if hero.health<=20:
                    return "Warning!!! Your health is low!"
                elif hero.health<=0:
                    return "You died."
                    break
                if monster.health<=0:
                    return "You win!"
            else:
                print('Game over')
                break
            print(hero)
            print(monster)
        
if __name__ == "__main__":
  gameplay(hero,monster)
  pass