class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_team = []
        self.active_pokemon = None

    def add_pokemon(self, pokemon):
        self.pokemon_team.append(pokemon)

    def set_active_pokemon(self, pokemon):
        self.active_pokemon = pokemon

    def switch_pokemon(self):
        print(f"{self.name} is switching Pokémon!")
        available_pokemon = [pokemon for pokemon in self.pokemon_team if pokemon != self.active_pokemon and pokemon.hp > 0]
        if not available_pokemon:
            print(f"{self.name} has no available Pokémon!")
            return
        print("Available Pokémon:")
        for i, pokemon in enumerate(available_pokemon):
            print(f"{i + 1}. {pokemon.name}")
        choice = int(input("Choose a Pokémon to switch to: ")) - 1
        if 0 <= choice < len(available_pokemon):
            self.set_active_pokemon(available_pokemon[choice])
            print(f"{self.name} switched to {self.active_pokemon.name}!")
        else:
            print("Invalid choice!")
