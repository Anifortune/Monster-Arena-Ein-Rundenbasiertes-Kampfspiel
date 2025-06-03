class BattleManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print("🛡️ Der Kampf beginnt!")
        turn = 0

        while self.player.is_alive() and self.enemy.is_alive():
            attacker = self.player if turn % 2 == 0 else self.enemy
            defender = self.enemy if turn % 2 == 0 else self.player

            attacker.perform_attack(defender)
            input("Drücke Enter für die nächste Runde...\n")
            turn += 1

        winner = self.player if self.player.is_alive() else self.enemy
        print(f"🏆 {winner.name} hat gewonnen!")
