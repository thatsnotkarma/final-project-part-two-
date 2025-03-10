from pokemon import Pokemon
from trainer import Trainer
from battle_log import BattleLog

def run_battle(trainer1, trainer2):
    """Handles turn-based Pokémon battles between two trainers."""
    open(BattleLog.LOG_FILE, "w", encoding="utf-8").close()  # Clear log at start
    print(f"\n🔥 {trainer1.name} vs {trainer2.name}! Battle Start! 🔥")
    BattleLog.log(f"\n🔥 {trainer1.name} vs {trainer2.name}! Battle Start! 🔥")

    while True:
        # Trainer 1's turn
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
                BattleLog.log(f"{trainer1.active_pokemon.name} attacks {trainer2.active_pokemon.name} with {move_choice}!")
            elif choice == "2":
                trainer1.switch_pokemon()

            if trainer2.active_pokemon.is_fainted():
                trainer2.switch_pokemon()
                if trainer2.active_pokemon is None:
                    print(f"\n🏆 {trainer1.name} wins the battle! 🏆")
                    BattleLog.log(f"\n🏆 {trainer1.name} wins the battle! 🏆")
                    break

        # Trainer 2's turn
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
                BattleLog.log(f"{trainer2.active_pokemon.name} attacks {trainer1.active_pokemon.name} with {move_choice}!")
            elif choice == "2":
                trainer2.switch_pokemon()

            if trainer1.active_pokemon.is_fainted():
                trainer1.switch_pokemon()
                if trainer1.active_pokemon is None:
                    print(f"\n🏆 {trainer2.name} wins the battle! 🏆")
                    BattleLog.log(f"\n🏆 {trainer2.name} wins the battle! 🏆")
                    break

    BattleLog.display_log()  # Show the battle log at the end


# Example initialization
if __name__ == "__main__":
    ash = Trainer("Ash")
    misty = Trainer("Misty")

    # Adding example Pokémon
    pikachu = Pokemon("Pikachu", 100, 50, 30, "Electric", ["Thunderbolt", "Quick Attack", "Electro Ball"])
    squirtle = Pokemon("Squirtle", 100, 40, 35, "Water", ["Water Gun", "Bubble", "Hydro Pump"])
    bulbasaur = Pokemon("Bulbasaur", 100, 40, 40, "Grass", ["Vine Whip", "Tackle", "Razor Leaf"])
    charmander = Pokemon("Charmander", 100, 45, 30, "Fire", ["Ember", "Scratch", "Flamethrower"])
    pidgey = Pokemon("Pidgey", 100, 40, 30, "Flying", ["Gust", "Tackle", "Quick Attack"])
    rattata = Pokemon("Rattata", 100, 30, 25, "Normal", ["Quick Attack", "Hyper Fang", "Bite"])

    # Add Pokémon to trainers
    ash.add_pokemon(pikachu)
    ash.add_pokemon(charmander)
    ash.add_pokemon(pidgey)
    misty.add_pokemon(squirtle)
    misty.add_pokemon(bulbasaur)
    misty.add_pokemon(rattata)

    # Set active Pokémon
    ash.set_active_pokemon(pikachu)
    misty.set_active_pokemon(squirtle)

    # Run the battle
    run_battle(ash, misty)
