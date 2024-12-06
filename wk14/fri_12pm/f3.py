import random

class BlackJack:
    def __init__(self, game_title, player_name):
        self.__game_title = game_title
        self.__player_name = player_name
        suits = "hearts", "diamonds", "clubs", "spades"
        self.__cards = dict()
        for suit in suits:
            self.__cards[suit] = list()
            for value in range(2, 11):
                self.__cards[suit].append(str(value))
            self.__cards[suit].append("Jack")
            self.__cards[suit].append("Queen")
            self.__cards[suit].append("King")
            self.__cards[suit].append("Ace")
    def play(self):
        self.turn("player")
        self.turn("dealer")


    def get_random_card(self):
        random_suit = random.choice(list(self.__cards.keys()))
        random_value = random.choice(self.__cards[random_suit])

        if not random_value.isdigit():
            card_map = {"A": 1, "J": 11, "Q": 12, "K": 13}
            num_value = card_map[random_value[0].upper()]
        else:
            num_value = int(random_value)

        return f"{random_value} of {random_suit}", num_value

    def turn(self, who):
        card_total = 0

        value_1 = self.get_random_card()
        value_2 = self.get_random_card()

        card_total += value_1[1]
        card_total += value_2[1]

        print("Your first card is",value_1[0])
        print("Your first card is",value_2[0])
        print("Your total is", card_total)

        while True:
            if who == "player":
                answer = input("(H)it or (S)tay? ")
                if answer.lower().strip()[0] == "h":
                    next_card = self.get_random_card()
                    card_total += next_card[1]
                    print("Your next card is", next_card[0])
                    print("Your total is now", card_total)
                elif answer.lower().strip()[0] == "s":
                    print("You decided to stay")
                    break
                else:
                    print("Invalid option")
            elif who == "dealer":
                if card_total >= 18:
                    print("The dealer stays.")
                    break
                print("The dealer hits")
                print("The dealer's next card is", next_card[0])
                print("The dealer's total is now", card_total)
                next_card = self.get_random_card()
                card_total += next_card[1]

            else:
                print("Oops, something went wrong. Exiting game")
                break



game1 = BlackJack("Game 1", "John")
game1.play()





"""

To-Do

           
Change all occurences of YOUR turn is to refer to player name

Add the game title to the text
    iso Your turn. 
    state: Game {game_title} player {player_name} turn
            OR
            Game {game_title} dealers turn

Add a method to determine who wins, and announce it at the end

Add a Condition to force game/player to wait when selecting cards

Run 2 games at the same time and note observations

"""