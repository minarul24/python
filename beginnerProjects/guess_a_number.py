import random


def guess():
    print(f'This is a number guessing game. It will first ask you to state the lower bound and '\
    f'then state the upper bound. The program will then generate a number randomly in boundary'\
          f'range provided. Finally, it will ask you guess the number!')

    lower_bound = input("Please, enter the lower bound: ")
    upper_bound = input("Please, enter the upper bound: ")


# The function/method is called to run program guess()
guess()