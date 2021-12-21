import random


def game():
    print(f'Welcome to Rock, Paper and Scissor Game!')
    # user input is taken, whats their choice from rock, paper and scissor!
    user_input = input("Choose 'r' for rock, 'p' for paper and 's' for scissor: \n")
    # takes computer input of the game
    computer_input = random.choice(['r', 'p', 's'])

    if user_input == computer_input:
        print(f'User: {user_input} \nComputer: {computer_input} \nIt\'s a TIE!')


game()
