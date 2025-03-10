import unittest
from pokemon import Pokemon
from trainer import Trainer
from battle_log import BattleLog


class TestPokemonBattle(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Create test Pokémon
        self.pikachu = Pokemon("Pikachu", 100, 50, 30, "Electric", [])
        self.squirtle = Pokemon("Squirtle", 100, 40, 35, "Water", [])
        self.bulbasaur = Pokemon("Bulbasaur", 100, 40, 40, "Grass", [])

        # Add moves to Pokémon
        self.pikachu.moves = ["Thunderbolt", "Quick Attack"]
        self.squirtle.moves = ["Water Gun", "Bubble"]
        self.bulbasaur.moves = ["Vine Whip", "Tackle"]

        # Create trainers
        self.ash = Trainer("Ash")
        self.misty = Trainer("Misty")

        # Add Pokémon to trainers
        self.ash.add_pokemon(self.pikachu)
        self.ash.add_pokemon(self.bulbasaur)
        self.misty.add_pokemon(self.squirtle)

        # Set active Pokémon
        self.ash.set_active_pokemon(self.pikachu)
        self.misty.set_active_pokemon(self.squirtle)

    def test_attack_damage(self):
        """Test the attack damage calculation."""
        # Pikachu attacks Squirtle with Thunderbolt
        self.pikachu.use_move("Thunderbolt", self.squirtle)
        self.assertTrue(self.squirtle.hp < 100, "Squirtle should take damage from Thunderbolt.")

        # Squirtle attacks Pikachu with Water Gun
        self.squirtle.use_move("Water Gun", self.pikachu)
        self.assertTrue(self.pikachu.hp < 100, "Pikachu should take damage from Water Gun.")

    def test_type_advantage(self):
        """Test type effectiveness between Electric and Water."""
        # Pikachu attacks Squirtle with Thunderbolt (Electric vs Water)
        initial_hp = self.squirtle.hp
        self.pikachu.use_move("Thunderbolt", self.squirtle)
        self.assertTrue(self.squirtle.hp < initial_hp, "Thunderbolt should do extra damage to Water-type Pokémon.")

    def test_pokemon_fainting(self):
        """Test if Pokémon faint when their HP reaches 0."""
        # Squirtle attacks Pikachu until fainted
        while self.pikachu.hp > 0:
            self.squirtle.use_move("Water Gun", self.pikachu)

        self.assertTrue(self.pikachu.is_fainted(), "Pikachu should faint after enough damage.")

    def test_switch_pokemon(self):
        """Test Pokémon switching functionality."""
        self.ash.switch_pokemon()
        self.assertEqual(self.ash.active_pokemon.name, "Bulbasaur", "Ash should have switched to Bulbasaur.")

        self.misty.switch_pokemon()
        self.assertEqual(self.misty.active_pokemon.name, "Squirtle", "Misty should still have Squirtle active.")

    def test_battle_log(self):
        """Test if the battle log records the actions."""
        BattleLog.log("Test log entry")
        with open(BattleLog.LOG_FILE, "r", encoding="utf-8") as log_file:
            log_contents = log_file.read()

        self.assertIn("Test log entry", log_contents, "Battle log should contain the test log entry.")

    def tearDown(self):
        """Clean up after tests."""
        # Clear the battle log after each test
        open(BattleLog.LOG_FILE, "w", encoding="utf-8").close()


if __name__ == "__main__":
    unittest.main()
