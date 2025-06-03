from monster import Monster
from battle_manager import BattleManager

def main():
    print("🎮 Willkommen in der Monster Arena!\n")

    # Einfaches statisches Setup – kann später durch Auswahl ersetzt werden
    player = Monster("Pyron", health=100, attack=20, defense=5)
    enemy = Monster("Schleimi", health=80, attack=15, defense=3)

    battle = BattleManager(player, enemy)
    battle.start_battle()

if __name__ == "__main__":
    main()
