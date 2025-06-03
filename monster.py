class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        damage = max(amount - self.defense, 0)
        self.health -= damage
        print(f"{self.name} nimmt {damage} Schaden! (HP: {self.health})")

    def perform_attack(self, target):
        print(f"{self.name} greift {target.name} an!")
        target.take_damage(self.attack)
