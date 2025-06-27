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
    def __init__(self, name, element, min_damage, max_damage=None):
        self.name = name
        self.element = element
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.max_damage = max_damage if max_damage is not None else min_damage

    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

# These lines are to write the stats of the moves variable and orginise it into the Moves class
tackle = Moves("Tackle", "Normal", damage=20)
scratch = Moves("Scratch", "Normal", damage=25)
quick_attack = Moves("Quick Attack", "Normal", damage=24)
claw = Moves("Claw",  "Normal", damage=36)
nibble = Moves("Nibble",  "Normal", min_damage=16, max_damage=46)
bite = Moves("Bite",  "Normal", damage=50)

ember = Moves("Ember", "Fire", damage=30)
flame = Moves("Flame", "Fire", damage=42)

water_gun = Moves("Water Gun", "Water", damage=30)

vine_whip = Moves("Vine Whip", "Plant", damage=30)

thunder_shock = Moves("Thunder shock", "Electric", damage=34)


# These lines arre to write the stats of the moves variable and orginis it into the Chompanion class
fire_lizard = Companion("\033[31;1mFire Lizard\033[0m", "\033[31;1mFire\033[0m", health=100, speed=30, damage_multiplier=1.2, defense= 40, moves= [tackle, ember])
fire_chameleon = Companion("\033[31;1mFire Chameleon\033[0m", "\033[31;1mFire\033[0m", health=165, speed=60, damage_multiplier=1.4, defense= 70, moves= [tackle, ember, flame, bite])
water_turtle = Companion("\033[36;1mWater Turtle\033[0m", "\033[36;1mWater\033[0m", health=110, speed=25, damage_multiplier=1.1, defense= 45, moves= [tackle, water_gun])
plant_frog = Companion("\033[32;1mPlant Frog\033[0m", "\033[32;1mPlant\033[0m", health=120, speed=20, damage_multiplier=0.9, defense= 50, moves= [tackle, vine_whip])
electric_mouse = Companion("\033[33;1mElectric Mouse\033[0m", "\033[33;1mElectric\033[0m", health=100, speed=40, damage_multiplier=1.0, defense= 35, moves= [quick_attack, thunder_shock])
rat_rat = Companion("\033[1m31Rat Rat\033[0m", "\033[1Normal\033[0m", health=80, speed=36, damage_multiplier=0.9, defense= 20, moves= [tackle, scratch])
rate_cate = Companion("\033[1m31Rate Cate\033[0m", "\033[1Normal\033[0m", health=154, speed=67, damage_multiplier=1.4, defense= 61, moves= [tackle, scratch, claw, nibble])

companion_inventory = []

meadow_wild = [
    ()
]

# These are the valid choices you can choose 
valid_companion_choices = {
    "1": fire_lizard,
    "2": water_turtle,
    "3": plant_frog,
    "fire lizard": fire_lizard,
    "water turtle": water_turtle,
    "plant frog": plant_frog,
    "firelizard": fire_lizard,
    "waterturtle": water_turtle,
    "plantfrog": plant_frog,
    "electric mouse": electric_mouse,
    "4": electric_mouse,
    "electricmouse": electric_mouse,
}


chosen_companion = None

# This defines the loop so that it loops until you choose a valid option
while chosen_companion is None:
    # This is the opening question to the game as it gives them the choice of what Companion they want for the rest of their journey
    print("\n\nChoose you Companion to start your journey, but you can only choose one so think wisely, what will your choice be?\n")
    user_choice = input("1. \033[31;1mFire Lizard\033[0m\n2. \033[36;1mWater Turtle\033[0m\n3. \033[32;1mPlant Frog\033[0m\n").lower()

    # This defines the user choice in the valid choices and sorts the chosen Companions into the inventory variable
    if user_choice in valid_companion_choices:
        chosen_companion = valid_companion_choices[user_choice]
        companion_inventory.append(chosen_companion)
    
        # These lines define what Companion you chose and gives a print statment depending on which one
        if chosen_companion == fire_lizard:
            print("\nGreat choice! Fire Lizard is a very strong and fast option, but slightly lacks defense and health.\nYou have obtained \033[31;1mFire Lizard\033[0m!")
        elif chosen_companion == water_turtle:
            print("\nGreat choice! Water Turtle is a great all-round option to outmatch your foes and become the victor!\nYou have obtained \033[36;1mWater Turtle\033[0m!")
        elif chosen_companion == plant_frog:
            print("\nGreat choice! Plant Frog has great defense and health, but is a bit slow, so get ready to tank some hits!\nYou have obtained \033[32;1mPlant Frog\033[0m!")
        elif chosen_companion == electric_mouse:
            print("\noh... uhh... I guess I could get you that one...\nYou have obtained \033[33;1mElectric Mouse\033[0m!")



    # If the typed word is not in the previously above valid choices it will loop the opening question and give the heads up to provide a valid option
    else:
        print("\n---------------------------------\nPlease choose a valid option.")

def show_inventory():
    global lobby
    print("\nYour Companion Inventory:")
    for companion in companion_inventory:
        moves_list = ', '.join(move.name for move in companion.moves)
        print(f"-   {companion.name}\033[0m    Element: {companion.element}    HP: {companion.health}    Damage: {companion.damage_multiplier}x    Defense: {companion.defense}    Speed: {companion.speed}    Moves: {moves_list}\n")
    lobby -= 1

def area_info():
    print("\nArea Info:\n- Meadow: Balanced\n- Forest: Trickier enemies\n- Cave: Higher risk, higher reward")

def play():
    print("\nWhere would you like to explore?")

    area_choice = input("Meadow   Forest   Beach   Desert   Cave   Meadow 2   Forest 2   Cave 2\n").lower()
    if area_choice  ["Meadow", "1"]:
            explore = meadow

# Once you have chosen a Companion you will begivn this prompt and taken to the main lobby menu
print("\n ---------------------------------\n\nNow that you have chosen your Companion what would you like to do next?\n")

lobby = 0

while lobby == 0:

    lobby_choice = input("1. \033[1mPlay!\033[0m\n2. \033[1mView Inventory\033[0m\n3. \033[1mArea Info\033[0m\n\n").lower()

    if lobby_choice in ["1", "play"]:
        play()
        lobby += 1
    elif lobby_choice in ["2", "inventory"]:
        show_inventory()
        lobby += 1
    elif lobby_choice in ["3", "area info", "area"]:
        area_info()
        lobby += 1
    else:
        print("Invalid option, try again")


