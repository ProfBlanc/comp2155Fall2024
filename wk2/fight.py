# print("ready, set, fight!")

"""

This is a fighting game where 2 players that have
    name, attack_level, health

are going to fight each other until 1 player's health reaches zero

Example
    Player 1: Batman    health=25, attack = 5
    Player 2: Superman  health = 20, attack = 4

    Batmas attacks Superman
        Superman's health decreases to 15
    Superman attacks Batman
        Batman's health decreases to 21

allow the user to pass 6 args to module
player1_name player1_attack player1_health
player2_name player2_attack player2_health


Create a Player class
    3 attributes: name, health, attack
        limit: name: at least 3 chars, health at least 20, attack 3-8
Create a Game class
    a list of two players
    a method that starts fight
    a method that outlines what happens when 1 player hits/strikes/attacks another player

"""
import random
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Value is not a string")
        elif len(value) < 3:
            raise ValueError("Name is too short")
        self.__name = value

    @property
    def health(self) -> int:
        return self.__health
    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Health value is not an int")
        elif value < 20:
            raise ValueError("Health value is not greater than 20")
        self.__health = value

    @property
    def attack(self) -> int:
        return self.__attack
    @attack.setter
    def attack(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Attack value is not an int")
        elif value < 3 or value > 8:
            raise ValueError("Invalid Attack value")
        self.__attack = value

    def strike(self, power: int):
        self.__health -= power

    def has_health(self):
        return self.__health > 0

    def __str__(self):
        return f"Name={self.__name}, Health={self.__health}, Attack={self.__attack}"

class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        if isinstance(player1, Player) and isinstance(player2, Player):
            self.__players = [player1, player2]
            self.start()
        else:
            raise ValueError("Both args need to be players")

    def start(self):
        while self.__players[0].has_health() and self.__players[1].has_health():
            self.turn()
    def turn(self):
        # attacker = random.randint(0,1)  # easier
        attacker = self.__players.index(random.choice(self.__players))
        getting_attacked = int(not attacker)

        self.__players[getting_attacked].strike(self.__players[attacker].attack)

        print(f"{self.__players[attacker].name} is attacking "
              f"{self.__players[getting_attacked].name}. {self.__players[getting_attacked].name} health is now {self.__players[getting_attacked].health}")



p1 = Player("Batman", 25, 5)
p2 = Player("Superman", 20, 4)
game = Game(p1, p2)

