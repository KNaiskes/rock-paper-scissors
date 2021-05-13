from player import Player
from computer import Computer

def menu(user_option):
    try:
        user_option = int(user_option)
        if user_option == 1:
            print('Enter new user name')
        elif user_option == 2:
            print('Play again')
        elif user_option == 3:
            print('Exit')
    except ValueError:
        print('An integer is the only valid option')

computer = Computer()
print('Welcome!\nEnter your username in order to play: ')
player = Player(input())

print('Make a guess!: (rock, paper, scissors)')
player.get_player_guess(input())

print(computer.get_guess())
