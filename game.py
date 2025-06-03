from monster import Monster
from battle_manager import BattleManager
import random

# Liste verfügbarer Monster für Spieler und Gegner
available_monsters = [
    Monster("Pyron", health=100, attack=20, defense=5),
    Monster("Aqualis", health=90, attack=18, defense=6),
    Monster("Terron", health=110, attack=15, defense=8),
    Monster("Zephyra", health=80, attack=25, defense=3)
]

def choose_monster():
    print("🎮 Willkommen in der Monster Arena!")
    print("\nWähle dein Monster:\n")

    for i, monster in enumerate(available_monsters):
        print(f"{i + 1}. {monster.name} (HP: {monster.health}, ATK: {monster.attack}, DEF: {monster.defense})")

    while True:
        try:
            choice = int(input("\nDeine Wahl (Zahl eingeben): ")) - 1
            if 0 <= choice < len(available_monsters):
                selected = available_monsters[choice]
                print(f"\n✅ Du hast {selected.name} gewählt!\n")
                return selected
            else:
                print("❌ Ungültige Auswahl. Bitte versuche es erneut.")
        except ValueError:
            print("❌ Bitte gib eine gültige Zahl ein.")

def choose_enemy(exclude_monster):
    # Wähle zufälligen Gegner, der nicht identisch ist mit dem Spieler-Monster
    candidates = [m for m in available_monsters if m.name != exclude_monster.name]
    return random.choice(candidates)

def main():
    player = choose_monster()
    enemy = choose_enemy(player)

    print(f"⚔️ Dein Gegner ist {enemy.name}! (HP: {enemy.health}, ATK: {enemy.attack}, DEF: {enemy.defense})\n")

    battle = BattleManager(player, enemy)
    battle.start_battle()

if __name__ == "__main__":
    main()
