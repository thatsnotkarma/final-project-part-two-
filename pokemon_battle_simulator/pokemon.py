class Pokemon:
    def __init__(self, name, hp, attack, defense, element, moves):
        self.name = name
        self.hp = 80  # Set base HP to 80 instead of the original value
        self.attack = attack
        self.defense = defense
        self.element = element
        self.moves = moves  # This will be a list of move names

    def type_effectiveness(self, opponent):
        """Returns a flat bonus damage based on type effectiveness."""
        # Adjusted type chart (added weaknesses that will give +10 damage)
        type_chart = {
            ("Fire", "Grass"): 10,  # Fire is strong against Grass
            ("Water", "Fire"): 10,  # Water is strong against Fire
            ("Grass", "Water"): 10,  # Grass is strong against Water
            ("Electric", "Water"): 10,  # Electric is strong against Water
            # You can add more type advantages here if needed
        }

        # Check if the move's type has an advantage and return bonus damage
        bonus_damage = type_chart.get((self.element, opponent.element), 0)
        return bonus_damage

    def use_move(self, move_name, opponent):
        """Calculates and applies damage from the Pokémon's move."""
        # Dictionary for moves and their base power
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
        type_bonus = self.type_effectiveness(opponent)

        # Check if the move is super effective
        if type_bonus > 0:
            print(f"Super effective! {self.name} uses {move_name}!")

        # Reduce damage formula to avoid one-shots and add type bonus
        damage = (move_power + (self.attack // 2) - (opponent.defense // 2)) + type_bonus

        # Ensure no negative damage
        if damage < 0:
            damage = 0

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
