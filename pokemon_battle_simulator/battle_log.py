class BattleLog:
    """Handles logging battle events to a file."""

    LOG_FILE = "battle_log.txt"

    @staticmethod
    def log(message):
        """
        Logs a battle event to the log file.

        :param message: str - The message to log
        """
        with open(BattleLog.LOG_FILE, "a", encoding="utf-8") as file:  # Added encoding="utf-8"
            file.write(message + "\n")

    @staticmethod
    def display_log():
        """Displays the battle log."""
        try:
            with open(BattleLog.LOG_FILE, "r", encoding="utf-8") as file:  # Added encoding="utf-8"
                print("\n📜 Battle Log 📜")
                print(file.read())
        except FileNotFoundError:
            print("No battle log found.")
