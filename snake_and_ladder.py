from random import randint


class Game:
    def __init__(self, players):
        self.players = players
        self.position = 0

    def start(self):
        if self.players == 1 and self.position == 0:
            dice = randint(1, 6)
            print("Dice Number : ", dice)
        else:
            print("Invalid Players")


if __name__ == '__main__':
    game = Game(int(input("Enter Player Number : ")))
    game.start()
