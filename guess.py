#! python3
# guess.py - A number guessing game with user.
#          - guess a number from 1 to 100

# use random module to access randint() for computer to pick an int
import random

# set bounds for what number to guess
LOW_BOUND = 1
UPPER_BOUND = 100

game_over = False

while not game_over:
    computer_num = random.randint(LOW_BOUND, UPPER_BOUND)
    print('I am thinking of a number between', LOW_BOUND, 'and', UPPER_BOUND)

    count = 0
    user_guess = 0      # set inital user guess to number outside of bounds.

    while user_guess != computer_num:
        print('Take a guess')
        user_guess = int(input())
        count = count + 1
        
        if user_guess < computer_num:
            print('Your guess is too low.')
        elif user_guess > computer_num:
            print('Your guess is too high.')

    print('Good job! You guessed my number in', count, 'guesses!\n')

    print('Play again? (yes/no)')
    response = input()
    if response == 'yes':
        game_over = False
    elif response == 'no':
        game_over = True

print('Thanks for playing!')