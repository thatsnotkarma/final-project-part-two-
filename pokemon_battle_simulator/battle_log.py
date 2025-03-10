class BattleLog:
    LOG_FILE = "battle_log.txt"

    @staticmethod
    def log(pokemon, move_name, opponent, damage, fainted=False):
        """Log the battle action with detailed info."""
        log_entry = f"{pokemon.name} uses {move_name} on {opponent.name} causing {damage} damage."
        if fainted:
            log_entry += f" {opponent.name} has fainted!"
        with open(BattleLog.LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(log_entry + "\n")

    @staticmethod
    def log_battle_start(trainer1, trainer2):
        """Log the start of the battle."""
        log_entry = f"🔥 {trainer1.name} vs {trainer2.name}! Battle Start! 🔥"
        with open(BattleLog.LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(log_entry + "\n")

    @staticmethod
    def display_log():
        """Display the battle log."""
        with open(BattleLog.LOG_FILE, "r", encoding="utf-8") as log_file:
            print(log_file.read())
