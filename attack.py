class Attack:
    def __init__(self, name, damage, cost=0):
        self.name = name
        self.damage = damage
        self.cost = cost  # z. B. für Energie oder Mana in späteren Versionen

    def use(self, attacker, target):
        print(f"{attacker.name} verwendet {self.name}!")
        target.take_damage(self.damage)
