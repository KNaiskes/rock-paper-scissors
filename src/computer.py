from player import Player

class Computer(Player):
    def __init__(self):
        self.player_name = 'Computer'
        self.score = 0
        self.guess = ''

    def get_guess(self):
        import random
        return random.choice(self.valid_guesses)
