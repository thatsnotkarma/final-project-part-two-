class Pokemon:
    def __init__(self, name, hp, attack, defense, element, moves):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.moves = moves

    def display_stats(self):
        """Displays the current stats of the Pokémon."""
        print(f"{self.name}: HP={self.hp}, Attack={self.attack}, Defense={self.defense}, Element={self.element}")

    def is_fainted(self):
        """Checks if the Pokémon has fainted (HP <= 0)."""
        return self.hp <= 0

    def use_move(self, move_name, opponent):
        """Calculates and applies damage from the Pokémon's move."""
        # Simple move power values (these could be more complex based on move types)
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

        # Make sure the move exists
        if move_name not in move_powers:
            print(f"{move_name} is not a valid move!")
            return

        # Get the move power
        move_power = move_powers[move_name]

        # Calculate damage using a simplified formula:
        # Damage = (Move Power * Attack / Defense) - opponent's defense effect
        damage = (move_power * self.attack) // (opponent.defense + 1)  # Avoid division by zero

        # Apply the damage
        opponent.hp -= damage

        # Display the damage dealt
        print(f"{self.name} uses {move_name}! {opponent.name} takes {damage} damage.")
        if opponent.hp < 0:
            opponent.hp = 0
        opponent.display_stats()

    def heal(self, amount):
        """Heals the Pokémon by a specified amount."""
        self.hp += amount
        if self.hp > 100:
            self.hp = 100  # Max HP limit
        print(f"{self.name} heals {amount} HP!")
        self.display_stats()

