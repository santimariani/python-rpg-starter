class Character:
    def __init__(self, name, health=10, power=5):
        self.name = name
        self.health = health
        self.power = power
        self.weapons = []
        
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        import random
        random_damage = random.randint(1, self.power)
        print("%s does %d!" % (self.name, random_damage))
        enemy.health -= random_damage
        
    def is_alive(self):
        return self.health > 0 
    
class Hero(Character):
    def __init__(self, name, health, power, cape):
        super().__init__(name, health, power)
        self.cape = cape

class Villain(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health,power)


hero = Hero("Batman", 20, 8, True)
villain = Villain("Joker", 40, 4)

def play_game():

    while villain.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The %s has %d health and %d power." % (villain.name, villain.health, villain.power))
        print()
        print("What do you want to do?")
        print("1. Fight %s" % villain.name)
        print("2. Guard & Heal")
        print("3. Flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks Joker
            hero.attack(villain)
            if villain.is_alive == False:
                print("The {villain.name} is dead.")
        elif user_input == "2":
            import random
            random_health = random.randint(1, 10)
            hero.health = hero.health + random_health
            print("%s healed %d" % (hero.name, random_health))
            villain.attack(hero)
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if villain.is_alive():
            # Joker attacks hero
            villain.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

play_game()

