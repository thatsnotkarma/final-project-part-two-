class BattleLog:
    LOG_FILE = "battle_log.txt"

    @staticmethod
    def log(message):
        """Log the message to a log file."""
        with open(BattleLog.LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")

    @staticmethod
    def display_log():
        """Display the battle log."""
        with open(BattleLog.LOG_FILE, "r", encoding="utf-8") as log_file:
            print(log_file.read())
