class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.active_pokemon = None

    def add_pokemon(self, pokemon):
        if len(self.team) < 6:
            self.team.append(pokemon)
        else:
            print(f"{self.name} already has 6 Pokémon!")

    def set_active_pokemon(self, pokemon):
        if pokemon in self.team and not pokemon.is_fainted():
            self.active_pokemon = pokemon
        else:
            print("Cannot set this Pokémon as active (either not in team or fainted).")

    def switch_pokemon(self):
        available_pokemon = [p for p in self.team if not p.is_fainted() and p != self.active_pokemon]
        if not available_pokemon:
            print(f"{self.name} has no Pokémon left to fight!")
            self.active_pokemon = None  # Signal to battle that trainer has lost
            return None
        else:
            print(f"{self.name}, choose a new Pokémon:")
            for idx, p in enumerate(available_pokemon):
                print(f"{idx + 1}. {p.name} (HP: {p.hp})")
            choice = int(input("Enter the number of the Pokémon you want to switch to: ")) - 1
            self.active_pokemon = available_pokemon[choice]
            print(f"{self.name} switched to {self.active_pokemon.name}!")
