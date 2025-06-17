import random

# This class is to define what a Companion needs including their stats and elements
class Companion:
    def __init__(self, name, element, health, speed, damage_multiplier, defense, moves):
        self.name = name
        self.element = element
        self.health = health
        self.speed = speed
        self.damage_multiplier = damage_multiplier
        self.defense = defense
        self.moves = moves


# This class is to define what Moves need including name, element and damage
class Moves:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage


# These lines are to write the stats of the moves variable and orginise it into the Moves class
tackle = Moves("Tackle", "Normal", damage= 20)

ember = Moves("Ember", "Fire", damage= 30)

water_gun = Moves("Water Gun", "Water", damage= 30)

vine_whip = Moves("Vine Whip", "Plant", damage= 30)

quick_attack = Moves("Quick Attack", "Normal", damage= 24)

thunder_shock = Moves("Thunder shock", "Electric", damage= 34)


# These lines arre to write the stats of the moves variable and orginis it into the Chompanion class
fire_lizard = Companion("Fire Lizard", "Fire", health=100, speed=30, damage_multiplier=1.1, defense= 40, moves= [tackle, ember])

water_turtle = Companion("Water Turtle", "Water", health=110, speed=25, damage_multiplier=1.0, defense= 45, moves= [tackle, water_gun])

plant_frog = Companion("Plant Frog", "Plant", health=120, speed=20, damage_multiplier=0.9, defense= 50, moves= [tackle, vine_whip])

electric_mouse = Companion("Electric Mouse", "Electric", health=100, speed=40, damage_multiplier=1.0, defense= 35, moves= [quick_attack, thunder_shock])


# This is the opening question to the game as it gives them the choice of what Companion they want for the rest of their journey
print("\nChoose you Companion to start your journey, you  can only choose one so think wisely")

inventory = input("1. Fire Lizard\n2. Water Turtle\n3. Plant Frog\n").lower()
while inventory not in ["1", "2", "3", "fire lizard", "water turtle", "plant frog", "firelizard", "waterturtle", "plantfrog", "electric mouse", "4", "electricmouse"]
    print("Please choose a valid option" )
    if inventory == "1":