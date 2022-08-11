import random
from time import sleep
delay = 1
areas_dict = {}
game_cmds = "Type 'go' then 'west', 'south', 'east', or 'north' to move to that area. \nType 'look' to look around the area. \nType 'mystats' to check your stats. \n\nType 'interact' then the npc/enemy/item's name to interact with them/it. \n\nType 'help' to bring up the commands again."
game_hints = ["Hint: Explore, try to talk to the npcs, some gives useful hints. There are some questions that you can answer too!", "Hint: Theres secrets almost everywhere in the game! Try to find them! 😃", "Hint: Theres a secret weapon somewhere. Maybe you will find it?"]
last_interaction = ""

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 0
        self.level = 1
        self.xp = 0
        self.xp_needed = 100
        self.last_xp = 100
        self.weapon = "Martial Arts"
        self.armor = "None"
        self.items = []
        self.balance = 100
    
    def __repr__(self):
        return (f"~~Player Stats~~ \nPlayer Name: {self.name} | Player Level: Lv {self.level} \nCurrent XP: {self.xp}xp | XP Needed: {self.xp_needed} XP \nPlayer Health: {self.health} Hp \n\n~~Inventory~~ \nBalance: ${self.balance} \nEquipped Weapon: {self.weapon} \nEquipped Armor: {self.armor} \nItems: {self.items} \n")

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        if self.xp_needed == 0:
            self.level += 1
            self.xp_needed += self.last_xp*2+50
            self.last_xp += self.last_xp*2+50
            print(f"--<You Leveled Up!>-- \n--<You are now level {self.level}>-- \n")

    def ability_selection(self):
        global selected_ability


    
#    def attack(self, enemy):

class Weapon:
    def __init__(self, name, defensive_ability, basic1_ability, basic2_ability, special_ability, ultimate_ability):
        self.name = name
        self.defensive_ability = defensive_ability
        self.basic1_ability = basic1_ability
        self.basic2_ability = basic2_ability
        self.special_ability = special_ability
        self.ultimate_ability = ultimate_ability
    
    def __repr__(self):
        return(f"~~Weapon Info~~ \nName: {self.name} \n\n~~Weapon Abilities~~ \nDefensive: {self.defensive_ability.name} | Accuracy: {self.defensive_ability.accuracy}% \nBasic-1: {self.basic1_ability.name} | Accuracy: {self.basic1_ability.accuracy}% \nBasic-2: {self.basic2_ability.name} | Accuracy: {self.basic2_ability.accuracy}% \nSpecial: {self.special_ability.name} | Accuracy: {self.special_ability.accuracy}% \nUltimate: {self.ultimate_ability.name} | Accuracy: {self.ultimate_ability.accuracy}%\n")
    
class Player_Ability:
    def __init__(self, ability_type, name, min_damage, max_damage, accuracy):
        self.ability_type = ability_type
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.accuracy = accuracy
    
    def __repr__(self):
        return (f"~~Ability Info~~ \nName: {self.name} \nDamage: {self.min_damage}-{self.max_damage} Dmg \nAccuracy: {self.accuracy}% \n")

class Game_Area:
    def __init__(self, sector, name, description, npcs, enemies, items, west, south, east, north):
        self.sector = sector
        self.name = name
        self.description = description
        self.npcs = npcs
        self.enemies = enemies
        self.items = items
        self.west = west
        self.south = south
        self.east = east
        self.north = north
    
    def __repr__(self):
        return (f"~~Area Info~~ \nName: {self.name} \nDescription: {self.description} \nNpcs: {self.npcs} | Enemies: {self.enemies} \nItems: {self.items} \n\n--Paths-- \nWest: {self.west} \nSouth: {self.south} \nEast: {self.east} \nNorth: {self.north} \n")

# class Game_Npc:

# class Game_Enemy:

# -------------------------Data Base-------------------------
# ----------Obtainable Things----------
ingame_weapons = ["Martial Arts", "Rusty Sword", "Dual Daggers", "Katana", "Greatsword", "Dragon Slayer"]
ingame_items = ["Letter", "Key", "Certificate", "Salmon"]

dev_weapons = ["Doombringer"]
# ----------Weapons/Abilties----------
# Note: Format:
# (weapon name)_weapon = Weapon("(Weapon Name)",
#     (weapon name)_(ability type) := Player_Ability("(ability_type)", "(Weapon Name)", (min_damage), (max_damage), (accuracy)),
#     (weapon name)_(ability type) := Player_Ability("(ability_type)", "(Weapon Name)", (min_damage), (max_damage), (accuracy)),
#     (weapon name)_(ability type) := Player_Ability("(ability_type)", "(Weapon Name)", (min_damage), (max_damage), (accuracy)),
#     (weapon name)_(ability type) := Player_Ability("(ability_type)", "(Weapon Name)", (min_damage), (max_damage), (accuracy)),
#     (weapon name)_(ability type) := Player_Ability("(ability_type)", "(Weapon Name)", (min_damage), (max_damage), (accuracy))

# Note: first ability: defensive abilities
# Note: second ability: basic1 attack abilities
# Note: third ability: basic2 abilities
# Note: fourth ability: special attack abilities
# Note: fifth ability: ultimate attack abilities

# Note: defense system: prompting user to enter timing using float()
# Note: defense system: allow player to choose to heal or take some damage while dealing the rest back to enemy(martial_arts_defense, doombringer_defense not included)
# Note: defense system: during boss fights you will negate 45% of the damage, return 5% of the damage, take 50% of the damage instead(doombringer_defense not included)
# Note: ultimates are available only after rounds count is greater than 5, can only be used once per battle

weapons_dict = {
# ---<Test Weapon>---
    test_weapon_weapon = Weapon("Test Weapon",
        idk1 := Player_Ability("nothing", "idk1", 1, 2, 100),
        idk2 := Player_Ability("nothing", "idk2", 1, 2, 90),
        idk3 := Player_Ability("nothing", "idk3", 1, 2, 80),
        idk4 := Player_Ability("nothing", "idk4", 1, 2, 70),
        idk5 := Player_Ability("nothing", "idk5", 1, 2, 60))
# Note: test_weapon is for testing purposes

# ---<Martial Arts>---
    martial_arts_weapon = Weapon("Martial Arts",
        martial_arts_defense := Player_Ability("defense", "Block", 0, 0, 100),
        martial_arts_basic1 := Player_Ability("basic1", "Punch", 2, 5, 100),
        martial_arts_basic2 := Player_Ability("basic2", "Upper Punch", 5, 8, 95),
        martial_arts_special := Player_Ability("special", "Roundhouse Kick", 8, 12, 80),
        martial_arts_ultimate := Player_Ability("ultimate", "Flurry Strike", 17, 17, 100))
# Note: martial_arts_defense will only negate 85% of the damage(rounded)

# ---<Rusty Sword>---
    rusty_sword_weapon = Weapon("Rusty Sword",
        rusty_sword_defense := Player_Ability("defense", "Counter", 0, 0, 100),
        rusty_sword_basic1 := Player_Ability("basic1", "Rusty Slice", 4, 7, 100),
        rusty_sword_basic2 := Player_Ability("basic2", "Upper Slash", 7, 12, 90),
        rusty_sword_special := Player_Ability("special", "Cross Slash", 10, 15, 80),
        rusty_sword_ultimate := Player_Ability("ultimate", "Rust Reaction", 20, 20, 100))
# Note: rusty_sword_defense will do 50% of the enemy damage to enemy(rounded)

# ---<Dual Daggers>---
    dual_daggers_weapon = Weapon("Dual Daggers",
        dual_daggers_defense := Player_Ability("defense", "Deflect", 0, 0, 100),
        dual_daggers_basic1 := Player_Ability("basic1", "Dagger Stab", 8, 10, 100),
        dual_daggers_basic2 := Player_Ability("basic2", "Double Slash", 10, 14, 90),
        dual_daggers_special := Player_Ability("special", "Dagger Throw", 15, 18, 95),
        dual_daggers_ultimate := Player_Ability("ultimate", "Deadly Assault", 30, 30, 100))
# Note: dual_daggers_defense will return 30% of the damage back to enemy(rounded)
# Note: dual_daggers_special will make player lose "dual daggers" weapon

# ---<Katana>---
    katana_weapon = Weapon("Katana",
        katana_defense := Player_Ability("defense", "Parry", 0, 0, 100),
        katana_basic1 := Player_Ability("basic2", "Slash", 10, 14, 100),
        katana_basic2 := Player_Ability("basic2", "Horizontal Arc", 15, 20, 90),
        katana_special := Player_Ability("special", "Fury Cutter", 21, 24, 80),
        katana_ultimate := Player_Ability("ultimate", "Phantom Claws", 45, 45, 100))
# Note: katana_defense will return 20% of the damage back to enemy(rounded), allows player to choose a 40% weaker version of another move(rounded)

# ---<Greatsword>---
    greatsword_weapon = Weapon("Greatsword",
        greatsword_defense := Player_Ability("defense", "Deflect", 0, 0, 100),
        greatsword_basic1 := Player_Ability("basic1", "Great Slash", 16, 19, 95),
        greatsword_basic2 := Player_Ability("basic2", "Horizontal Cutter", 18, 26, 85),
        greatsword_special := Player_Ability("special", "Whirlwind", 30, 35, 90),
        greatsword_ultimate := Player_Ability("ultimate", "Splitting Earth", 60, 60, 100))
# Note: greatsword_defense will return 30% of the damage back to enemy(rounded)
# Note: greatsword_special will have cd of 1 rounds to prevent abuse

# ---<Dragon Slayer>---
    dragon_slayer_weapon = Weapon("Dragon Slayer",
        dragon_slayer_defense := Player_Ability("defense", "Counter", 0, 0, 100),
        dragon_slayer_basic1 := Player_Ability("basic1", "Dragon Bite", 27, 35, 100),
        dragon_slayer_basic2 := Player_Ability("basic2", "Fire Breath", 35, 45, 95),
        dragon_slayer_special := Player_Ability("special", "Dragon's Rage", 90, 100, 70),
        dragon_slayer_ultimate := Player_Ability("ultimate", "Dragons Assemble!", 150, 150, 100))
# Note: dragon_slayer_defense will do 50% of the enemy damage to enemy

# ---<Reaper's Blade>---
    reapers_blade_weapon = Weapon("Reaper's Blade",
        reapers_blade_defense := Player_Ability("defense", "Absolute Defense", 0, 0, 100),
        reapers_blade_basic1 := Player_Ability("basic1", "Silent Moon", 10000, 10000, 100),
        reapers_blade_basic2 := Player_Ability("basic2", "Deadly Cresent", 10000, 10000, 100),
        reapers_blade_special := Player_Ability("special", "Gate of Death", 10000, 10000, 100),
        reapers_blade_ultimate := Player_Ability("ultimate", "The Void", 999999, 999999, 100))
# Note: Dev-Only weapon, for testing purposes, and meant to destroy everything
# Note: reaper_blade_defense will negate all damage
}


# ----------Game Areas----------
# (name, npcs, enemies, items, west, south, east, north)

areas_dict = {
# ---<Starting City>---
    starting_city_city_square := Game_Area("starting_city", "City Square", "The center of Starting City.", [], [], "___", "West Gate", "South Gate", "East Gate", "North Gate"),
    starting_city_west_gate := Game_Area("starting_city", "West Gate", "The western gate of Starting City.", [], [], "___", "None", "Knight Quarters", "City Square", "None"),
    starting_city_south_gate := Game_Area("starting_city", "South Gate", "The southern gate of Starting CIty.", [], [], "___", "City Teleporter", "None", "None", "City Square"),
    starting_city_east_gate := Game_Area("starting_city", "East Gate", "The eastern gate of Starting City.", [], [], "___", "City Square", "City Smithy", "None", "None"),
    starting_city_north_gate := Game_Area("starting_city", "North Gate", "The northern gate of Starting City.", [], [], "___", "None", "City Square", "Town Hall", "None"),
    starting_city_town_hall := Game_Area("starting_city", "Town Hall", "", [], [], "___", "North Gate", "None", "None", "None"),
    starting_city_knight_quarters := Game_Area("starting_city", "Knight Quarters", "", [], [], "___", "None", "None", "None", "West Gate"),
    starting_city_city_smithy := Game_Area("starting_city", "City Smithy", "", [], [], "___", "None", "None", "None", "East Gate"),
    starting_city_city_teleporter := Game_Area("starting_city", "City Teleporter", "", [], [], "___", "None", "None", "South Gate", "None"),

# ---<Scorching Desert>---
    scorching_desert_barren_lands := Game_Area("scorching_desert", "Barren Lands", "", [], [], "___", "", "", "", ""),
    scorching_desert_scorching_desert1 := Game_Area("scorching_desert", "Scorching Desert-1", "", [], [], "___", "", "", "", ""),
    scorching_desert_scorching_desert2 := Game_Area("scorching_desert", "Scorching Desert-2", "", [], [], "___", "", "", "", ""),
    scorching_desert_scorching_desert3 := Game_Area("scorching_desert", "Scorching Desert-3", "", [], [], "___", "", "", "", ""),
    scorching_desert_desert_oasis := Game_Area("scorching_desert", "Desert Oasis", "", [], [], "___", "", "", "", ""),
    scorching_desert_oasis_lakeside := Game_Area("scorching_desert", "Oasis Lakeside", "", [], [], "___", "", "", "", ""),
    scorching_desert_crimson_canyon := Game_Area("scorching_desert", "Crimson Canyon", "", [], [], "___", "", "", "", ""),
    scorching_desert_hidden_cave := Game_Area("scorching_desert", "Hidden Cave", "", [], [], "___", "", "", "", ""),

# ---<Desert Temple (Dungeon)>---
    desert_temple_temple_entrance := Game_Area("desert_temple", "Temple Entrance", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_hallways1 := Game_Area("desert_temple", "Temple Hallways-1", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_storeroom1 := Game_Area("desert_temple", "Temple Storeroom-1", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_stairs := Game_Area("desert_temple", "Temple Stairs", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_hallways2 := Game_Area("desert_temple", "Temple Hallways-2", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_storeroom2 := Game_Area("desert_temple", "Temple Storeroom-2", "", [], [], "___", "", "", "", ""),
    desert_temple_heavy_doors := Game_Area("desert_temple", "Heavy Doors", "", [], [], "___", "", "", "", ""),
    desert_temple_temple_hallways3 := Game_Area("desert_temple", "Temple Hallways-3", "", [], [], "___", "", "", "", ""),
    desert_temple_grand_chamber := Game_Area("desert_temple", "Grand Chamber", "", [], [], "___", "", "", "", ""),
    desert_temple_treasure_room := Game_Area("desert_temple", "Treasure Room", "", [], [], "___", "", "", "", ""),
    desert_temple_exit_teleporter := Game_Area("desert_temple", "Exit Teleporter", "", [], [], "___", "", "", "", ""),

} 

# -------------------------Test Game-------------------------
def game_start():
    global current_area
    global player_character
    active = True

    current_area = starting_city_city_square

    player_name = input("Hello player! What is your name?>> " + "\n")




def prompt_player():
    active = True

    while active:
        player_input = input("What do you want to do?>> " + "\n").lower()
        print("---<Processing...>--- \n")
        sleep(delay)

        if player_input.strip():
            active = False
            return player_input
        else:
            print("---<Input Cannot Be Blank>--- \n")
        


def player_command(player_input):
    global current_area
    global last_interaction

    #if "go" in player_input:


    if "look" in player_input:
        print(current_area)

        if "teleporter" in current_area.name.lower():
            print("---<'interact' With the Teleporter to Use It>--- \n")

    #elif "interact" in player_input:


    elif "mystats" in player_input:
        print(player_character)

    elif "help" in player_input:
        print(game_cmds)
