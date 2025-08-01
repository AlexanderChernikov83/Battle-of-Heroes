import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} на {damage} урона!")

    def is_alive(self):
        return self.health > 0

    class Game:
        def __init__(self):
            player_name = input("Введите имя вашего героя: ")
            self.player = Hero(player_name)
            self.computer = Hero("Компьютер")