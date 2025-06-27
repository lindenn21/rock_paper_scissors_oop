from game_mechanics import Gameplay
class StartGame(Gameplay):
    def start_game(self):
        print("Welcome to RPS!!")


game = Gameplay()
game.mechanics()
game.moves()