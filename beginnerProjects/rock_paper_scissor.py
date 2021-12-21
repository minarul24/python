import random


def game():
    print(f'Welcome to Rock, Paper and Scissor Game!')

    user_name = input("Please enter your name: ")
    user_input = 0
    while user_input != 'q':
        # user input is taken, whats their choice from rock, paper and scissor!
        user_input = input("Choose 'r' for rock, 'p' for paper and 's' for scissor \n or choose 'q' to quit: \n")
        # takes computer input of the game
        computer_input = 'r' #random.choice(['r', 'p', 's'])
        game_decision(user_name,user_input,computer_input)


    print(f'{user_name}, thank you for playing!')


def game_decision(username,user, computer):
    if user == computer:
        print(f'{username}: {user} \nComputer: {computer} \nIt\'s a TIE!')

    # paper wins against rock, rock wins against scissors, scissor wins against paper
    elif user == 'r' and computer == 's':
        print(f'{username} WON!')



game()
