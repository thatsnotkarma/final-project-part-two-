import random
from pokemon import Pokemon
from battle_log import BattleLog
from trainer import Trainer

def run_battle(trainer1, trainer2):
    """Handles turn-based Pokémon battles between two trainers."""
    open(BattleLog.LOG_FILE, "w", encoding="utf-8").close()  # Clear log at start
    BattleLog.log_battle_start(trainer1, trainer2)  # Log battle start

    while True:
        # Check if any trainer has no Pokémon left
        if trainer1.active_pokemon is None or trainer1.active_pokemon.is_fainted():
            print(f"\n🏆 {trainer2.name} wins the battle! 🏆")
            break
        if trainer2.active_pokemon is None or trainer2.active_pokemon.is_fainted():
            print(f"\n🏆 {trainer1.name} wins the battle! 🏆")
            break

        # ------------------ Trainer 1's Turn ------------------
        if trainer1.active_pokemon.hp > 0:
            trainer1.active_pokemon.display_stats()  # Show stats
            print(f"\n{trainer1.name}'s turn! Active Pokémon: {trainer1.active_pokemon.name}")
            print("1. Attack")
            print("2. Switch Pokémon")
            choice = input("Choose your action (1 or 2): ")

            while choice not in ["1", "2"]:
                print("Invalid choice! Please choose 1 for Attack or 2 for Switch Pokémon.")
                choice = input("Choose your action (1 or 2): ")

            if choice == "1":
                print(f"Choose a move: {trainer1.active_pokemon.moves}")
                move_choice = input("Enter move name: ")
                trainer1.active_pokemon.use_move(move_choice, trainer2.active_pokemon)
                BattleLog.log(trainer1.active_pokemon, move_choice, trainer2.active_pokemon, trainer2.active_pokemon.hp)

            elif choice == "2":
                trainer1.switch_pokemon()

            # Handle opponent fainting
            if trainer2.active_pokemon.is_fainted():
                print(f"{trainer2.active_pokemon.name} has fainted!")
                trainer2.switch_pokemon()

        # Check again after Trainer 1's turn
        if trainer1.active_pokemon is None or trainer2.active_pokemon is None:
            continue  # Skip the opponent's turn if one of the Pokémon fainted

        # ------------------ Trainer 2's Turn ------------------
        if trainer2.active_pokemon.hp > 0:
            trainer2.active_pokemon.display_stats()  # Show stats
            print(f"\n{trainer2.name}'s turn! Active Pokémon: {trainer2.active_pokemon.name}")
            print("1. Attack")
            print("2. Switch Pokémon")
            choice = input("Choose your action (1 or 2): ")

            while choice not in ["1", "2"]:
                print("Invalid choice! Please choose 1 for Attack or 2 for Switch Pokémon.")
                choice = input("Choose your action (1 or 2): ")

            if choice == "1":
                print(f"Choose a move: {trainer2.active_pokemon.moves}")
                move_choice = input("Enter move name: ")
                trainer2.active_pokemon.use_move(move_choice, trainer1.active_pokemon)
                BattleLog.log(trainer2.active_pokemon, move_choice, trainer1.active_pokemon, trainer1.active_pokemon.hp)

            elif choice == "2":
                trainer2.switch_pokemon()

            # Handle opponent fainting
            if trainer1.active_pokemon.is_fainted():
                print(f"{trainer1.active_pokemon.name} has fainted!")
                trainer1.switch_pokemon()

        # Final check after Trainer 2's turn
        if trainer1.active_pokemon is None or trainer2.active_pokemon is None:
            continue  # Skip if one of the Pokémon fainted

    # Display the battle result
    print(f"\n🏆 {trainer1.name} wins the battle! 🏆") if trainer1.active_pokemon else print(f"\n🏆 {trainer2.name} wins the battle! 🏆")

    # Display battle log at the end
    BattleLog.display_log()

if __name__ == "__main__":
    # Create Pokémon for both trainers
    pikachu = Pokemon("Pikachu", 35, 55, 40, "Electric", ["Thunderbolt", "Quick Attack", "Iron Tail"])
    charizard = Pokemon("Charizard", 60, 85, 60, "Fire", ["Flamethrower", "Ember", "Scratch"])
    squirtle = Pokemon("Squirtle", 50, 40, 35, "Water", ["Water Gun", "Bubble", "Hydro Pump"])
    bulbasaur = Pokemon("Bulbasaur", 45, 50, 45, "Grass", ["Vine Whip", "Razor Leaf", "Tackle"])

    # Create trainers and add Pokémon to their teams
    ash = Trainer("Ash")
    ash.add_pokemon(pikachu)
    ash.add_pokemon(charizard)
    ash.set_active_pokemon(pikachu)

    misty = Trainer("Misty")
    misty.add_pokemon(squirtle)
    misty.add_pokemon(bulbasaur)
    misty.set_active_pokemon(squirtle)

    # Start the battle
    run_battle(ash, misty)
