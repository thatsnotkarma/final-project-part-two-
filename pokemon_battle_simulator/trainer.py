from pokemon import Pokemon


class Trainer:
    """Represents a Pokémon trainer with a team of Pokémon."""

    def __init__(self, name):
        """
        Initializes a Trainer.

        :param name: str - The trainer's name
        """
        self.name = name
        self.pokemon_team = []  # List of Pokémon
        self.active_pokemon = None  # Pokémon currently in battle

    def add_pokemon(self, pokemon):
        """
        Adds a Pokémon to the trainer's team.

        :param pokemon: Pokemon - The Pokémon to add
        """
        self.pokemon_team.append(pokemon)
        if len(self.pokemon_team) == 1:
            self.active_pokemon = pokemon  # Set first Pokémon as active

    def switch_pokemon(self):
        """
        Switches to the next available Pokémon if the current one faints.
        """
        for pokemon in self.pokemon_team:
            if pokemon.hp > 0:
                self.active_pokemon = pokemon
                print(f"{self.name} switched to {pokemon.name}!")
                return
        print(f"{self.name} has no Pokémon left! {self.name} loses the battle.")
        self.active_pokemon = None  # No Pokémon left means game over

    def __str__(self):
        """
        Returns a string representation of the Trainer and their Pokémon team.
        """
        team_status = "\n".join([str(pokemon) for pokemon in self.pokemon_team])
        return f"Trainer: {self.name}\nActive Pokémon: {self.active_pokemon.name if self.active_pokemon else 'None'}\nTeam:\n{team_status}"
