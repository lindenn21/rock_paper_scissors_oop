from random import randint
from score import Scores
score = Scores()
score.score_tracker()
class Gameplay:
    def __init__(self):
        self.player_move = ""
        self.computer_move = ""

    def mechanics(self):
        rps_move = {"R": "ROCK","P": "PAPER","S": "SCISSORS"}
        while score.player < score.winning and score.computer < score.winning:
            random_num = randint(0,2)
            print("SCORES:")
            print(f"|Player 1: {score.player} || Computer: {score.computer}|")
            self.player_move = input("Pick your move, Player: R - Rock | P - Paper | S - Scissors | Q - Quit ==").upper()

            if self.player_move == "Q":
                print("Game is stopping..")
                break

            if random_num == 0:
                self.computer_move = "ROCK"
            elif random_num == 1:
                self.computer_move = "PAPER"
            else:
                self.computer_move = "SCISSORS"

            print(f"Computer Picks: {self.computer_move}")

            self.play()

    def play(self):
        if self.player_move == self.computer_move:
            print("It's a tie!")
        elif self.player_move == "R":
            if self.computer_move == "SCISSORS":
                print("Player: ROCK | Computer = SCISSORS | PLAYER WINS!")
                score.player += 1
            else:
                print("Player: ROCK | Computer = PAPER | COMPUTER WINS!")
                score.computer += 1
        elif self.player_move == "P":
            if self.computer_move == "ROCK":
                print("Player: PAPER | Computer = ROCK | PLAYER WINS!")
                score.player += 1
            else:
                print("Player: PAPER | Computer = SCISSORS | COMPUTER WINS!")
                score.computer_move += 1
        elif self.player_move == "S":
            if self.computer_move == "PAPER":
                print("Player: SCISSORS | Computer = PAPER | PLAYER WINS!")
                score.player += 1
            else:
                print("Player: SCISSORS | Computer = ROCK | COMPUTER WINS!")
                score.computer += 1
        else:
            print("Invalid move!")












