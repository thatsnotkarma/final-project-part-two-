class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.selected_team = []
        self.active_pokemon = None

    def add_pokemon(self, pokemon):
        """Add a Pokémon to the trainer's team."""
        self.pokemon_team.append(pokemon)

    def set_active_pokemon(self, pokemon):
        """Set the active Pokémon for the trainer."""
        self.active_pokemon = pokemon

    def switch_pokemon(self):
        """Switch the active Pokémon with another Pokémon from the selected team."""
        print(f"{self.name}, choose a Pokémon to switch to:")
        available_pokemon = [pokemon for pokemon in self.selected_team if not pokemon.is_fainted()]

        if not available_pokemon:
            print("All your Pokémon have fainted! You cannot switch.")
            return  # End the switch attempt if all Pokémon are fainted

        for i, pokemon in enumerate(available_pokemon, 1):
            print(f"{i}. {pokemon.name}")

        choice = int(input("Enter the number of the Pokémon you want to switch to: "))
        self.set_active_pokemon(available_pokemon[choice - 1])
