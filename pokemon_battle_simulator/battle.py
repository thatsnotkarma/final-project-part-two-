import random
from pokemon import Pokemon
from battle_log import BattleLog
from trainer import Trainer

def run_battle(trainer1, trainer2):
    """Handles turn-based Pokémon battles between two trainers."""
    open(BattleLog.LOG_FILE, "w", encoding="utf-8").close()  # Clear log at start
    BattleLog.log_battle_start(trainer1, trainer2)  # Log battle start

    # Ask each trainer to select 3 Pokémon for battle
    def select_pokemon_for_battle(trainer):
        print(f"\n{trainer.name}, choose 3 Pokémon for the battle:")
        for i, pokemon in enumerate(trainer.pokemon_team, 1):
            print(f"{i}. {pokemon.name}")

        # Get 3 unique selections
        selected_pokemon = []
        while len(selected_pokemon) < 3:
            choice = int(input("Enter the number of the Pokémon you want to select (1-6): "))
            if choice < 1 or choice > 6:
                print("Invalid choice! Please choose a number between 1 and 6.")
                continue  # Skip this iteration if invalid input
            if trainer.pokemon_team[choice - 1] not in selected_pokemon:
                selected_pokemon.append(trainer.pokemon_team[choice - 1])
            else:
                print("You've already selected that Pokémon!")
        trainer.selected_team = selected_pokemon
        trainer.set_active_pokemon(trainer.selected_team[0])

    select_pokemon_for_battle(trainer1)
    select_pokemon_for_battle(trainer2)

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
            # Display current Pokémon and their health
            print(f"\n{trainer1.name}'s turn!")
            print(f"Active Pokémon: {trainer1.active_pokemon.name} | HP: {trainer1.active_pokemon.hp}")
            choice = input("Choose your action (1: Attack, 2: Switch Pokémon): ")

            while choice not in ["1", "2"]:
                print("Invalid choice! Please choose 1 for Attack or 2 for Switch Pokémon.")
                choice = input("Choose your action (1: Attack, 2: Switch Pokémon): ")

            if choice == "1":
                move_choice = input(f"Choose a move: {trainer1.active_pokemon.moves} ")
                trainer1.active_pokemon.use_move(move_choice, trainer2.active_pokemon)
            elif choice == "2":
                trainer1.switch_pokemon()

            # Handle fainting after trainer 1's turn
            if trainer2.active_pokemon.is_fainted():
                trainer2.switch_pokemon()

        # ------------------ Trainer 2's Turn ------------------
        if trainer2.active_pokemon.hp > 0:
            # Display current Pokémon and their health
            print(f"\n{trainer2.name}'s turn!")
            print(f"Active Pokémon: {trainer2.active_pokemon.name} | HP: {trainer2.active_pokemon.hp}")
            choice = input("Choose your action (1: Attack, 2: Switch Pokémon): ")

            while choice not in ["1", "2"]:
                print("Invalid choice! Please choose 1 for Attack or 2 for Switch Pokémon.")
                choice = input("Choose your action (1: Attack, 2: Switch Pokémon): ")

            if choice == "1":
                move_choice = input(f"Choose a move: {trainer2.active_pokemon.moves} ")
                trainer2.active_pokemon.use_move(move_choice, trainer1.active_pokemon)
            elif choice == "2":
                trainer2.switch_pokemon()

            # Handle fainting after trainer 2's turn
            if trainer1.active_pokemon.is_fainted():
                trainer1.switch_pokemon()

    # Display the battle result
    if trainer1.active_pokemon and not trainer1.active_pokemon.is_fainted():
        print(f"\n🏆 {trainer1.name} wins the battle! 🏆")
    else:
        print(f"\n🏆 {trainer2.name} wins the battle! 🏆")


if __name__ == "__main__":
    # Ash's pokemon
    pikachu = Pokemon("Pikachu", 80, 55, 40, "Electric", ["Thunderbolt", "Quick Attack", "Iron Tail"])
    charizard = Pokemon("Charizard", 80, 85, 60, "Fire", ["Flamethrower", "Ember", "Scratch"])
    squirtle = Pokemon("Squirtle", 80, 40, 35, "Water", ["Water Gun", "Bubble", "Hydro Pump"])
    bulbasaur = Pokemon("Bulbasaur", 80, 50, 45, "Grass", ["Vine Whip", "Razor Leaf", "Tackle"])
    butterfree = Pokemon("Butterfree", 70, 60, 50, "Bug", ["Bite", "Gust", "Tackle"])
    jigglypuff = Pokemon("Jigglypuff", 70, 45, 48, "Fairy", ["Double Slap", "Pound", "Play Rough"])

    # Misty’s Pokémon (different from Ash)
    starmie = Pokemon("Starmie", 80, 70, 60, "Water", ["Hydro Pump", "Rapid Spin", "Psychic"])
    psyduck = Pokemon("Psyduck", 70, 50, 45, "Water", ["Water Gun", "Confusion", "Tackle"])
    goldeen = Pokemon("Goldeen", 60, 45, 40, "Water", ["Peck", "Horn Attack", "Waterfall"])
    horsea = Pokemon("Horsea", 60, 45, 40, "Water", ["Bubble", "Tackle", "Hydro Pump"])
    staryu = Pokemon("Staryu", 70, 50, 45, "Water", ["Tackle", "Water Gun", "Bubble"])

    # Create trainers and add Pokémon to their teams
    ash = Trainer("Ash")
    ash.add_pokemon(pikachu)
    ash.add_pokemon(charizard)
    ash.add_pokemon(squirtle)
    ash.add_pokemon(bulbasaur)
    ash.add_pokemon(butterfree)
    ash.add_pokemon(jigglypuff)

    misty = Trainer("Misty")
    misty.add_pokemon(starmie)
    misty.add_pokemon(psyduck)
    misty.add_pokemon(goldeen)
    misty.add_pokemon(horsea)
    misty.add_pokemon(staryu)
    misty.add_pokemon(squirtle)

    # Start the battle
    run_battle(ash, misty)
