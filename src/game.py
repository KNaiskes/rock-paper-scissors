from player import Player
from computer import Computer

def check_result(human_player, computer_player):
    if human_player.get_guess() == computer_player.get_guess():
        print('[Draw] Both you and the computer guessed the same!')
        human_player.set_score(0.5)
        computer_player.set_score(0.5)
    elif human_player.get_guess() == "rock":
        if computer_player.get_guess() == "scissors":
            print("Rock smashes scissors! You win!")
            human_player.set_score(1)
        else:
            print("Paper covers rock! You lose.")
            computer_player.set_score(1)
    elif human_player.get_guess() == "paper":
        if computer_player.get_guess() == "rock":
            print("Paper covers rock! You win!")
            human_player.set_score(1)
        else:
            print("Scissors cuts paper! You lose.")
            computer_player.set_score(1)
    elif human_player == "scissors":
        if computer_player.get_guess() == "paper":
            print("Scissors cuts paper! You win!")
            human_player.set_score(1)
        else:
            print("Rock smashes scissors! You lose.")
            human_player.set_score(1)

computer = Computer()

player = Player(input('Welcome!\nEnter your username in order to play: '))

while True:
    print('Make a guess!: (rock, paper, scissors)')
    player.set_guess(input())

    check_result(player, computer)
    print('==========')
    print(f'Score: {player.get_score()} - {computer.get_score()}')
    print('==========')
