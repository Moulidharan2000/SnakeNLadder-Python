from random import randint


class Game:
    def __init__(self, players):
        self.players = players
        self.position = 0
        self.dice = 0
        self.options_dict = {1: "No Play", 2: "Ladder", 3: "Snake"}
        self.win_position = 100

    def start(self):
        if self.players == 1:
            print("Player : ", self.players)
            print("Player Position : ", self.position)
            return True
        return False

    def options_check(self):
        while self.position <= self.win_position:
            self.dice = randint(1, 6)
            options_rand = randint(1, 3)
            previous_position = self.position
            if options_rand in self.options_dict.keys():
                print("\nDice Number : ", self.dice)
                if options_rand == 1:
                    print(self.options_dict.get(options_rand))
                    self.position = self.position
                elif options_rand == 2:
                    print(self.options_dict.get(options_rand))
                    self.position += self.dice
                elif options_rand == 3:
                    print(self.options_dict.get(options_rand))
                    self.position -= self.dice
                    if self.position < 0:
                        self.position = 0
            print("Player Position : ", self.position)
            if self.position > self.win_position:
                self.position = previous_position
            elif self.position == self.win_position:
                print("Player 1 Wins...")
                break


if __name__ == '__main__':
    game = Game(int(input("Enter number of Players : ")))
    if game.start():
        game.options_check()
    else:
        print("Invalid Players...")
