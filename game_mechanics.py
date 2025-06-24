from random import randint
from score import Scores
score = Scores()
score.score_tracker()
class Gameplay:
    def mechanics(self):
        while score.player < score.winning and score.computer < score.winning:
            random_num = randint(0,2)
            print("SCORES:")
            print(f"|Player 1: {score.player} || Computer: {score.computer}|")
            self.player = input("Pick your move, Player: R - Rock | P - Paper | S - Scissors | Q - Quit ==").capitalize
            if self.player == "Q":
                break




