class Store:
    def __init__(self, name):
        self.name = name
        self.items = [tonic.name, sword.name, elixir.name]
        
    def do_shopping(self):
        print(f"Welcome to {self.name}!")
        print()
        print(f"We have the following items: \n\n{self.items}\n\n Tonic heals 10 HP. Cost: 10 coins. \n Sword increases power by 1. Cost: 20 coins. \n Elixir heals 10 HP and increases power by 1. Cost: 30 coins.\n")
        print("You have %d coins. What would you like to buy?" % hero.coins)
        answer = input().lower()
        if answer == "tonic":
            hero.items.append(answer)
            hero.coins -= tonic.cost
            print("You bought 1 %s for %d coins. \nYou now have %d coins remaining" % (tonic.name, tonic.cost, hero.coins))
            print()
            print(hero.items)
        elif answer == "sword":
            hero.items.append(answer)
            hero.coins -= sword.cost
            print("You bought 1 %s for %d coins. \nYou now have %d coins remaining" % (sword.name, sword.cost, hero.coins))
            print()
            print("There are your current items")
            print(hero.items)
        elif answer == "elixir":
            hero.items.append(answer)
            hero.coins -= elixir.cost
            print("You bought 1 %s for %d coins. \nYou now have %d coins remaining" % (elixir.name, elixir.cost, hero.coins))
            print()
            print("There are your current items.")
            print(hero.items)
            
class Item:
    def __init__(self, name, cost, h_increase, p_increase):
        self.name = name
        self.cost = cost
        self.h_increase = h_increase
        self.p_increase = p_increase
        
    def do_apply(self):
        for self.name in hero.items:
            if self.h_increase > 0 and self.p_increase > 0:
                hero.health += self.h_increase
                hero.power += self.p_increase
                print(f"Your used up 1 {self.name}")
                print(f"Your power increased by {self.p_increase}")
                print(f"Your health increased by {self.h_increase}")
                print()
                hero.items.remove(self.name)
                break
            elif self.h_increase > 0:
                hero.health += self.h_increase
                print(f"Your used up 1 {self.name}")
                print(f"Your health increased by {self.h_increase}")
                print()
                hero.items.remove(self.name)
                break
            elif self.p_increase > 0:
                hero.power += self.p_increase
                print(f"Your used up 1 {self.name}")
                print(f"Your power increased by {self.p_increase}")
                print()
                hero.items.remove(self.name)
                break

            else:
                pass
        else:
            print("You do not have that item")
        
tonic = Item("Tonic", 5, 10, 0)
sword = Item("Sword", 20, 0, 1)
elixir = Item("Elixir", 30, 10, 2)
    
class Character:
    def __init__(self, name, health=20, power=5):
        self.name = name
        self.health = health
        self.power = power
        self.items = []
        
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}.")
        import random
        random_damage = random.randint(1, self.power)
        print("%s does %d damage!" % (self.name, random_damage))
        enemy.health -= random_damage
        print()
        
    def is_alive(self):
        return self.health > 0 
    
class Hero(Character):
    def __init__(self, name, health=30, power=8, cape=True, coins=20):
        super().__init__(name, health, power)
        self.cape = cape
        self.coins = coins
        
    def attack(self, enemy):
        print()
        print(f"{self.name} gets ready to attack {enemy.name}...")
        print()
        import random
        probability_threshold = 0.25
        if random.random() < probability_threshold:
            print(f"{self.name} deals {enemy.name} a MASSIVE blow!")
            import random
            random_damage = (random.randint(4, self.power)) * 2
            print("%s deals %d damange!" % (self.name, random_damage))
            enemy.health -= random_damage
            print()
        else:
            import random
            print(f"{self.name} lands a regular punch on {enemy.name}.")
            random_damage = random.randint(1, self.power)
            print("%s deals %d damage!" % (self.name, random_damage))
            enemy.health -= random_damage
            print()
            
    def purchase(self, item):
        item = name.item
        self.items.append(name.item)
        self.coins =- name.item
        pass 
    
    
class Enemy(Character):
    def __init__(self, name, health, power, coins):
        super().__init__(name, health, power)
        self.coins = coins
        
    def is_dead(self):
        hero.coins += self.coins
        print("%s receives %d coins and has %d total" % (hero.name, self.coins, hero.coins))
        
class Human(Enemy):
    def __init__(self, name, health=60, power=4, coins=10):
        super().__init__(name, health, power, coins)
        
class Spirit(Enemy):
    def __init__(self, name, health=1, power=10, coins=15):
        super().__init__(name, health, power, coins)
            
class Undead(Enemy):
    def __init__(self, name, health=100, power=100, coins=20):
        super().__init__(name, health, power, coins)
       
hero = Hero("Batman")
nemesis = Human("Joker")
shadow = Spirit("Shadow")
zombie = Undead("Zombie")
store = Store("The Place Where You Buy Stuff While Getting Punched in the Face, LLC!")

def play_game():

    while nemesis.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The %s has %d health and %d power." % (nemesis.name, nemesis.health, nemesis.power))
        print()
        print("What do you want to do?")
        print()
        print("1. Fight %s" % nemesis.name)
        print("2. Guard & Heal")
        print("3. Flee")
        print("4. Go Shopping")
        print("5. Use Item")
        print()
        user_input = input()
        if user_input == "1":
            # Hero attacks Joker
            hero.attack(nemesis)
            if nemesis.health <= 0:
                print("The %s is dead." % nemesis.name)
                nemesis.is_dead()
        elif user_input == "2":
            import random
            random_health = random.randint(1, 11)
            hero.health = hero.health + random_health
            print("%s healed %d" % (hero.name, random_health))
            nemesis.attack(hero)
        elif user_input == "3":
            print("Goodbye.")
            break
        elif user_input == "4":
            store.do_shopping()
            
        elif user_input == "5":
            if hero.items == False:
                print("You have no items")
            else:
                print(f"Which of your items would you like to use? \n{hero.items}")
                answer = input().lower()
                if answer == "tonic":
                    tonic.do_apply()
                elif answer == "sword":
                    sword.do_apply()
                elif answer == "elixir":
                    elixir.do_apply()
        else:
            print("Invalid input %r" % user_input)

        if nemesis.is_alive():
            # Joker attacks hero
            nemesis.attack(hero)
            if hero.health <= 0:
                print("You are dead.")
            else:
                import random
                probability_threshold = 0.15
                if random.random() < probability_threshold:
                    print(f"{nemesis.name} takes a healing potion and heals 10 HP.")
                    nemesis.health += 10
                    print()
                else:
                    pass

play_game()

