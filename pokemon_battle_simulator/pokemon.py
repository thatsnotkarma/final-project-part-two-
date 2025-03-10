class Pokemon:
    def __init__(self, name, hp, attack, defense, element, moves):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.moves = moves  # This will be a list of move names

    def type_effectiveness(self, opponent):
        """Returns a multiplier based on the type effectiveness."""
        type_chart = {
            ("Fire", "Grass"): 2,
            ("Water", "Fire"): 2,
            ("Grass", "Water"): 2,
            ("Electric", "Water"): 2,
            # Other type combinations can be added here
        }

        # Check if the move's type has an advantage
        multiplier = type_chart.get((self.element, opponent.element), 1)
        return multiplier

    def use_move(self, move_name, opponent):
        """Calculates and applies damage from the Pokémon's move."""
        # Dictionary for moves and their power
        move_powers = {
            "Thunderbolt": 40,
            "Quick Attack": 20,
            "Electro Ball": 50,
            "Water Gun": 30,
            "Bubble": 20,
            "Hydro Pump": 60,
            "Vine Whip": 35,
            "Tackle": 15,
            "Razor Leaf": 45,
            "Ember": 40,
            "Scratch": 15,
            "Flamethrower": 60,
            "Gust": 35,
            "Hyper Fang": 50,
            "Bite": 40,
        }

        if move_name not in move_powers:
            print(f"{move_name} is not a valid move!")
            return

        move_power = move_powers[move_name]
        type_multiplier = self.type_effectiveness(opponent)

        # Apply the type advantage
        damage = (move_power * self.attack * type_multiplier) // (opponent.defense + 1)
        opponent.hp -= damage

        print(f"{self.name} uses {move_name}! {opponent.name} takes {damage} damage.")
        if opponent.hp < 0:
            opponent.hp = 0
        opponent.display_stats()

    def is_fainted(self):
        """Check if the Pokémon has fainted (HP <= 0)."""
        return self.hp <= 0

    def display_stats(self):
        """Display the current stats of the Pokémon."""
        print(f"{self.name} | HP: {self.hp} | Type: {self.element}")
