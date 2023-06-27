from random import randint


class Game:
    def __init__(self, players):
        self.players = players
        self.position = 0
        self.dice = randint(1, 6)
        self.options_dict = {1: "No Play", 2: "Ladder", 3: "Snake"}

    def start(self):
        if self.players == 1:
            print("Player : ", self.players)
            print("Player Position : ", self.position)
            print("Dice Number : ", self.dice)
        else:
            print("Invalid Players")

    def options_check(self):
        options_rand = randint(1, 3)
        if options_rand in self.options_dict.keys():
            if options_rand == 1:
                print("\n", self.options_dict.get(options_rand))
                self.position = self.position
                print("Player Position : ", self.position)
            elif options_rand == 2:
                print("\nLadder...")
                self.position += self.dice
                print("Player Position : ", self.position)
            elif options_rand == 3:
                if self.position == 0:
                    print("\nSnake")
                    print("Player Position : ", self.position)
                else:
                    self.position -= self.dice
                    print("Player Position : ", self.position)


if __name__ == '__main__':
    game = Game(int(input("Enter Player Number : ")))
    game.start()
    game.options_check()
