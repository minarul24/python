import random


def guess():
    print(f'This is a number guessing game. It will first ask you to state the lower bound and '\
    f'then state the upper bound. The program will then generate a number randomly in boundary'\
          f'range provided. Finally, it will ask you guess the number!')

    lower_bound = int(input("Please, enter the lower bound: "))
    upper_bound = int(input("Please, enter the upper bound: "))

    number = random.randint(lower_bound,upper_bound)

    user_input = int(input("Please, enter your GUESS: "))

    if lower_bound <= user_input <= upper_bound:
        if user_input == number:
            print(f"Congratulations! You have entered {user_input}. {number} is the correct answer!")

        else:
            while user_input != number:
                if int(user_input) == number:
                    print(f"Congratulations! You have entered {user_input} and {number} is the correct answer!")
                    break

                elif user_input == '0':
                    print(f"Thank you for playing! The number was {number}.")
                    break

                else:
                    user_input = input(
                        "Sorry, you guessed the wrong number. To continue, enter another number or press '0' to QUIT: ")

    elif user_input > upper_bound or user_input < lower_bound:
        print(f'The number you entered, is not in the provided range')

        if user_input == number:
            print(f"Congratulations! You have entered {user_input}. {number} is the correct answer!")

        else:
            while user_input != number:
                if int(user_input) == number:
                    print(f"Congratulations! You have entered {user_input} and {number} is the correct answer!")
                    break

                elif user_input == '0':
                    print(f"Thank you for playing! The number was {number}.")
                    break

                else:
                    user_input = input(
                        "Sorry, you guessed the wrong number. To continue, enter another number or press '0' to QUIT: ")




# The function/method is called to run program guess()
guess()