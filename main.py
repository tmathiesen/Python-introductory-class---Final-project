import random
import time
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
    play=True
    while play is True:
        print(hero)
        time.sleep(2)
        print(monster)
        time.sleep(2)
        while hero.health>0:
            option=input("\nType 1 for attack, type 2 for run: ")
            time.sleep(2)
            if int(option) not in [1,2]:
                raise ValueError("1 for attack, 2 for run only")
            else:
                if int(option)==1:
                    print('The hero is attacking the monster...')
                    time.sleep(2)
                    block1=random.randint(1,10)
                    if int(block1) in [3,7]:
                        monster.energy-=5
                        print("The monster blocked the hero's attack.")
                        time.sleep(2)
                    else:
                        Character.hero_attack(hero)
                        monster.health-=10
                        print("The hero successfully landed a hit!")
                        time.sleep(2)
                    print('The monster is attacking the hero...')
                    time.sleep(2)
                    block2=random.randint(1,10)
                    if int(block2) in [2,5,8]:
                        hero.energy-=2
                        print("The hero blocked the monster's attack")
                        time.sleep(2)
                    else:
                        Character.monster_attack(monster)
                        hero.health-=15
                        print("The monster landed a hit!")
                        time.sleep(2)
                    if hero.experience>=5:
                        hero.level+=1
                        hero.experience-=5
                        hero.health=100
                        hero.energy=100
                        print('Hero leveled up!')
                        time.sleep(2)
                    if hero.health<=20:
                        print("Warning!!! Hero, your health is low!")
                        time.sleep(2)
                    elif hero.health<=0:
                        print("You died.")
                        time.sleep(2)
                        break
                    if monster.health<=0:
                        print("You win!")
                        option=2
                else:
                    option_2=input("Type C to fight another monster, type E to end the game: ")
                    if option_2 not in ["C","E"]:
                        raise ValueError("C for continue, E for exit only")
                    else:
                        if option_2=="E":
                            print('Game over.')
                            play=False
                            time.sleep(2)
                            break
                        if option_2=="C":
                            monster=Character("Java monster",100,100,10,3)
                            break
                print(hero)
                time.sleep(2)
                print(monster)
                time.sleep(2)
        
if __name__ == "__main__":
    gameplay(hero,monster)
    pass