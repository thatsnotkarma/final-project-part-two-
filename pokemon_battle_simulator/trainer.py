class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.active_pokemon = None

    def add_pokemon(self, pokemon):
        """Add a Pokémon to the trainer's team."""
        self.pokemon_team.append(pokemon)

    def set_active_pokemon(self, pokemon):
        """Set the active Pokémon for the trainer."""
        self.active_pokemon = pokemon

    def switch_pokemon(self):
        """Switch the active Pokémon with another Pokémon from the team."""
        print(f"{self.name}, choose a Pokémon to switch to:")
        available_pokemon = [pokemon for pokemon in self.pokemon_team if not pokemon.is_fainted()]

        if not available_pokemon:
            print("All your Pokémon have fainted! You cannot switch.")
            return  # End the switch attempt if all Pokémon are fainted

        for i, pokemon in enumerate(available_pokemon, 1):
            print(f"{i}. {pokemon.name}")

        choice = input("Choose a Pokémon (1, 2, 3, ...): ")

        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(available_pokemon):
            print("Invalid choice! Please choose a valid number.")
            choice = input("Choose a Pokémon (1, 2, 3, ...): ")

        # Set the new active Pokémon to the selected one
        self.active_pokemon = available_pokemon[int(choice) - 1]
        print(f"{self.name} switched to {self.active_pokemon.name}!")
