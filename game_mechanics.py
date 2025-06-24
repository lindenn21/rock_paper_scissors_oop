from random import randint
from score import Scores
score = Scores()
score.score_tracker()
class Gameplay:
    def __init__(self):
        self.player = ""
        self.computer = ""
    def mechanics(self):
        rps_move = ["ROCK", "PAPER", "SCISSORS"]
        while score.player < score.winning and score.computer < score.winning:
            random_num = randint(0,2)
            print("SCORES:")
            print(f"|Player 1: {score.player} || Computer: {score.computer}|")
            self.player = input("Pick your move, Player: R - Rock | P - Paper | S - Scissors | Q - Quit ==").capitalize()

            if self.player == "Q":
                print("Game is stopping..")
                break

            if random_num == 0:
                self.computer = "ROCK"
            elif random_num == 1:
                self.computer = "PAPER"
            else:
                self.computer = "SCISSORS"

            print(f"Computer Picks: {self.computer}")









