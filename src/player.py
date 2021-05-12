class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0

    def get_score(self):
        return f'{self.player_name} is: {self.score}'
