class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.guess = ''

    def get_player_guess(self, guess):
        valid_guesses = ['rock', 'paper', 'scissors']

        while(guess not in valid_guesses):
            print(f'Valid options are: {", ".join(valid_guesses)}')
            guess = input().lower()

        self.guess = guess.lower()
        print(self.guess)

    def get_score(self):
        return f'{self.player_name} is: {self.score}'
