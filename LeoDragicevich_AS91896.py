# My imports used
import random
import os
import re
import copy

# This is defining the clear_screen and what it does
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# I can use this ID to edit the text colour in RGB for a more advanced colour metric by putting it in formula
def colour_text_rgb(text, r, g, b):
    return f"\033[1m\033[38;2;{r};{g};{b}m{text}\033[0m"

# This line  to strip ANSI colour codes
_ansi_re = re.compile(r'\x1b\[[0-9;]*m')
def _strip_ansi(s: str) -> str:
    return _ansi_re.sub('', s)

# This class is to define what a Companion needs, including their stats and elements
class Companion:
    def __init__(
        self,
        name,
        element,
        health,
        max_health=None,  # Optional now
        damage_multiplier=1.0,
        defense=0,
        speed=0,
        moves=None,
        xp=0,
        first_evolution=None,
        second_evolution=None,
        first_evolution_xp=10,
        second_evolution_xp=35,
    ):
        self.name = name
        self.element = element
        self.health = health
        self.max_health = max_health if max_health is not None else health  # Default to health
        self.damage_multiplier = damage_multiplier
        self.defense = defense
        self.speed = speed
        self.moves = moves or []
        self.xp = xp
        self.first_evolution = first_evolution
        self.second_evolution = second_evolution
        self.first_evolution_xp = first_evolution_xp
        self.second_evolution_xp = second_evolution_xp

    def gain_xp_and_check_evolution(self):
        self.xp += 1
        print(f"{self.name} gained 1 XP! Total XP: {self.xp}")

        if self.xp < self.first_evolution_xp:
            print(f"{self.name} needs {self.first_evolution_xp - self.xp} more XP to evolve.")
        elif self.xp < self.second_evolution_xp:
            if self.name == self.first_evolution:
                print(f"{self.name} needs {self.second_evolution_xp - self.xp} more XP to evolve again.")
            elif self.first_evolution:
                # Evolve to first evolution
                print(f"{self.name} is evolving into {self.first_evolution}!")
                evolved = globals()[self.first_evolution]
                self.evolve_to(evolved)
        elif self.name == self.second_evolution:
            print(f"{self.name} is at max evolution.")
        else:
            # Evolve to second evolution
            print(f"{self.name} is evolving into {self.second_evolution}!")
            evolved = globals()[self.second_evolution]
            self.evolve_to(evolved)

    def evolve_to(self, evolved_form):
        self.name = evolved_form.name
        self.element = evolved_form.element
        self.health = evolved_form.health
        self.max_health = evolved_form.max_health
        self.damage_multiplier = evolved_form.damage_multiplier
        self.defense = evolved_form.defense
        self.speed = evolved_form.speed
        self.moves = evolved_form.moves
        self.first_evolution = evolved_form.first_evolution
        self.second_evolution = evolved_form.second_evolution
        self.first_evolution_xp = evolved_form.first_evolution_xp
        self.second_evolution_xp = evolved_form.second_evolution_xp
        print(f"Your Companion Evolved into {self.name}!")

    def __str__(self):
        move_names = ', '.join([move.name for move in self.moves])
        return (
            f"{self.name} ({self.element}) - HP: {self.health}/{self.max_health}, "
            f"Damage: {self.damage_multiplier}x, Defense: {self.defense}, Speed: {self.speed}, "
            f"XP: {self.xp}, Moves: {move_names}"
        )
# This class is to define what Moves need, including name, element and damage
class Moves:
    def __init__(self, name, element, min_damage, max_damage=None):
        self.name = name
        self.element = element
        self.min_damage = min_damage
        self.max_damage = max_damage if max_damage is not None else min_damage
    # This line randomises the damage output inbetween max and min damage
    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

# These lines are to write the stats of the moves

# None Element moves
tackle = Moves(colour_text_rgb("Tackle", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=20, max_damage=20)
peck = Moves(colour_text_rgb("Peck", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=24, max_damage=24)
scratch = Moves(colour_text_rgb("Scratch", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=25, max_damage=25)
quick_attack = Moves(colour_text_rgb("Quick Attack", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=24, max_damage=24)
claw = Moves(colour_text_rgb("Claw", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=36, max_damage=36)
snap = Moves(colour_text_rgb("Snap", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=37, max_damage=37)
nibble = Moves(colour_text_rgb("Nibble", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=16, max_damage=48)
bite = Moves(colour_text_rgb("Bite", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=40, max_damage=40)
quick_claw = Moves(colour_text_rgb("Quick Claw", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=48, max_damage=48)
chomp = Moves(colour_text_rgb("Chomp", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=60, max_damage=60)
gulp = Moves(colour_text_rgb("Gulp", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=63, max_damage=63)
instant_strike = Moves(colour_text_rgb("Instant Strike", 205, 205, 205), colour_text_rgb("None", 205, 205, 205), min_damage=71, max_damage=71)

# Fire Element moves
ember = Moves(colour_text_rgb("Ember", 255, 0, 0), colour_text_rgb("Fire", 255, 0, 0), min_damage=30, max_damage=30)
flame = Moves(colour_text_rgb("Flame", 255, 0, 0), colour_text_rgb("Fire", 255, 0, 0), min_damage=23, max_damage=52)
fire_ball = Moves(colour_text_rgb("Fire Ball", 255, 0, 0), colour_text_rgb("Fire", 255, 0, 0), min_damage=88, max_damage=88)
fire_storm = Moves(colour_text_rgb("Fire Storm", 255, 0, 0), colour_text_rgb("Fire", 255, 0, 0), min_damage=46, max_damage=129)

# Water Element moves
water_gun = Moves(colour_text_rgb("Water Gun", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), min_damage=30, max_damage=30)
liquid_combat = Moves(colour_text_rgb("Liquid Combat", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), min_damage=52, max_damage=52)
splash = Moves(colour_text_rgb("Splash", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), min_damage=23, max_damage=61)
pressure_wash = Moves(colour_text_rgb("Pressure Wash", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), min_damage=81, max_damage=81)
tsunami = Moves(colour_text_rgb("Tsunami", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), min_damage=42, max_damage=119)

# Plant Element moves
petal_cut = Moves(colour_text_rgb("Petal Cut", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=18, max_damage=18)
petal_pinch = Moves(colour_text_rgb("Petal Pinch", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=8, max_damage=27)
vine_whip = Moves(colour_text_rgb("Vine Whip", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=30, max_damage=30)
pine_punch = Moves(colour_text_rgb("Pine Punch", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=38, max_damage=38)
thorn_barrage = Moves(colour_text_rgb("Thorn Barrage", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=23, max_damage=52)
flower_power = Moves(colour_text_rgb("Flower Power", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=50, max_damage=50)
tree_smash = Moves(colour_text_rgb("Tree Smash", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=62, max_damage=62)
tanglement = Moves(colour_text_rgb("Tanglement", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=28, max_damage=68)
plant_pounding = Moves(colour_text_rgb("Plant Pounding", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=25, max_damage=75)
leaf_storm = Moves(colour_text_rgb("Leaf Storm", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), min_damage=32, max_damage=109)

# Electric Element moves
thunder_shock = Moves(colour_text_rgb("Thunder Shock", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=34, max_damage=34)
lightning_punch = Moves(colour_text_rgb("Lightning Punch", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=52, max_damage=52)
charged_zap = Moves(colour_text_rgb("Charged Zap", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=61, max_damage=61)
thunder_bolt = Moves(colour_text_rgb("Thunder Bolt", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=34, max_damage=78)
lightning_charge = Moves(colour_text_rgb("Lightning Charge", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=97, max_damage=97)
thunder_storm = Moves(colour_text_rgb("Thunder Storm", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), min_damage=79, max_damage=118)

# Enraged Element moves
head_smash = Moves(colour_text_rgb("Head Smash", 229, 70, 81), colour_text_rgb("Enraged", 229, 70, 81), min_damage=60, max_damage=60)
charge = Moves(colour_text_rgb("Charge", 229, 70, 81), colour_text_rgb("Enraged", 229, 70, 81), min_damage=80, max_damage=80)
stomp = Moves(colour_text_rgb("Stomp", 229, 70, 81), colour_text_rgb("Enraged", 229, 70, 81), min_damage=84, max_damage=84)

# Wind Element moves
winds_edge = Moves(colour_text_rgb("Winds Edge", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=23, max_damage=23)
wing_push = Moves(colour_text_rgb("Wing Push", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=28, max_damage=28)
breeze = Moves(colour_text_rgb("Breeze", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=30, max_damage=30)
feather_storm = Moves(colour_text_rgb("Feather Storm", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=14, max_damage=53)
wing_slash = Moves(colour_text_rgb("Wing Slash", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=76, max_damage=76)
dust_devil = Moves(colour_text_rgb("Dust Devil", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=38, max_damage=78)
gust = Moves(colour_text_rgb("Gust", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=80, max_damage=80)
windy_day = Moves(colour_text_rgb("Windy Day", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=54, max_damage=92)
tornado = Moves(colour_text_rgb("Tornado", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=82, max_damage=119)
cyclone = Moves(colour_text_rgb("Cyclone", 164, 226, 242), colour_text_rgb("Wind", 164, 226, 242), min_damage=63, max_damage=182)

# Armoured Element moves
rollout = Moves("Rollout", colour_text_rgb("Armoured", 70, 124, 90), min_damage=36, max_damage=36)
grounded_push = Moves("Grounded Push", colour_text_rgb("Armoured", 70, 124, 90), min_damage=62, max_damage=62)
shell_ram = Moves("Shell Spin", colour_text_rgb("Armoured", 70, 124, 90), min_damage=80, max_damage=80)
roll_ram = Moves("Roll Ram", colour_text_rgb("Armoured", 70, 124, 90), min_damage=84, max_damage=84)
shelled_shrapnel = Moves("Shelled Shrapnel", colour_text_rgb("Armoured", 70, 124, 90), min_damage=24, max_damage=130)

# Spirit Element moves
ghostly_punch = Moves(colour_text_rgb("Ghostly Punch", 137, 0, 255), colour_text_rgb("Spirit", 137, 0, 255), min_damage=30, max_damage=30)
scare = Moves(colour_text_rgb("Scare", 137, 0, 255), colour_text_rgb("Spirit", 137, 0, 255), min_damage=24, max_damage=53)
tongue_strike = Moves(colour_text_rgb("Tongue Strike", 137, 0, 255), colour_text_rgb("Spirit", 137, 0, 255), min_damage=62, max_damage=62)

nightmare = Moves(colour_text_rgb("Nightmare", 137, 0, 255), colour_text_rgb("Spirit", 137, 0, 255), min_damage=122, max_damage=122)
soul_steal = Moves(colour_text_rgb("Soul Steal", 137, 0, 255), colour_text_rgb("Spirit", 137, 0, 255), min_damage=52, max_damage=172)

# Toxic Element moves
foul_stench = Moves(colour_text_rgb("Foul Stench", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=24, max_damage=24)
toxic_touch = Moves(colour_text_rgb("Toxic Touch", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=30, max_damage=30)
spore_cloud = Moves(colour_text_rgb("Spore Cloud", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=1, max_damage=51)
venom_claw = Moves(colour_text_rgb("Venom Claw", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=58, max_damage=58)
poison_spores = Moves(colour_text_rgb("Poison Spores", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=2, max_damage=93)
toxic_spores = Moves(colour_text_rgb("Toxic Spores", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=4, max_damage=169)
spore_storm = Moves(colour_text_rgb("Spore Storm", 134, 0, 120), colour_text_rgb("Toxic", 134, 0, 120), min_damage=6, max_damage=282)

# Rock Element moves
pebble_punch = Moves(colour_text_rgb("Pebble Punch", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=20, max_damage=20)
mud_slap = Moves(colour_text_rgb("Mud Slap", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=36, max_damage=36)
stone_edge = Moves(colour_text_rgb("Stone Edge", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=44, max_damage=44)
rock_toss = Moves(colour_text_rgb("Rock Toss", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=0, max_damage=50)
iron_tail = Moves(colour_text_rgb("Iron Tail", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=54, max_damage=54)
metal_chomp = Moves(colour_text_rgb("Metal Chomp", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=72, max_damage=72)
rock_barrage = Moves(colour_text_rgb("Rock Barrage", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=44, max_damage=78)
rock_slide = Moves(colour_text_rgb("Rock Slide", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=60, max_damage=84)
cementation = Moves(colour_text_rgb("Cementation", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=101, max_damage=101)
earthquake = Moves(colour_text_rgb("Earthquake", 141, 138, 131), colour_text_rgb("Rock", 141, 138, 131), min_damage=42, max_damage=173)

# These lines are to write the stats of the companions and their moves

# Rat Rat evolution line
rate_cate = Companion(colour_text_rgb("Rate Cate", 220, 208, 178), colour_text_rgb("None", 205, 205, 205), health=154, speed=67, damage_multiplier=1.4, defense= 61, moves= [tackle, scratch, claw, nibble])
rat_rat = Companion(colour_text_rgb("Rat Rat", 192, 176, 201), colour_text_rgb("None", 205, 205, 205), health=80, speed=32, damage_multiplier=0.9, defense= 35, moves= [tackle, scratch], first_evolution= 'rate_cate', second_evolution=None,)

# Rib Rab evolution line
rabta_rubast = Companion(colour_text_rgb("Rabta Rubast", 199, 106, 125), colour_text_rgb("Enraged", 229, 70, 81), health=210, speed=101, damage_multiplier=2.3, defense= 90, moves= [chomp, charge, stomp])
riba_ruba = Companion(colour_text_rgb("Riba Ruba", 206, 196, 171), colour_text_rgb("None", 205, 205, 205), health=84, speed=46, damage_multiplier=0.9, defense= 38, moves= [claw, nibble], second_evolution= rabta_rubast)
rib_rab = Companion(colour_text_rgb("Rib Rab", 220, 211, 190), colour_text_rgb("None", 205, 205, 205), health=74, speed=36, damage_multiplier=0.8, defense= 28, moves= [nibble], first_evolution= riba_ruba)

# Sqanib evolution line
sqornatib = Companion(colour_text_rgb("Sqornatib", 123, 139, 168), colour_text_rgb("Wind", 164, 226, 242), health=98, speed=82, damage_multiplier=1.5, defense= 39, moves= [wing_slash, windy_day, gulp, charge], first_evolution=None, second_evolution=None,)
sqanib = Companion(colour_text_rgb("Sqanib", 165, 196, 215), colour_text_rgb("None", 205, 205, 205), health=64, speed=44, damage_multiplier=1.1, defense= 22, moves= [peck, wing_push, feather_storm], first_evolution= 'sqornatib', second_evolution=None,)

# Tafalu evolution line
lafatulu = Companion(colour_text_rgb("Lafatulu", 113, 206, 160), colour_text_rgb("Wind", 164, 226, 242), health=151, speed=83, damage_multiplier=1.2, defense= 54, moves= [breeze, feather_storm, thorn_barrage])
tafalu = Companion(colour_text_rgb("Tafalu", 157, 238, 213), colour_text_rgb("Wind", 164, 226, 242), health=89, speed=41, damage_multiplier=0.9, defense= 29, moves= [peck, winds_edge], first_evolution= 'lafatulu')

# Fire Lizard evolution line
fire_dragon = Companion(colour_text_rgb("Fire Dragon", 255, 145, 0), colour_text_rgb("Fire", 255, 0, 0), health=250, speed=100, damage_multiplier=2, defense= 110, moves= [chomp, fire_ball, fire_storm, charge, wing_slash ])
fire_chameleon = Companion(colour_text_rgb("Fire Chameleon", 255, 94, 0), colour_text_rgb("Fire", 255, 0, 0), health=165, speed=60, damage_multiplier=1.4, defense= 70, moves= [bite, ember, flame], second_evolution= 'fire_dragon')
fire_lizard = Companion(colour_text_rgb("Fire Lizard", 255, 0, 0), colour_text_rgb("Fire", 255, 0, 0), health=100, speed=30, damage_multiplier=1.2, defense= 40, moves= [tackle, ember], first_evolution= 'fire_chameleon')

# Water Turtle evolution line
water_galapagos = Companion(colour_text_rgb("Water Galapagos", 0, 0, 255), colour_text_rgb("Water", 0, 188, 255), health=310, speed=79, damage_multiplier=1.6, defense= 145, moves= [chomp, pressure_wash, tsunami, shell_ram, stomp])
water_tortoise = Companion(colour_text_rgb("Water Tortoise", 0, 78, 255), colour_text_rgb("Water", 0, 188, 255), health=180, speed=50, damage_multiplier=1.3, defense= 80, moves= [snap, water_gun, splash], second_evolution= 'water_galapagos')
water_turtle = Companion(colour_text_rgb("Water Turtle", 0, 188, 255), colour_text_rgb("Water", 0, 188, 255), health=110, speed=25, damage_multiplier=1.1, defense= 45, moves= [tackle, water_gun], first_evolution= 'water_tortoise')

# Crabsture evolution line
crabbastwar = Companion(colour_text_rgb("Crabbastwar", 63, 139, 148), colour_text_rgb("Armoured", 0, 188, 255), health=214, speed=64, damage_multiplier=1.4, defense= 214, moves= [chomp, shell_ram, shelled_shrapnel, pressure_wash])
crabstawir = Companion(colour_text_rgb("Crabstawir", 181, 90, 0), colour_text_rgb("Water", 0, 188, 255), health=132, speed=39, damage_multiplier=1, defense= 79, moves= [quick_claw, liquid_combat, grounded_push], second_evolution= 'crabbastwar')
crabsture = Companion(colour_text_rgb("Crabsture", 255, 174, 91), colour_text_rgb("Water", 0, 188, 255), health=84, speed=21, damage_multiplier=0.8, defense= 39, moves= [claw, water_gun], first_evolution= 'crabstawir')

# Plant Frog evolution line
plant_goliath = Companion(colour_text_rgb("Plant Goliath", 33, 166, 0), colour_text_rgb("Plant", 50, 255, 0), health=365, speed=45, damage_multiplier=1.4, defense= 185, moves= [gulp, tree_smash, leaf_storm, tongue_strike, spore_storm])
plant_toad = Companion(colour_text_rgb("Plant Toad", 46, 228, 0), colour_text_rgb("Plant", 50, 255, 0), health=210, speed=35, damage_multiplier=1.1, defense= 100, moves= [snap, vine_whip, thorn_barrage], second_evolution= 'plant_goliath')
plant_frog = Companion(colour_text_rgb("Plant Frog", 50, 255, 0), colour_text_rgb("Plant", 50, 255, 0), health=120, speed=20, damage_multiplier=0.9, defense= 50, moves= [tackle, vine_whip], first_evolution= 'plant_toad')

# Loofwis evolution line
maloofo = Companion(colour_text_rgb("Maloofo", 108, 146, 57), colour_text_rgb("Plant", 50, 255, 0), health=180, speed=62, damage_multiplier=1.1, defense=79, moves= [plant_pounding, breeze, dust_devil])
loofwis = Companion(colour_text_rgb("Loofwis", 167, 209, 112), colour_text_rgb("Plant", 50, 255, 0), health=140, speed=38, damage_multiplier=1, defense=19, moves= [thorn_barrage, breeze], first_evolution= 'maloofo')

#Blossma evolution line
blossertama = Companion(colour_text_rgb("Blossertama", 98, 146, 0), colour_text_rgb("Plant", 50, 255, 0), health=192, speed=61, damage_multiplier=1.1, defense= 52, moves= [flower_power, plant_pounding, toxic_spores])
blossume = Companion(colour_text_rgb("Blossume", 137, 205, 0), colour_text_rgb("Plant", 50, 255, 0), health=122, speed=48, damage_multiplier=0.9, defense= 42, moves= [pine_punch, thorn_barrage, poison_spores], second_evolution= 'blossertama')
blossma = Companion(colour_text_rgb("Blossma", 171, 255, 0), colour_text_rgb("Plant", 50, 255, 0), health=71, speed=21, damage_multiplier=0.6, defense= 20, moves= [petal_cut, petal_pinch], first_evolution= 'blossume')

#Mosspre evolution line
mossponsa = Companion(colour_text_rgb("Mossponsa", 37, 139, 11), colour_text_rgb("Plant", 50, 255, 0), health=123, speed=31, damage_multiplier=1.1, defense= 62, moves= [pine_punch, tanglement, poison_spores])
mosspre = Companion(colour_text_rgb("Mosspre", 0, 182, 18), colour_text_rgb("Plant", 50, 255, 0), health=85, speed=20, damage_multiplier=0.8, defense= 48, moves= [vine_whip, spore_cloud], first_evolution= 'mossponsa')

# Toforrast evolution line
tofarstaffar = Companion(colour_text_rgb("Toferstaffer", 27, 137, 64), colour_text_rgb("Plant", 50, 255, 0), health=380, speed=80, damage_multiplier=1.6, defense= 78, moves= [gulp, tree_smash, leaf_storm, stomp, rock_slide])
fotorasta = Companion(colour_text_rgb("Fotorasta", 52, 185, 97), colour_text_rgb("Plant", 50, 255, 0), health=230, speed=58, damage_multiplier=1.2, defense= 48, moves= [flower_power, plant_pounding, head_smash, iron_tail], second_evolution= 'tofarstaffer')
toforrast = Companion(colour_text_rgb("Toforrast", 32, 223, 96), colour_text_rgb("Plant", 50, 255, 0), health=140, speed=28, damage_multiplier=0.8, defense= 12, moves= [vine_whip, thorn_barrage, bite], first_evolution= 'fotorasta')

# Foongar evolution line
shroomgart = Companion(colour_text_rgb("Shroomgart", 174, 73, 163), colour_text_rgb("Toxic", 134, 0, 120), health=182, speed=39, damage_multiplier=1.2, defense= 81, moves= [venom_claw, toxic_spores])
foongar = Companion(colour_text_rgb("Foongar", 216, 255, 156), colour_text_rgb("Plant", 50, 255, 0), health=92, speed=26, damage_multiplier=1, defense= 54, moves= [toxic_touch, poison_spores], first_evolution= 'shroomgar')

# Pineto evolution line
pinstawile = Companion(colour_text_rgb("Pinstawile", 40, 117, 12), colour_text_rgb("Plant", 50, 255, 0), health=178, speed=42, damage_multiplier=1.3, defense= 95, moves= [tree_smash, shell_ram, rock_barrage])
pineto = Companion(colour_text_rgb("Pineto", 75, 165, 42), colour_text_rgb("Plant", 50, 255, 0), health=81, speed=27, damage_multiplier=0.8, defense= 56, moves= [pine_punch, thorn_barrage], first_evolution= 'pinstawile')

# Stumptas evolution line
tasmaradark = Companion(colour_text_rgb("Tasmaradark", 75, 45, 98), colour_text_rgb("Spirit", 137, 0, 255), health=340, speed=120, damage_multiplier=2.4, defense= 153, moves= [nightmare, soul_steal, instant_strike ])
tasmandoo = Companion(colour_text_rgb("Tasmandoo", 173, 125, 209), colour_text_rgb("Spirit", 137, 0, 255), health=220, speed=80, damage_multiplier=1.9, defense= 100, moves= [scare, ghostly_punch, scratch], second_evolution= 'tasmaradark')
stumptas = Companion(colour_text_rgb("Stumptas", 56, 75, 4), colour_text_rgb("Plant", 50, 255, 0), health=50, speed=5, damage_multiplier=0.2, defense= 400, moves= [tree_smash, roll_ram, leaf_storm], first_evolution= 'tasmandoo')

# Roglis evolution line
rogilons = Companion(colour_text_rgb("Rogilons", 42, 68, 31), colour_text_rgb("Rock", 141, 138, 131), health=203, speed=32, damage_multiplier=1, defense= 142, moves= [stone_edge, rock_barrage, roll_ram, flower_power])
roglis = Companion(colour_text_rgb("Roglis", 83, 114, 70), colour_text_rgb("Rock", 141, 138, 131), health=102, speed=19, damage_multiplier=0.7, defense= 93, moves= [pebble_punch, rock_toss, vine_whip], first_evolution= 'rogilons')

# Buugwis evolution line
brassteron = Companion(colour_text_rgb("Burgsast", 35, 65, 24), colour_text_rgb("Armoured", 70, 124, 90), health=290, speed=62, damage_multiplier=1, defense= 201, moves= [roll_ram, shelled_shrapnel, rock_slide, charge])
burgsast = Companion(colour_text_rgb("Burgsast", 53, 81, 43), colour_text_rgb("Armoured", 70, 124, 90), health=140, speed=41, damage_multiplier=0.9, defense= 102, moves= [grounded_push, rock_barrage, head_smash], second_evolution= 'brassteron')
buugwis = Companion(colour_text_rgb("Buugwis", 76, 107, 65), colour_text_rgb("Armoured", 70, 124, 90), health=83, speed=26, damage_multiplier=0.7, defense= 72, moves= [rollout, mud_slap], first_evolution= 'burgsast')

# Sporesta evolution line
sporestonine = Companion(colour_text_rgb("Sporestonine", 84, 6, 92), colour_text_rgb("Toxic", 134, 0, 120), health=132, speed=139, damage_multiplier=2.6, defense= 49, moves= [spore_storm])
sporpoin = Companion(colour_text_rgb("Sporpoin", 206, 60, 222), colour_text_rgb("Toxic", 134, 0, 120), health=83, speed=83, damage_multiplier=1.6, defense= 21, moves= [poison_spores], second_evolution= 'sporestonine')
sportix = Companion(colour_text_rgb("Sportix", 167, 30, 182), colour_text_rgb("Toxic", 134, 0, 120), health=105, speed=105, damage_multiplier=2, defense= 39, moves= [toxic_spores], first_evolution= 'sporpoin')

# Electric Mouse evolution line
electric_capybara = Companion(colour_text_rgb("Electric Capybara", 243, 182, 0), colour_text_rgb("Electric", 255, 255, 0), health=220, speed=195, damage_multiplier=1.7, defense= 100, moves= [instant_strike, lightning_charge, thunder_storm, metal_chomp, roll_ram, gust])
electric_rat = Companion(colour_text_rgb("Electric Rat", 255, 205, 0), colour_text_rgb("Electric", 255, 255, 0), health=150, speed=82, damage_multiplier=1.3, defense= 60, moves= [quick_claw, lightning_punch, thunder_bolt, iron_tail], second_evolution= 'electric_capybara')
electric_mouse = Companion(colour_text_rgb("Electric Mouse", 255, 255, 0), colour_text_rgb("Electric", 255, 255, 0), health=100, speed=42, damage_multiplier=1.0, defense= 35, moves= [quick_attack, thunder_shock], first_evolution= 'electric_rat')

# Zaatran evolution line
zooshatraan = Companion(colour_text_rgb("Zooshatraan", 164, 169, 11), colour_text_rgb("Electric", 255, 255, 0), health=181, speed=142, damage_multiplier=1.5, defense= 252, moves= [lightning_charge, thunder_storm, roll_ram, shelled_shrapnel])
ziptaraan = Companion(colour_text_rgb("Ziptaraan", 203, 208, 65), colour_text_rgb("Electric", 255, 255, 0), health=128, speed=73, damage_multiplier=1.2, defense= 112, moves= [charged_zap, thunder_shock, grounded_push], second_evolution= 'zooshatraan')
zaataran = Companion(colour_text_rgb("Zaataran", 226, 253, 91), colour_text_rgb("Electric", 255, 255, 0), health=94, speed=39, damage_multiplier=0.9, defense= 54, moves= [thunder_shock, rollout], first_evolution= 'ziptaraan')

# Chart used to orginise what elements are weak or strong to what
element_chart = {
    "None": {
        "strong_against": ["Spirit", "Armoured"],
        "weak_against": ["Toxic", "Enraged"]
    },
    "Fire": {
        "strong_against": ["Plant", "Armoured"],
        "weak_against": ["Water", "Wind"]
    },
    "Water": {
        "strong_against": ["Fire","Rock"],
        "weak_against": ["Plant", "Electric"]
    },
    "Plant": {
        "strong_against": ["Water", "Spirit"],
        "weak_against": ["Fire", "Electric"]
    },
    "Electric": {
        "strong_against": ["Water", "Wind"],
        "weak_against": ["Rock", "Armoured"]
    },
    "Rock": {
        "strong_against": ["Electric", "Toxic"],
        "weak_against": ["Water", "Enraged"]
    },
    "Wind": {
        "strong_against": ["Fire", "Plant"],
        "weak_against": ["Electric", "Armoured"]
    },
    "Armoured": {
        "strong_against": ["Wind", "Enraged"],
        "weak_against": ["Fire", "None"]
    },    
    "Spirit": {
        "strong_against": ["Enraged", "Toxic"],
        "weak_against": ["Plant", "None"],
    },
    "Toxic": {
        "strong_against": ["None","Plant"],
        "weak_against": ["Rock", "Spirit"]
    },
    "Enraged": {
        "strong_against": ["None", "Rock"],
        "weak_against": ["Spirit", "Armoured"]        
    }
}

# List containing what Companions are in forest_wild
forest_wild = [
    blossma,
    mosspre,
    pineto,
    rib_rab,
    rat_rat,
    tafalu,
    sqanib,
    foongar,
    blossume,
    stumptas,
    roglis,
    buugwis,
    toforrast,
    zaataran,
    pinstawile,
    mossponsa,
    lafatulu,
    burgsast,
    sporpoin,
    shroomgart,
    loofwis,
    riba_ruba,
    fotorasta,
    sqornatib,
    maloofo,
    sportix,
    rogilons,
    ziptaraan,
    tasmandoo,
    tofarstaffar,
    electric_mouse,
    plant_frog,
    plant_toad,
    water_turtle,
    fire_lizard,
    plant_goliath,
    water_tortoise,
    fire_chameleon,
]

# List containing the weights for the Companions in forest_wild
forest_weights = [
    22, # Blossma
    22, # Mosspre
    16, # Pineto
    15, # Rib Rab
    15, # Rat Rat
    14, # Tafalu
    14, # Sqanib
    14, # Foongar
    15, # Blossume
    14, # Stumptas
    13, # roglis
    13, # Buugwis
    13, # Toforrast
    13, # Zaataran
    12, # Pinstawile
    12, # Mossponsa
    12, # Lafatulu
    12, # Burgsast
    11, # Sporpoin
    11, # Shroomgart
    13, # Loofwis
    12, # Riba Ruba
    12, # Fotorasta
    11, #sqornatib
    10, # Maloofo
    9, # Sportix
    8, # Rogilons
    8, # Tasmandoo
    8, # Ziptaraan
    7, # Tofarstaffar
    5, # Electric Mouse
    3, # Plant Frog
    2, # Plant Toad
    2, # Water Turtle
    2, # Fire Lizard
    1, # Plant Goliath
    1, # Water Tortoise
    1, # Fire Chameleon
]

# List containing what Companions are in beach_wild
beach_wild = [
    crabsture,
    crabstawir,
    electric_mouse,
    water_turtle,
    water_tortoise,
    plant_frog,
    fire_lizard,
    water_galapagos,
    plant_toad,
    fire_chameleon
]

# List containing the weights for the Companions in beach_wild
beach_weights = [
    20, # Crabsture
    12, # Crabstawir
    5, # Electric Mouse
    3, # Water Turtle
    2, # Water Tortoise
    2, # Plant Frog
    2, # Fire Lizard
    1, # Water Galapagos
    1, # Plant Toad
    1, # Fire Chameleon
]

# List containing what Companions are in desert_wild
desert_wild = [
    electric_mouse,
    fire_lizard,
    fire_chameleon,
    plant_frog,
    water_turtle,
    fire_dragon,
    plant_toad,
    water_tortoise
]

# List containing the weights for the Companions in desert_wild
desert_weights = [
    5, # Electric Mouse
    3, # Fire Lizard
    2, # Fire Chameleon
    2, # Plant Frog
    2, # Water Turtle
    1, # Fire Dragon
    1, # Plant Toad
    1, # Water Tortoise
]

# List for active companions max 3
active_companions = []

# List for stored companions infinite
stored_companions = []

# Shows that the player companion is empty unless you are in a battle
player_companion = None

# This is defining the get_element_multiplier, which makes the attackers move get a 2x or 0.5x multipler depending on their elements on the element chart 
def get_element_multiplier(attacker_element, defender_element):
    # remove colour codes & normalize
    att = _strip_ansi(attacker_element).strip().title()
    def_ = _strip_ansi(defender_element).strip().title()

    chart = element_chart  # your existing plain‑string chart
    if att in chart:
        if def_ in chart[att]["strong_against"]:
            return 2.0
        elif def_ in chart[att]["weak_against"]:
            return 0.5
    return 1.0



# This defines adding a new companion and states that if your active Companions are full it sends it to the stored Companions
def add_new_companion(new_companion):
    if len(active_companions) < 3:
        active_companions.append(new_companion)
        print(f"{new_companion.name} added to your active Companions.")
    else:
        stored_companions.append(new_companion)
        print(f"{new_companion.name} was sent to storage (Active Companions full).")

# This defines choose_player_companion, which is what is done before battle and you choose which one of your active Companions are used
def choose_player_companion():
    print("\nChoose a companion to use for battle:")
    for i, comp in enumerate(active_companions, 1):
        print(f"{i}. {comp.name}\n")
    
    while True:
        try:    
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(active_companions):
                return active_companions[choice - 1]
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid number")


# This defines the battle function and displays the order of it all including attacks
def battle(player, opponent):
    turn_order = decide_turn_order(player, opponent)

    while player.health > 0 and opponent.health > 0:
        for attacker in turn_order:
            defender = player if attacker is opponent else opponent

            print(f"\n{attacker.name}'s Turn!")
            print(
                f"{player.name} HP: {colour_text_rgb(str(player.health), 0, 255, 0)} | "
                f"{opponent.name} HP: {colour_text_rgb(str(opponent.health), 0, 255, 0)}"
            )

            # Player move
            if attacker is player:
                print("\nChoose a move:")
                for i, move in enumerate(player.moves, 1):
                    print(f"{i}. {move.name} ({move.min_damage}-{move.max_damage})")
                while True:
                    try:
                        idx = int(input("Enter move number: "))
                        if 1 <= idx <= len(player.moves):
                            chosen_move = player.moves[idx - 1]
                            break
                    except ValueError:
                        pass
                    print("Invalid choice; enter a number.")
            else:
                chosen_move = random.choice(opponent.moves)
                print(f"{opponent.name} used {chosen_move.name}!")

            raw = random.randint(chosen_move.min_damage, chosen_move.max_damage)
            scaled = raw * attacker.damage_multiplier

            elem_mul = get_element_multiplier(attacker.element, defender.element)
            if elem_mul > 1:
                print(colour_text_rgb("It's super effective!", 255, 100, 100))
            elif elem_mul < 1:
                print(colour_text_rgb("It's not very effective...", 150, 150, 255))

            reduction = defender.defense / (defender.defense + 100)
            dmg_after_def = int(scaled * (1 - reduction))

            final_dmg = max(int(dmg_after_def * elem_mul), 1)
            defender.health -= final_dmg
            print(f"{defender.name} {colour_text_rgb(f'took {final_dmg} damage!', 255, 255, 255)}")

            if defender.health <= 0:
                print(f"\n{defender.name} has fainted!")

                if defender is player:
                    print(f"\n{colour_text_rgb('You ', 255, 255, 255)}{colour_text_rgb(' Lost ', 255, 0, 0)}{colour_text_rgb(' the battle...', 255, 255, 255)}")
                    player.health = player.max_health
                    print("Returning to the lobby...\n")
                    return

                # You win!
                print(f"\n{colour_text_rgb('You ', 255, 255, 255)}{colour_text_rgb(' Won ', 0, 255, 0)}{colour_text_rgb(' the battle!', 255, 255, 255)}")

                # Ask to capture or gain XP
                while True:
                    choice = input("\n1. Capture the wild companion?\n2. Gain XP from the battle").lower()
                    if choice in ["1", "Capture", "yes", "y"]:
                        add_new_companion(copy.deepcopy(defender))
                        break
                    elif choice in ["2", "no", "n", "xp", "gain"]:
                        player.gain_xp_and_check_evolution()
                        break
                    else:
                        print("Invalid input. Please type (1 or 2)")

                player.health = player.max_health
                print("Returning to the lobby...\n")
                return

def gain_xp_and_check_evolution(self):
    self.xp += 1
    print(f"{self.name} gained 1 XP! Total XP: {self.xp}")

    if self.xp < self.first_evolution_xp:
        print(f"{self.name} needs {self.first_evolution_xp - self.xp} more XP to evolve.")
    elif self.xp < self.second_evolution_xp:
        if self.name == self.first_evolution:
            print(f"{self.name} needs {self.second_evolution_xp - self.xp} more XP to evolve again.")
        elif self.first_evolution:
            # Evolve to first evolution
            print(f"{self.name} is evolving into {self.first_evolution}!")
            evolved = globals()[self.first_evolution]
            self.evolve_to(evolved)
    elif self.name == self.second_evolution:
        print(f"{self.name} is at max evolution.")
    else:
        # Evolve to second evolution
        print(f"{self.name} is evolving into {self.second_evolution}!")
        evolved = globals()[self.second_evolution]
        self.evolve_to(evolved)

def evolve_to(self, evolved_form):
    self.name = evolved_form.name
    self.element = evolved_form.element
    self.health = evolved_form.health
    self.max_health = evolved_form.max_health
    self.damage_multiplier = evolved_form.damage_multiplier
    self.defense = evolved_form.defense
    self.speed = evolved_form.speed
    self.moves = evolved_form.moves
    self.first_evolution = evolved_form.first_evolution
    self.second_evolution = evolved_form.second_evolution
    self.first_evolution_xp = evolved_form.first_evolution_xp
    self.second_evolution_xp = evolved_form.second_evolution_xp
    print(f"Evolution complete! Say hello to {self.name}!")

# These are all the random responses that could be chosen when typing an invalid option when choosing your starter
invalid_companion_responses = [
    '"I dont think we got that one?... uh try again?"',
    '"Whats that? Just try again, I guess..."',
    '"uhh?... try again?"',
    '"Just say either the name or just 1, 2, 3 or 4... oh uh 1, 2, or 3..."', # Hints towards the secret 4th starter
]

# This defines the player turn order and who starts depending on the speed stat
def decide_turn_order(player, wild):
    if player.speed >= wild.speed: # If  player speed is greater than wild speed player starts
        return [player, wild]
    else:
        return [wild, player]
    
def forest():
    clear_screen()
    global player_companion
    global lobby
    print(colour_text_rgb('\nYou explore deep into the Forest...', 255, 255, 255))
    wild_opponent = copy.deepcopy(random.choices(forest_wild, weights=forest_weights, k=1)[0])
    print(f"\nA wild {wild_opponent.name} appears!")
    print(f"{colour_text_rgb('Element', 255, 255, 255)}: {wild_opponent.element}")
    print(f"{colour_text_rgb('Health', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.health), 0, 255, 0)}")
    print(f"{colour_text_rgb('Speed', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.speed), 138, 232, 255)}\n")

    player_companion = choose_player_companion()

    if player_companion.speed >= wild_opponent.speed:
        clear_screen()
        print(f"\n{colour_text_rgb('Your', 255, 255, 255)} {player_companion.name} {colour_text_rgb('outsped', 255, 255, 255)} {wild_opponent.name}{colour_text_rgb('!', 255, 255, 255)}")
    else:
        clear_screen()
        print(f"\n{wild_opponent.name} {colour_text_rgb('outsped your', 255, 255, 255)} {player_companion.name}{colour_text_rgb('!', 255, 255, 255)}")
    
    battle(player_companion, wild_opponent)


def beach():
    clear_screen()
    global player_companion
    global lobby
    print(colour_text_rgb('\nYou travel far along the Beach...', 255, 255, 255))
    wild_opponent = copy.deepcopy(random.choices(beach_wild, weights=beach_weights, k=1)[0])
    print(f"\nA wild {wild_opponent.name} appears!")
    print(f"{colour_text_rgb('Element', 255, 255, 255)}: {wild_opponent.element}")
    print(f"{colour_text_rgb('Health', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.health), 0, 255, 0)}")
    print(f"{colour_text_rgb('Speed', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.speed), 138, 232, 255)}\n")

    player_companion = choose_player_companion()

    if player_companion.speed >= wild_opponent.speed:
        clear_screen()
        print(f"\n{colour_text_rgb('Your', 255, 255, 255)} {player_companion.name} {colour_text_rgb('outsped', 255, 255, 255)} {wild_opponent.name}{colour_text_rgb('!', 255, 255, 255)}")
    else:
        clear_screen()
        print(f"\n{wild_opponent.name} {colour_text_rgb('outsped your', 255, 255, 255)} {player_companion.name}{colour_text_rgb('!', 255, 255, 255)}")
    
    battle(player_companion, wild_opponent)

def desert():
    clear_screen()
    global player_companion
    global lobby
    print(colour_text_rgb('\nYou venture out into the Desert...', 255, 255, 255))
    wild_opponent = copy.deepcopy(random.choices(desert_wild, weights=desert_weights, k=1)[0])
    print(f"\nA wild {wild_opponent.name} appears!")
    print(f"{colour_text_rgb('Element', 255, 255, 255)}: {wild_opponent.element}")
    print(f"{colour_text_rgb('Health', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.health), 0, 255, 0)}")
    print(f"{colour_text_rgb('Speed', 255, 255, 255)}: {colour_text_rgb(str(wild_opponent.speed), 138, 232, 255)}\n")

    player_companion = choose_player_companion()

    if player_companion.speed >= wild_opponent.speed:
        clear_screen()
        print(f"\n{colour_text_rgb('Your', 255, 255, 255)} {player_companion.name} {colour_text_rgb('outsped', 255, 255, 255)} {wild_opponent.name}{colour_text_rgb('!', 255, 255, 255)}")
    else:
        clear_screen()
        print(f"\n{wild_opponent.name} {colour_text_rgb('outsped your', 255, 255, 255)} {player_companion.name}{colour_text_rgb('!', 255, 255, 255)}")
    
    battle(player_companion, wild_opponent)

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
        f"1. {colour_text_rgb('Fire Lizard', 255, 0, 0)}\n"
        f"2. {colour_text_rgb('Water Turtle', 0, 188, 255)}\n"
        f"3. {colour_text_rgb('Plant Frog', 50, 255, 0)}\n"
    ).lower()
    # This defines the user choice in the valid choices and sorts the chosen Companions into the inventory variable
    if user_choice in valid_companion_choices:
        chosen_companion = valid_companion_choices[user_choice]
        active_companions.append(chosen_companion)
    
        # These lines define what Companion you chose and gives a print statment depending on which one
    if chosen_companion == fire_lizard:
            clear_screen()
            print(f'\n"Great choice! Fire Lizard is a very strong and fast option, but slightly lacks defense and health."\nYou have obtained {colour_text_rgb("Fire Lizard", 255, 0, 0)}!')
    elif chosen_companion == water_turtle:
            clear_screen()
            print(f'\n"Great choice! Water Turtle is a great all-round option to outmatch your foes and become the victor!"\nYou have obtained {colour_text_rgb("Water Turtle", 0, 188, 255)}!')
    elif chosen_companion == plant_frog:
            clear_screen()
            print(f'\n"Great choice! Plant Frog has great defense and health, but is a bit slow, so get ready to tank some hits!"\nYou have obtained {colour_text_rgb("Plant Frog", 50, 255, 0)}!')
    elif chosen_companion == electric_mouse:
            clear_screen()
            print(f'\n"oh... uhh... I guess I could get you that one..."\nYou have obtained {colour_text_rgb("Electric Mouse", 255, 255, 0)}!')

    # If the typed word is not in the previously above valid choices it will loop the opening question and give the heads up to provide a valid option and choose a random response
    else:
        print("\n---------------------------------")
        print(random.choice(invalid_companion_responses))

def show_inventory():
    clear_screen()
    global lobby
    print("\nYour Companion Inventory:")
    for companion in active_companions:
        moves_list = ', '.join(move.name for move in companion.moves)
        print(
            f"-   {companion.name}    "
            f"{colour_text_rgb('Element', 255, 255, 255)}: {companion.element}    "
            f"{colour_text_rgb('HP', 255, 255, 255)}: {colour_text_rgb(str(companion.health), 0, 255, 0)}    "
            f"{colour_text_rgb('Damage', 255, 255, 255)}: {colour_text_rgb(str(companion.damage_multiplier), 255, 185, 130)}{colour_text_rgb('x', 255, 185, 130)}    "
            f"{colour_text_rgb('Defense', 255, 255, 255)}: {colour_text_rgb(str(companion.defense), 0, 162, 54)}    "
            f"{colour_text_rgb('Speed', 255, 255, 255)}: {colour_text_rgb(str(companion.speed), 138, 232, 255)}\n"
            f"    {colour_text_rgb('Moves', 255, 255, 255)}: {moves_list}\n"
        )

def area_info():
    clear_screen()
    global lobby
    print("\nArea Info:\n"
        f"- {colour_text_rgb('Forest', 190, 250, 188)}: Easy, dense Forest, containing an increased amount of {colour_text_rgb('Plant', 50, 255, 0)} element Companions!\n"
        f"- {colour_text_rgb('Beach', 158, 194, 255)}: Easy, Ocean-side, containing an increased amount of {colour_text_rgb('Water', 0, 188, 255)} element Companions!\n"
        f"- {colour_text_rgb('Desert', 252, 215, 215)}: Easy, scorching Desert, containing an increased amount of {colour_text_rgb('Fire', 255, 0, 0)} element Companions!\n")

def play():
    clear_screen()
    print("\nWhere would you like to explore?\n")
    area_choice = input(
        f"1. {colour_text_rgb('Forest', 190, 250, 188)}\n"
        f"2. {colour_text_rgb('Beach', 158, 194, 255)}\n"
        f"3. {colour_text_rgb('Desert', 252, 215, 215)}\n"
        f"4. Return to Lobby\n"
    ).lower()

    if area_choice in ["forest", "1"]:
        forest()
    elif area_choice in ["beach", "2"]:
        beach()
    elif area_choice in ["desert", "3"]:
        desert()
    elif area_choice in ["4", "return", "return to lobby", "lobby"]:
        return  # Takes you back to lobby menu
    else:
        print("Invalid area, try again.")

def element_info():
    clear_screen()

    def get_element_colour(element):
        colours = {
            "None": (180, 180, 180),
            "Fire": (255, 0, 0),
            "Water": (0, 188, 255),
            "Plant": (50, 255, 0),
            "Electric": (255, 255, 0),
            "Rock": (141, 138, 131),
            "Wind": (164, 226, 242),
            "Armoured": (70, 124, 90),
            "Spirit": (137, 0, 255),
            "Toxic": (134, 0, 120),
            "Enraged": (229, 70, 81),
        }
        return colours.get(element, (255, 255, 255))

    print(colour_text_rgb("- Element Info -", 255, 255, 255))
    print()

    for element, info in element_chart.items():
        r, g, b = get_element_colour(element)
        element_colored = colour_text_rgb(element, r, g, b)

        strong_colored = ", ".join([colour_text_rgb(e, *get_element_colour(e)) for e in info["strong_against"]])
        weak_colored = ", ".join([colour_text_rgb(e, *get_element_colour(e)) for e in info["weak_against"]])

        print(f"Element: {element_colored}")
        print(f"  Strong Against: {strong_colored}")
        print(f"  Weak Against  : {weak_colored}\n")

# Once you have chosen a Companion you will begivn this prompt and taken to the main lobby menu
print("\n ---------------------------------\n\nNow that you have chosen your Companion what would you like to do next?\n")

while True:
    print("\nWhat would you like to do next?")
    lobby_choice = input("1. \033[1mPlay!\033[0m\n2. \033[1mView Inventory\033[0m\n3. \033[1mArea Info\033[0m\n4. \033[1mElement Info\033[0m\n\n").lower()

    if lobby_choice in ["1", "play", "play!"]:
        play()
    elif lobby_choice in ["2", "show inventory", "inventory", "view inventory", "showinventory", "viewinventory"]:
        clear_screen()
        show_inventory()
    elif lobby_choice in ["3", "area info", "area", "areainfo"]:
        clear_screen()
        area_info()
    elif lobby_choice in ["4", "element info", "element", "elementinfo"]:
        clear_screen()
        element_info()
    else:
        print("Invalid option, try again.")
