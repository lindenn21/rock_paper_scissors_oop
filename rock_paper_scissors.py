from game_mechanics import Gameplay
class StartGame(Gameplay):
    def start_game(self):
        print("Welcome to RPS!!")
        print("First to 5 wins the game, would you like to play?")
        print("1. Play the game")
        print("2. Nope! I'm leaving.")
        try:
            while True:
                choice = input("Choose (1 - Play, 2 - Exit): ")
                if choice == "1":
                    self.mechanics()
                    break
                elif choice == "2":
                    print("Alright! Thanks and goodbye.")
                    break
                else:
                    print("Umm, the choices you're supposed to input are 1 or 2...")
        except TypeError:
            print("Try again...")











