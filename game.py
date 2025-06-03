from monster import Monster
from battle_manager import BattleManager
import random

# Liste verfügbarer Monster
available_monsters = [
    Monster("Pyron", health=100, attack=20, defense=5),
    Monster("Aqualis", health=90, attack=18, defense=6),
    Monster("Terron", health=110, attack=15, defense=8),
    Monster("Zephyra", health=80, attack=25, defense=3)
]

def choose_monster():
    """Lässt den Spieler ein Monster auswählen."""
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
    """Wählt zufällig ein gegnerisches Monster, das nicht das Spieler-Monster ist."""
    candidates = [m for m in available_monsters if m.name != exclude_monster.name]
    return random.choice(candidates)

def main():
    """Startet das Spiel und fragt, ob der Spieler erneut spielen möchte."""
    print("🎮 Willkommen in der MONSTER ARENA!")
    print("Stelle dich im rundenbasierten Kampf einem zufälligen Gegner.\n")

    while True:
        # Monster auswählen
        player = choose_monster()

        # Gegner zufällig wählen
        enemy = choose_enemy(player)
        print(f"⚔️ Dein Gegner ist {enemy.name}!")
        print(f"   HP: {enemy.health}, ATK: {enemy.attack}, DEF: {enemy.defense}\n")

        # Kampf starten
        battle = BattleManager(player, enemy)
        battle.start_battle()

        # Wiederholung abfragen
        again = input("\n🔁 Möchtest du nochmal spielen? (j/n): ").strip().lower()
        if again != 'j':
            print("\n👋 Danke fürs Spielen! Bis zum nächsten Mal.")
            break

if __name__ == "__main__":
    main()

