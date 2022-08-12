teleport_options = []

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


areas_dict = {
# ---<Starting City>---
    starting_city_city_square := Game_Area("starting_city", "City Square", "The center of Starting City.", [], [], "___", "West Gate", "South Gate", "East Gate", "North Gate"),
    starting_city_west_gate := Game_Area("starting_city", "West Gate", "The western gate of Starting City.", [], [], "___", "None", "Knight Quarters", "City Square", "City Bank"),
    starting_city_south_gate := Game_Area("starting_city", "South Gate", "The southern gate of Starting CIty.", [], [], "___", "Starting City Teleporter", "None", "None", "City Square"),
    starting_city_east_gate := Game_Area("starting_city", "East Gate", "The eastern gate of Starting City.", [], [], "___", "City Square", "City Smithy", "None", "None"),
    starting_city_north_gate := Game_Area("starting_city", "North Gate", "The northern gate of Starting City.", [], [], "___", "None", "City Square", "Town Hall", "None"),
    starting_city_town_hall := Game_Area("starting_city", "Town Hall", "", [], [], "___", "North Gate", "None", "None", "None"),
    starting_city_knight_quarters := Game_Area("starting_city", "Knight Quarters", "", [], [], "___", "None", "None", "None", "West Gate"),
    starting_city_city_smithy := Game_Area("starting_city", "City Smithy", "", [], [], "___", "None", "None", "None", "East Gate"),
    starting_city_teleporter := Game_Area("starting_city", "Starting City Teleporter", "", [], [], "___", "None", "None", "South Gate", "None"),
    starting_city_city_bank := Game_Area("starting_city", "City Bank", "", [], [], "___", "None", "West Gate", "None", "None"),

# ---<Scorching Desert>---
    scorching_desert_barren_lands := Game_Area("scorching_desert", "Barren Lands", "", [], [], "___", "None", "Scorching Desert-1", "None", "South Gate"),
    scorching_desert_scorching_desert1 := Game_Area("scorching_desert", "Scorching Desert-1", "", [], [], "___", "Desert Oasis", "Scorching Desert-2", "Crimson Canyon", "Barren Lands"),
    scorching_desert_scorching_desert2 := Game_Area("scorching_desert", "Scorching Desert-2", "", [], [], "___", "Temple Entrance", "None", "None", "Scorching Desert-1"),
    scorching_desert_desert_oasis := Game_Area("scorching_desert", "Desert Oasis", "", [], [], "___", "None", "None", "Scorching Desert-1", "Oasis Lakeside"),
    scorching_desert_oasis_lakeside := Game_Area("scorching_desert", "Oasis Lakeside", "", [], [], "___", "None", "Desert Oasis", "None", "None"),
    scorching_desert_crimson_canyon := Game_Area("scorching_desert", "Crimson Canyon", "", [], [], "___", "Scorching Desert-1", "None", "Northern Road", "None"),
    scorching_desert_hidden_cave := Game_Area("scorching_desert", "Hidden Cave", "", [], [], "___", "None", "None", "None", "Crimson Canyon"),    
    # Note: scorching_desert_hidden_cave will not show on scorching_desert_crimson_canyon's paths, its hidden

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

# ---<Desert Town>---
    desert_town_town_square := Game_Area("desert_town", "Town Square", "", [], [], "___", "Western Road", "Southern Road", "Eastern Road", "Northern Road"),
    desert_town_western_road := Game_Area("desert_town", "Western Road", "", [], [], "___", "None", "Town Smithy", "Town Square", "Town Stores"),
    desert_town_southern_road := Game_Area("desert_town", "Southern Road", "", [], [], "___", "Town Warehouse", "WIP", "Desert Town Teleporter", "Town Square"),
    desert_town_eastern_road := Game_Area("desert_town", "Eastern Road", "", [], [], "___", "Town Square", "None", "WIP", "Town Bank"),
    desert_town_northern_road := Game_Area("desert_town", "Northern Road", "", [], [], "___", "Crimson Canyon", "Town Square", "None", "None"),
    desert_town_town_stores := Game_Area("desert_town", "Town Stores", "", [], [], "___", "None", "Western Road", "None", "None"),
    desert_town_town_smithy := Game_Area("desert_town", "Town Smithy", "", [], [], "___", "None", "None", "None", "Western Road"),
    desert_town_teleporter := Game_Area("desert_town", "Desert Town Teleporter", "", [], [], "___", "Southern Road", "None", "None", "None"),
    desert_town_town_warehouse := Game_Area("desert_town", "Town Warehouse", "", [], [], "___", "None", "None", "Southern Road", "None"),
    desert_town_town_bank := Game_Area("desert_town", "Town Bank", "", [], [], "___", "None", "Eastern Road", "None", "None"),

# --<Redwood Forest>---
#:= Game_Area("scorching_desert", "Crimson Canyon", "", [], [], "___", "", "", "", ""),

}


current_area = desert_temple_exit_teleporter
print(current_area)

if "exit" in current_area.name.lower():
    for entrance in areas_dict:
        if "entrance" in entrance.name.lower() and entrance.sector == current_area.sector:
            current_area = entrance

print(current_area)

