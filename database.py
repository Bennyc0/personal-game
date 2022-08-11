# -------------------------Data Base-------------------------
# ----------Obtainable Things----------
ingame_weapons = ["martial arts", "rusty sword", "dual daggers", "katana", "greatsword", "dragon slayer"]
ingame_items = ["letter", "key", "certificate", "salmon"]

dev_weapons = ["doombringer"]
# ----------Player Abilities---------
# Note: first ability: defensive abilities, ability_id = (weapon name)_defense3
# Note: second ability: basic1 attack abilities, ability_id = (weapon name)_basic1
# Note: third ability: basic2 abilities, ability_id = (weapon name)_basic2
# Note: fourth ability: special attack abilities, ability_id = (weapon name)_special
# Note: fifth ability: ultimate attack abilities, ability_id = (weapon name)_ultimate

# Note: defense system: prompting user to enter timing using float()
# Note: defense system: allow player to choose to heal or take some damage while dealing the rest back to enemy(martial_arts_defense, doombringer_defense not included)
# Note: defense system: during boss fights you will negate 45% of the damage, return 5% of the damage, take 50% of the damage instead(doombringer_defense not included)
# Note: ultimates are available only after rounds count is greater than 5, can only be used once per battle

# ---<martial arts>---

# Note: martial_arts_defense will only negate 85% of the damage(rounded)
martial_arts_defense = Player_Ability("martial_arts_defense", "defense", "Block", 0, 0, 100)
martial_arts_basic1 = Player_Ability("martial_arts_basic1", "basic1", "Punch", 2, 5, 100)
martial_arts_basic2 = Player_Ability("martial_arts_basic2", "basic2", "Upper Punch", 5, 8, 95)
martial_arts_special = Player_Ability("martial_arts_special", "special", "Roundhouse Kick", 8, 12, 80)
martial_arts_ultimate = Player_Ability("martial_arts_ultimate", "ultimate", "Flurry Strike", 17, 17, 100)

# ---<rusty sword>---
rusty_sword_defense = Player_Ability("rusty_sword_defense", "defense", "Counter", 0, 0, 100)
rusty_sword_basic1 = Player_Ability("rusty_sword_basic1", "basic1", "Rusty Slice", 4, 7, 100)
rusty_sword_basic2 = Player_Ability("rusty_sword_basic2", "basic2", "Upper Slash", 7, 12, 90)
rusty_sword_special = Player_Ability("rusty_sword_special", "special", "Cross Slash", 10, 15, 80)
rusty_sword_ultimate = Player_Ability("rusty_sword_ultimate", "ultimate", "Rust Reaction", 20, 20, 100)
# Note: rusty_sword_defense will do 50% of the enemy damage to enemy(rounded)

# ---<dual daggers>---
dual_daggers_defense = Player_Ability("dual_daggers_defense", "defense", "Deflect", 0, 0, 100)
dual_daggers_basic1 = Player_Ability("dual_daggers_basic1", "basic1", "Dagger Stab", 8, 10, 100)
dual_daggers_basic2 = Player_Ability("dual_daggers_basic2", "basic2", "Double Slash", 10, 14, 90)
dual_daggers_special = Player_Ability("dual_daggers_special", "special", "Dagger Throw", 15, 18, 95)
dual_daggers_ultimate = Player_Ability("dual_daggers_ultimate", "ultimate", "Deadly Assault", 30, 30, 100)
# Note: dual_daggers_defense will return 30% of the damage back to enemy(rounded)
# Note: dual_daggers_special will make player lose "dual daggers" weapon

# ---<katana>---
katana_defense = Player_Ability("katana_defense", "defense", "Parry", 0, 0, 100)
katana_basic1 = Player_Ability("katana_basic1", "basic2", "Slash", 10, 14, 100)
katana_basic2 = Player_Ability("katana_basic2", "basic2", "Horizontal Arc", 15, 20, 90)
katana_special = Player_Ability("katana_special", "special", "Fury Cutter", 21, 24, 80)
katana_ultimate = Player_Ability("katana_ultimate", "ultimate", "Phantom Claws", 45, 45, 100)
# Note: katana_defense will return 20% of the damage back to enemy(rounded), allows player to choose a 40% weaker version of another move(rounded)

# ---<greatsword>---
greatsword_defense = Player_Ability("greatsword_defense", "defense", "Deflect", 0, 0, 100)
greatsword_basic1 = Player_Ability("greatsword_basic1", "basic1", "Great Slash", 16, 19, 95)
greatsword_basic2 = Player_Ability("greatsword_basic2", "basic2", "Horizontal Cutter", 18, 26, 85)
greatsword_special = Player_Ability("greatsword_special", "special", "Whirlwind", 30, 35, 90)
greatsword_ultimate = Player_Ability("greatsword_ultimate", "ultimate", "Splitting Earth", 60, 60, 100)
# Note: greatsword_defense will return 30% of the damage back to enemy(rounded)
# Note: greatsword_special will have cd of 1 rounds to prevent abuse

# ---<dragon slayer>---
dragon_slayer_defense = Player_Ability("dragon_slayer_defense", "defense", "Counter", 0, 0, 100)
dragon_slayer_basic1 = Player_Ability("dragon_slayer_basic1", "basic1", "Dragon Bite", 27, 35, 100)
dragon_slayer_basic2 = Player_Ability("dragon_slayer_basic2", "basic2", "Fire Breath", 35, 45, 95)
dragon_slayer_special = Player_Ability("dragon_slayer_special", "special", "Dragon's Rage", 90, 100, 70)
dragon_slayer_ultimate = Player_Ability("dragon_slayer_ultimate", "ultimate", "Dragons Assemble!", 150, 150, 100)
# Note: dragon_slayer_defense will do 50% of the enemy damage to enemy

# ---<doombringer>---
doombringer_defense = Player_Ability("doombringer_defense", "defense", "Absolute Defense", 0, 0, 100)
doombringer_basic1 = Player_Ability("doombringer_basic1", "basic1", "Dead Silence", 10000, 10000, 100)
doombringer_basic2 = Player_Ability("doombringer_basic2", "basic2", "Final Punishment", 10000, 10000, 100)
doombringer_special = Player_Ability("doombringer_special", "special", "GG", 10000, 10000, 100)
doombringer_ultimate = Player_Ability("doombringer_ultimate", "ultimate", "Ragnarok", 999999, 999999, 100)
# Note: Dev-Only weapon, for testing purposes, and meant to destroy everything
# Note: doombringer_defense will negate all damage
