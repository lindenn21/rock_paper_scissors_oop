from game_mechanics import Gameplay
class StartGame(Gameplay):
    def start_game(self):
        print("Welcome to RPS!!")
        print("First to 5 wins the game, would you like to play?")
        print("1. Play the game")
        print("2. Nope! I'm leaving.")
        try:
            choice = input("Choose: ")
            if choice == "1":
                self.mechanics()
            else:
                print("Alright! Goodbye.")











