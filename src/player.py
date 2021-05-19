class Player:
    valid_guesses = ['rock', 'paper', 'scissors']

    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.guess = ''

    def get_player_guess(self, guess):

        while(guess not in self.valid_guesses):
            print(f'Valid options are: {", ".join(self.valid_guesses)}')
            guess = input().lower()

        self.guess = guess.lower()

    def get_score(self):
        return f'{self.player_name} score is: {self.score}'
