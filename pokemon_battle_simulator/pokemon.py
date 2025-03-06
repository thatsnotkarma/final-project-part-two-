class Pokemon:
    """Represents a Pokémon with a name, HP, and attack power."""

    def __init__(self, name, hp, attack):
        """
        Initializes a Pokémon.

        :param name: str - The Pokémon's name
        :param hp: int - Hit points (health)
        :param attack: int - Attack power
        """
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_pokemon(self, opponent):
        """
        Attacks another Pokémon and reduces its HP.

        :param opponent: Pokemon - The opponent being attacked
        """
        print(f"{self.name} attacks {opponent.name} for {self.attack} damage!")
        opponent.hp -= self.attack
        if opponent.hp <= 0:
            print(f"{opponent.name} has fainted!")
        else:
            print(f"{opponent.name} now has {opponent.hp} HP left.")

    def __str__(self):
        return f"{self.name} - HP: {self.hp}, Attack: {self.attack}"
