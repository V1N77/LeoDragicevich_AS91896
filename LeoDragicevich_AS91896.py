import random

# I can use this ID to edit the text colour in RGB for a more advanced colour metric by putting it in formula
def color_text_rgb(text, r, g, b):
    return f"\033[1m\033[38;2;{r};{g};{b}m{text}\033[0m"

# This class is to define what a Companion needs, including their stats and elements
class Companion:
    def __init__(self, name, element, health, speed, damage_multiplier, defense, moves):
        self.name = name
        self.element = element
        self.health = health
        self.speed = speed
        self.damage_multiplier = damage_multiplier
        self.defense = defense
        self.moves = moves


# This class is to define what Moves need, including name, element and damage
class Moves:
    def __init__(self, name, element, min_damage, max_damage=None):
        self.name = name
        self.element = element
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.max_damage = max_damage if max_damage is not None else min_damage

    # This line randomises the damage output inbetween max and min damage
    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

# These lines are to write the stats of the moves

# None Element moves
tackle = Moves("Tackle", color_text_rgb("None", 205, 205, 205), min_damage=20, max_damage=20)
peck = Moves("Peck", color_text_rgb("None", 205, 205, 205), min_damage=24, max_damage=24)
scratch = Moves("Scratch", color_text_rgb("None", 205, 205, 205), min_damage=25, max_damage=25)
quick_attack = Moves("Quick Attack", color_text_rgb("None", 205, 205, 205), min_damage=24, max_damage=24)
claw = Moves("Claw", color_text_rgb("None", 205, 205, 205), min_damage=36, max_damage=36)
snap = Moves("Snap", color_text_rgb("None", 205, 205, 205), min_damage=37, max_damage=37)
nibble = Moves("Nibble", color_text_rgb("None", 205, 205, 205), min_damage=16, max_damage=48)
bite = Moves("Bite", color_text_rgb("None", 205, 205, 205), min_damage=40, max_damage=40)
quick_claw = Moves("Quick Claw", color_text_rgb("None", 205, 205, 205), min_damage=48, max_damage=48)
chomp = Moves("Chomp", color_text_rgb("None", 205, 205, 205), min_damage=60, max_damage=60)
gulp = Moves("Gulp", color_text_rgb("None", 205, 205, 205), min_damage=63, max_damage=63)
instant_strike = Moves("Instant Strike", color_text_rgb("None", 205, 205, 205), min_damage=71, max_damage=71)

# Fire Element moves
ember = Moves("Ember", color_text_rgb("Fire", 255, 0, 0), min_damage=30, max_damage=30)
flame = Moves("Flame", color_text_rgb("Fire", 255, 0, 0), min_damage=23, max_damage=52)
fire_ball = Moves("Fire Ball", color_text_rgb("Fire", 255, 0, 0), min_damage=88, max_damage=88)
fire_storm = Moves("Fire Storm", color_text_rgb("Fire", 255, 0, 0), min_damage=46, max_damage=129)

# Water Element moves
water_gun = Moves("Water Gun", color_text_rgb("Water", 0, 188, 255), min_damage=30, max_damage=30)
splash = Moves("Splash", color_text_rgb("Water", 0, 188, 255), min_damage=23, max_damage=52)
pressure_wash = Moves("Pressure Wash", color_text_rgb("Water", 0, 188, 255), min_damage=81, max_damage=81)
tsunami = Moves("Tsunami", color_text_rgb("Water", 0, 188, 255), min_damage=42, max_damage=119)

# Plant Element moves
petal_cut = Moves("Petal Cut", color_text_rgb("Plant", 50, 255, 0), min_damage=18, max_damage=18)
petal_pinch = Moves("Petal Pinch", color_text_rgb("Plant", 50, 255, 0), min_damage=8, max_damage=27)
vine_whip = Moves("Vine Whip", color_text_rgb("Plant", 50, 255, 0), min_damage=30, max_damage=30)
pine_punch = Moves("Pine Punch", color_text_rgb("Plant", 50, 255, 0), min_damage=33, max_damage=33)
thorn_barrage = Moves("Thorn Barrage", color_text_rgb("Plant", 50, 255, 0), min_damage=23, max_damage=52)
flower_power = Moves("Flower Power", color_text_rgb("Plant", 50, 255, 0), min_damage=50, max_damage=50)
plant_pounding = Moves("Plant Pounding", color_text_rgb("Plant", 50, 255, 0), min_damage=25, max_damage=75)
tree_smash = Moves("Tree Smash", color_text_rgb("Plant", 50, 255, 0), min_damage=62, max_damage=62)
leaf_storm = Moves("Leaf Storm", color_text_rgb("Plant", 50, 255, 0), min_damage=32, max_damage=109)

# Electric Element moves
thunder_shock = Moves("Thunder shock", color_text_rgb("Electric", 255, 255, 0), min_damage=34, max_damage=34)
lightning_punch = Moves("Lightning Punch", color_text_rgb("Electric", 255, 255, 0), min_damage=52, max_damage=52)
thunder_bolt = Moves("Thunder Bolt", color_text_rgb("Electric", 255, 255, 0), min_damage=34, max_damage=78)
lightning_charge = Moves("Lightning Charge", color_text_rgb("Electric", 255, 255, 0), min_damage=97, max_damage=97)
thunder_storm = Moves("Thunder Storm", color_text_rgb("Electric", 255, 255, 0), min_damage=77, max_damage=117)

# Enraged Element moves
head_smash = Moves("Head Smash", color_text_rgb("Enraged", 229, 70, 81), min_damage=60, max_damage=60)
charge = Moves("Charge", color_text_rgb("Enraged", 229, 70, 81), min_damage=80, max_damage=80)
stomp = Moves("Stomp", color_text_rgb("Enraged", 229, 70, 81), min_damage=84, max_damage=84)

# Wind Element moves
wing_push = Moves("wing_push", "Wind", min_damage=28, max_damage=28)
breeze = Moves("Breeze", "Wind", min_damage=30, max_damage=30)
feather_storm = Moves("Feather Storm", "Wind", min_damage=14, max_damage=53)
wing_slash = Moves("Wing Slash", "Wind", min_damage=76, max_damage=76)
dust_devil = Moves("Dust Devil", "Wind", min_damage=38, max_damage=78)
gust = Moves("Gust", "Wind", min_damage=80, max_damage=80)
windy_day = Moves("Windy Day", "Wind", min_damage=54, max_damage=92)
tornadoe = Moves("Tornadoe", "Wind", min_damage=82, max_damage=119)
cyclone = Moves("Cyclone", "Wind", min_damage=63, max_damage=182)

# Armoured Element moves
shell_ram = Moves("Shell Spin", color_text_rgb("Armoured", 70, 124, 90), min_damage=80, max_damage=80)
roll_ram = Moves("Roll Ram", color_text_rgb("Armoured", 70, 124, 90), min_damage=84, max_damage=84)

# Spirit Element moves
scare = Moves("Scare", color_text_rgb("Spirit", 137, 0, 255), min_damage=24, max_damage=53)
tongue_strike = Moves("Tongue Strike", color_text_rgb("Spirit", 137, 0, 255), min_damage=62, max_damage=62)

# Toxic Element moves
foul_stench = Moves("Foul Stench", color_text_rgb("Toxic", 134, 0, 120), min_damage=24, max_damage=24)
toxic_touch = Moves("Toxic Touch", color_text_rgb("Toxic", 134, 0, 120), min_damage=30, max_damage=30)
spore_cloud = Moves("Spore Cloud", color_text_rgb("Toxic", 134, 0, 120), min_damage=1, max_damage=51)
venom_claw = Moves("Venom Claw", color_text_rgb("Toxic", 134, 0, 120), min_damage=58, max_damage=58)
poison_spores = Moves("Poison Spores", color_text_rgb("Toxic", 134, 0, 120), min_damage=2, max_damage=93)
toxic_spores = Moves("Toxic Spores", color_text_rgb("Toxic", 134, 0, 120), min_damage=4, max_damage=169)
spore_storm = Moves("Spore Storm", color_text_rgb("Toxic", 134, 0, 120), min_damage=6, max_damage=282)

# Rock Element moves
pebble_punch = Moves("Pebble Punch", color_text_rgb("Rock", 141, 138, 131), min_damage=20, max_damage=20)
mud_slap = Moves("Mud Slap", color_text_rgb("Rock", 141, 138, 131), min_damage=36, max_damage=36)
stone_edge = Moves("Stone Edge", color_text_rgb("Rock", 141, 138, 131), min_damage=44, max_damage=44)
rock_toss = Moves("Rock Toss", color_text_rgb("Rock", 141, 138, 131), min_damage=0, max_damage=50)
iron_tail = Moves("Iron Tail", color_text_rgb("Rock", 141, 138, 131), min_damage=54, max_damage=54)
metal_chomp = Moves("Metal Chomp", color_text_rgb("Rock", 141, 138, 131), min_damage=72, max_damage=72)
rock_barrage = Moves("Rock Barrage", color_text_rgb("Rock", 141, 138, 131), min_damage=44, max_damage=78)
rock_slide = Moves("Rock Slide", color_text_rgb("Rock", 141, 138, 131), min_damage=60, max_damage=84)
cementation = Moves("Cementation", color_text_rgb("Rock", 141, 138, 131), min_damage=101, max_damage=101)

# These lines arre to write the stats of the moves variable and orginis it into the Chompanion class

rat_rat = Companion(color_text_rgb("Rat Rat", 192, 176, 201), color_text_rgb(color_text_rgb("None", 205, 205, 205), 205, 205, 205), health=80, speed=32, damage_multiplier=0.9, defense= 35, moves= [tackle, scratch])
rate_cate = Companion(color_text_rgb("Rate Cate", 220, 208, 178), color_text_rgb(color_text_rgb("None", 205, 205, 205), 205, 205, 205), health=154, speed=67, damage_multiplier=1.4, defense= 61, moves= [tackle, scratch, claw, nibble])

rib_rab = Companion(color_text_rgb("Rib Rab", 220, 211, 190), color_text_rgb(color_text_rgb("None", 205, 205, 205), 205, 205, 205), health=74, speed=36, damage_multiplier=0.8, defense= 28, moves= [nibble])
riba_ruba = Companion(color_text_rgb("Riba Ruba", 206, 196, 171), color_text_rgb(color_text_rgb("None", 205, 205, 205), 205, 205, 205), health=84, speed=46, damage_multiplier=0.9, defense= 38, moves= [claw, nibble])
rabta_rubast = Companion(color_text_rgb("Rabta Rubast", 199, 106, 125), color_text_rgb(color_text_rgb("Enraged", 229, 70, 81), 229, 70, 81), health=210, speed=101, damage_multiplier=2.3, defense= 90, moves= [chomp, charge, stomp])

sqanib = Companion(color_text_rgb("Sqanib", 165, 196, 215), color_text_rgb(color_text_rgb("None", 205, 205, 205), 205, 205, 205), health=64, speed=44, damage_multiplier=1.1, defense= 22, moves= [peck, wing_push, feather_storm])
sqornatib = Companion(color_text_rgb("Sqornatib", 123, 139, 168), color_text_rgb(color_text_rgb("Wind", 205, 205, 205), 205, 205, 205), health=98, speed=82, damage_multiplier=1.5, defense= 39, moves= [wing_slash, windy_day, gulp, charge])

fire_lizard = Companion(color_text_rgb("Fire Lizard", 255, 0, 0), color_text_rgb("Fire", 255, 0, 0), health=100, speed=30, damage_multiplier=1.2, defense= 40, moves= [tackle, ember])
fire_chameleon = Companion(color_text_rgb("Fire Chameleon", 255, 94, 0), color_text_rgb("Fire", 255, 0, 0), health=165, speed=60, damage_multiplier=1.4, defense= 70, moves= [bite, ember, flame])
fire_dragon = Companion(color_text_rgb("Fire Dragon", 255, 145, 0), color_text_rgb("Fire", 255, 0, 0), health=250, speed=100, damage_multiplier=2, defense= 110, moves= [chomp, fire_ball, fire_storm, charge, wing_slash ])

water_turtle = Companion(color_text_rgb("Water Turtle", 0, 188, 255), color_text_rgb("Water", 0, 188, 255), health=110, speed=25, damage_multiplier=1.1, defense= 45, moves= [tackle, water_gun])
water_tortoise = Companion(color_text_rgb("Water Tortoise", 0, 78, 255), color_text_rgb("Water", 0, 188, 255), health=180, speed=50, damage_multiplier=1.3, defense= 80, moves= [snap, water_gun, splash])
water_galapagos = Companion(color_text_rgb("Water Galapagos", 0, 0, 255), color_text_rgb("Water", 0, 188, 255), health=310, speed=79, damage_multiplier=1.6, defense= 145, moves= [chomp, pressure_wash, tsunami, shell_ram, stomp])

plant_frog = Companion(color_text_rgb("Plant Frog", 50, 255, 0), color_text_rgb("Plant", 50, 255, 0), health=120, speed=20, damage_multiplier=0.9, defense= 50, moves= [tackle, vine_whip])
plant_toad = Companion(color_text_rgb("Plant Toad", 46, 228, 0), color_text_rgb("Plant", 50, 255, 0), health=210, speed=35, damage_multiplier=1.1, defense= 100, moves= [snap, vine_whip, thorn_barrage])
plant_goliath = Companion(color_text_rgb("Plant Goliath", 33, 166, 0), color_text_rgb("Plant", 50, 255, 0), health=365, speed=45, damage_multiplier=1.4, defense= 185, moves= [gulp, tree_smash, leaf_storm, tongue_strike, spore_storm])

loofwis = Companion(color_text_rgb("Loofwis", 167, 209, 112), color_text_rgb("Plant", 50, 255, 0), health=140, speed=38, damage_multiplier=1, defense=19, moves= [thorn_barrage, breeze])
maloofo = Companion(color_text_rgb("Maloofo", 108, 146, 57), color_text_rgb("Plant", 50, 255, 0), health=180, speed=62, damage_multiplier=1.1, defense=79, moves= [plant_pounding, breeze, dust_devil])

blossma = Companion(color_text_rgb("Blossma", 171, 255, 0), color_text_rgb("Plant", 50, 255, 0), health=71, speed=21, damage_multiplier=0.6, defense= 20, moves= [petal_cut, petal_pinch])
blossume = Companion(color_text_rgb("Blossume", 137, 205, 0), color_text_rgb("Plant", 50, 255, 0), health=102, speed=48, damage_multiplier=0.9, defense= 42, moves= [pine_punch, thorn_barrage, poison_spores])
blossertama = Companion(color_text_rgb("Blossertama", 98, 146, 0), color_text_rgb("Plant", 50, 255, 0), health=172, speed=61, damage_multiplier=1.1, defense= 52, moves= [flower_power, plant_pounding, toxic_spores])

mosspre = Companion(color_text_rgb("Mosspre", 0, 182, 18), color_text_rgb("Plant", 50, 255, 0), health=85, speed=20, damage_multiplier=0.8, defense= 48, moves= [vine_whip, spore_cloud])

toforrast = Companion(color_text_rgb("Toforrast", 32, 223, 96), color_text_rgb("Plant", 50, 255, 0), health=140, speed=28, damage_multiplier=0.8, defense= 12, moves= [vine_whip, thorn_barrage, bite])
fotorasta = Companion(color_text_rgb("Fotorasta", 52, 185, 97), color_text_rgb("Plant", 50, 255, 0), health=230, speed=58, damage_multiplier=1.2, defense= 48, moves= [flower_power, plant_pounding, head_smash, iron_tail])
tofarstaffar = Companion(color_text_rgb("Toferstaffer", 27, 137, 64), color_text_rgb("Plant", 50, 255, 0), health=380, speed=80, damage_multiplier=1.6, defense= 78, moves= [gulp, tree_smash, leaf_storm, stomp, rock_slide])

foongar = Companion(color_text_rgb("Foongar", 216, 255, 156), color_text_rgb("Plant", 50, 255, 0), health=92, speed=28, damage_multiplier=1, defense= 54, moves= [toxic_touch, poison_spores])
shroomgart = Companion(color_text_rgb("Shroomgart", 174, 73, 163), color_text_rgb(color_text_rgb("Toxic", 134, 0, 120), 134, 0, 120), health=142, speed=39, damage_multiplier=1.2, defense= 81, moves= [venom_claw, toxic_spores])

stumptas = Companion(color_text_rgb("Stumptas", 56, 75, 4), color_text_rgb("Plant", 50, 255, 0), health=50, speed=5, damage_multiplier=0.3, defense= 400, moves= [tree_smash, roll_ram, leaf_storm])
tasmandoo = Companion(color_text_rgb("Tasmandoo", 173, 125, 209), color_text_rgb("Spirit", 137, 0, 255), health=220, speed=80, damage_multiplier=1.9, defense= 100, moves= [])

roglis = Companion(color_text_rgb("Roglis", 83, 114, 70), color_text_rgb("Rock", 141, 138, 131), health=102, speed=19, damage_multiplier=0.7, defense= 83, moves= [pebble_punch, rock_toss, vine_whip])
rogilons = Companion(color_text_rgb("Rogilons", 42, 68, 31), color_text_rgb("Rock", 141, 138, 131), health=203, speed=32, damage_multiplier=1, defense= 112, moves= [stone_edge, rock_barrage, roll_ram, flower_power])

electric_mouse = Companion(color_text_rgb("Electric Mouse", 255, 255, 0), color_text_rgb("Electric", 255, 255, 0), health=100, speed=42, damage_multiplier=1.0, defense= 35, moves= [quick_attack, thunder_shock])
electric_rat = Companion(color_text_rgb("Electric Rat", 255, 205, 0), color_text_rgb("Electric", 255, 255, 0), health=150, speed=82, damage_multiplier=1.3, defense= 60, moves= [quick_claw, lightning_punch, thunder_bolt, iron_tail])
electric_capybara = Companion(color_text_rgb("Electric Capybara", 243, 182, 0), color_text_rgb("Electric", 255, 255, 0), health=220, speed=195, damage_multiplier=1.7, defense= 100, moves= [instant_strike, lightning_charge, thunder_storm, metal_chomp, roll_ram, gust])

companion_inventory = []

invalid_companion_responses = [
    '"I dont think we got that one?... uh try again?"',
    '"Whats that? Just try again, I guess..."',
    '"uhh?... try again?"',
    '"Just say either the name or just 1, 2, 3 or 4... oh uh 1, 2, or 3..."',
]


forest_wild = [
    blossma,
    mosspre,
    rib_rab,
    rat_rat,
    sqanib,
    foongar,
    roglis,
    blossume,
    stumptas,
    shroomgart,
    loofwis,
    riba_ruba,
    sqornatib,
    maloofo,
    rogilons,
    electric_mouse,
    plant_frog,
    plant_toad,
    water_turtle,
    fire_lizard,
    plant_goliath,
    water_tortoise,
    fire_chameleon,

]

forest_weights = [
    30, # Blossma
    30, # Mosspre
    20, # Rib Rab
    20, # Rat Rat
    19, # Sqanib1
    18, # Foongar
    16, # roglis
    15, # Blossume
    14, # Stumptas
    14, # Shroomgart
    13, # Loofwis
    12, # Riba Ruba
    11, #sqornatib
    10, # Maloofo
    8, # Rogilons
    5, # Electric Mouse
    3, # Plant Frog
    2, # Plant Toad
    2, # Water Turtle
    2, # Fire Lizard
    1, # Plant Goliath
    1, # Water Tortoise
    1, # Fire Chameleon
]

def forest():
    global lobby
    print("\n You explore deep into the Forest...")
    wild_opponent = random.choices(forest_wild, weights=forest_weights, k=1)[0]
    print(f"\nA wild {wild_opponent.name} appears!")
    print(f"Element: {wild_opponent.element}")
    print(f"Health: {wild_opponent.health}\n\n")
    lobby -= 1

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
    print('\n\n"Choose you Companion to start your journey, but you can only choose one so think wisely, what will your choice be?"\n')
    user_choice = input(
        f"1. {color_text_rgb('Fire Lizard', 255, 0, 0)}\n"
        f"2. {color_text_rgb('Water Turtle', 0, 188, 255)}\n"
        f"3. {color_text_rgb('Plant Frog', 50, 255, 0)}\n"
    ).lower()
    # This defines the user choice in the valid choices and sorts the chosen Companions into the inventory variable
    if user_choice in valid_companion_choices:
        chosen_companion = valid_companion_choices[user_choice]
        companion_inventory.append(chosen_companion)
    
        # These lines define what Companion you chose and gives a print statment depending on which one
    if chosen_companion == fire_lizard:
        print(f'\n"Great choice! Fire Lizard is a very strong and fast option, but slightly lacks defense and health."\nYou have obtained {color_text_rgb("Fire Lizard", 255, 0, 0)}!')
    elif chosen_companion == water_turtle:
        print(f'\n"Great choice! Water Turtle is a great all-round option to outmatch your foes and become the victor!"\nYou have obtained {color_text_rgb("Water Turtle", 0, 188, 255)}!')
    elif chosen_companion == plant_frog:
        print(f'\n"Great choice! Plant Frog has great defense and health, but is a bit slow, so get ready to tank some hits!"\nYou have obtained {color_text_rgb("Plant Frog", 50, 255, 0)}!')
    elif chosen_companion == electric_mouse:
            print(f'\n"oh... uhh... I guess I could get you that one..."\nYou have obtained {color_text_rgb("Electric Mouse", 255, 255, 0)}!')

    # If the typed word is not in the previously above valid choices it will loop the opening question and give the heads up to provide a valid option and choose a random response
    else:
        print("\n---------------------------------")
        print(random.choice(invalid_companion_responses))

def show_inventory():
    global lobby
    print("\nYour Companion Inventory:")
    for companion in companion_inventory:
        moves_list = ', '.join(move.name for move in companion.moves)
        print(
            f"-   {companion.name}    "
            f"{color_text_rgb('Element', 255, 255, 255)}: {companion.element}    "
            f"{color_text_rgb('HP', 255, 255, 255)}: {color_text_rgb(str(companion.health), 0, 255, 0)}    "
            f"{color_text_rgb('Damage', 255, 255, 255)}: {color_text_rgb(str(companion.damage_multiplier), 255, 185, 130)}{color_text_rgb('x', 255, 185, 130)}    "
            f"{color_text_rgb('Defense', 255, 255, 255)}: {color_text_rgb(str(companion.defense), 0, 162, 54)}    "
            f"{color_text_rgb('Speed', 255, 255, 255)}: {color_text_rgb(str(companion.speed), 138, 232, 255)}\n"
            f"    {color_text_rgb('Moves', 255, 255, 255)}: {moves_list}\n"
        )
    lobby -= 1
def area_info():
    global lobby
    print("\nArea Info:\n"
        f"- {color_text_rgb('Forest', 190, 250, 188)}: Easy, dense Forest, containing an increased amount of {color_text_rgb('Plant', 50, 255, 0)} element Companions!\n"
        f"- {color_text_rgb('Beach', 158, 194, 255)}: Easy, Ocean-side, containing an increased amount of {color_text_rgb('Water', 0, 188, 255)} element Companions!\n"
        f"- {color_text_rgb('Desert', 252, 215, 215)}: Easy, scorching Desert, containing an increased amount of {color_text_rgb('Fire', 255, 0, 0)} element Companions!\n")
    lobby -= 1

def play():
    while True:
        print("\nWhere would you like to explore?\n")
        area_choice = input(
        f"1. {color_text_rgb('Forest', 190, 250, 188)}\n"
        f"2. {color_text_rgb('Beach', 158, 194, 255)}\n"
        f"3. {color_text_rgb('Desert', 252, 215, 215)}\n").lower()
        if area_choice in ["forest", "1"]:
            forest()
            break
        elif area_choice in ["beach", "2"]:
            print()
            break
        elif area_choice in ["desert", "3"]:
            print()
            break
        else:
            print("Invalid area")

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