import random

print("Choose you Companion to start your journey")

class Companion:
    def __init__(self, name, element, health, speed, damagemultiplier, defense, moves):
        self.name
        self.element
        self.health
        self.speed
        self.damage_multiplier
        self.defense
        self.moves

class Moves:
    def __init__(self, name, element, damage):
        self.name   
        self.element
        self.damage

tackle = Moves("Tackle", "Normal", damage= 20)

ember = Moves("Ember", "Fire", damage= 30)

water_gun = Moves("Water Gun", "Water", damage= 30)

vine_whip = Moves("Vine Whip", "Plant", damage= 30)


def show_stats(self):
    
    print("{self.name},{self.element},Stats:").format

fire_lizard = Companion("Fire Lizard", "Fire", health=100, speed=30, damagemultiplier=1.1 ,defense= 40, moves= tackle, ember)

water_turtle = Companion("Water Turtle", "Water", health=110, speed=25, damagemultiplier=1.0 ,defense= 45, moves= tackle, water_gun)

plant_frog = Companion("Plant Frog", "Plant", health=120, speed=20, damagemultiplier=0.9 ,defense= 50, moves= tackle, vine_whip)
