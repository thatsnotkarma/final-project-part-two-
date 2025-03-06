from pokemon import Pokemon
from trainer import Trainer
from battle_log import BattleLog

def battle(trainer1, trainer2):
    """Handles turn-based Pokémon battles between two trainers."""
    print(f"\n🔥 {trainer1.name} vs {trainer2.name}! Battle Start! 🔥\n")
    BattleLog.log(f"\n🔥 {trainer1.name} vs {trainer2.name}! Battle Start! 🔥")

    while True:
        # Trainer 1 attacks
        if trainer1.active_pokemon.hp > 0:
            trainer1.active_pokemon.attack_pokemon(trainer2.active_pokemon)
            BattleLog.log(f"{trainer1.active_pokemon.name} attacks {trainer2.active_pokemon.name} for {trainer1.active_pokemon.attack} damage!")

        if trainer2.active_pokemon.hp <= 0:
            trainer2.switch_pokemon()
            if trainer2.active_pokemon is None:
                print(f"\n🏆 {trainer1.name} wins the battle! 🏆\n")
                BattleLog.log(f"\n🏆 {trainer1.name} wins the battle! 🏆")
                break

        # Trainer 2 attacks
        if trainer2.active_pokemon.hp > 0:
            trainer2.active_pokemon.attack_pokemon(trainer1.active_pokemon)
            BattleLog.log(f"{trainer2.active_pokemon.name} attacks {trainer1.active_pokemon.name} for {trainer2.active_pokemon.attack} damage!")

        if trainer1.active_pokemon.hp <= 0:
            trainer1.switch_pokemon()
            if trainer1.active_pokemon is None:
                print(f"\n🏆 {trainer2.name} wins the battle! 🏆\n")
                BattleLog.log(f"\n🏆 {trainer2.name} wins the battle! 🏆")
                break

    BattleLog.display_log()  # Show the battle log at the end

# Create Pokémon
pikachu = Pokemon("Pikachu", 35, 10)
charmander = Pokemon("Charmander", 39, 12)
bulbasaur = Pokemon("Bulbasaur", 45, 9)
squirtle = Pokemon("Squirtle", 44, 11)

# Create Trainers
ash = Trainer("Ash")
gary = Trainer("Gary")

# Add Pokémon to Trainers
ash.add_pokemon(pikachu)
ash.add_pokemon(bulbasaur)

gary.add_pokemon(charmander)
gary.add_pokemon(squirtle)

# Start Battle
battle(ash, gary)
