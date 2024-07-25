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
        """Attack function for the hero. If he runs out of energy, he will struggle his way to win!"""
        if self.energy>=5:
            self.energy-=5
        else:
            self.health-=8
            print("The hero ran out of energy. The hero is using his body to attack.")
            time.sleep(2)
        self.experience+=1


    def monster_attack(self):
        """Attack function for the monster. If it runs out of energy, it can grapple."""
        if self.energy>=10:
            self.energy-=10
        else:
            self.health-=12
            print("The monster ran out of energy. The monster is using its body to attack.")
            time.sleep(2)

    def __repr__(self):
      return f'\nCharacter: {self.name}\nHealth: {self.health}\nEnergy: {self.energy}\nExperience: {self.experience}\nLevel: {self.level}'

hero=Character("Python hero",100,100,0,1)
monster=Character("Java monster",100,100,10,3)

def gameplay(hero,monster):
    """Basic game fight between a hero and a monster."""
    print(hero)
    time.sleep(2)
    print(monster)
    time.sleep(2)
    while hero.health>0:
        while monster.health>0:
            if monster.health==10 or monster.energy==10:
                print("\nThe monster has escaped.")
                break
            elif monster.health<=0:
                print("\nYou win.")
                break
            else:
                option=input("\nType 1 for attack, type 2 for run: ")
                time.sleep(2)
                if int(option) not in [1,2]:
                    raise ValueError("1 for attack, 2 for run only.")
                else:
                    if int(option)==1:
                        print('The hero is attacking the monster...')
                        time.sleep(2)
                        block1=random.randint(1,10)
                        if int(block1) in [3,5,8]:
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
                        if int(block2) in [1,6,10]:
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
                            print("Hero's health and energy have been restored.")
                            time.sleep(2)
                        if hero.health<=20:
                            print("Warning!!! Hero, your health is low!")
                            time.sleep(2)
                        print(hero)
                        time.sleep(2)
                        print(monster)
                        time.sleep(2)
                    else:
                        print("The hero has fled.")
                        break
        option_2=input("\nType C to fight another monster, type E to end the game: ")
        if option_2.upper() not in ["C","E"]:
            raise ValueError("C for continue, E for exit only")
        else:
            if option_2.upper()=="E":
                print('\nGame over.')
                break
            if option_2.upper()=="C":
                monster=Character("Java monster",100,100,10,3)
                print(hero)
                time.sleep(2)
                print(monster)
                time.sleep(2)
        
if __name__ == "__main__":
    gameplay(hero,monster)
    pass