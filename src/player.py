class Player:
    valid_guesses = ['rock', 'paper', 'scissors']

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.guess = ''

    def set_guess(self, guess):

        while(guess not in self.valid_guesses):
            print(f'Valid options are: {", ".join(self.valid_guesses)}')
            guess = input().lower()

        self.guess = guess.lower()

    def get_guess(self):
        return self.guess

    def set_score(self, points):
        self.score += points

    def get_score(self):
        return f'{self.player_name}\'s score is: {self.score}'
