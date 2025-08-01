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

    def start(self):
        round_num = 1
        print("\nНачинается битва!")
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n--- Раунд {round_num} ---")

            # Ход игрока
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} HP")

            if not self.computer.is_alive():
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} HP")

            round_num += 1

        print("\nИгра окончена!")
        if self.player.is_alive():
            print(f"Победил {self.player.name}!")
        else:
            print("Победил Компьютер!")

# Запуск игры
game = Game()
game.start()
