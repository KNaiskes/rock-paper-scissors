from player import Player

class Computer(Player):
    def __init__(self):
        pass

    def get_guess(self):
        import random
        return random.choice(self.valid_guesses)
