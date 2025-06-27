from game_mechanics import Gameplay
class StartGame(Gameplay):
    def start_game(self, ):
        print("Welcome to RPS!!")
        print("First to 5 wins the game, would you like to play?")

        choice = input("Yes or No?: ")






game = Gameplay()
game.mechanics()
game.moves()