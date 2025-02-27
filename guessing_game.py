# Guessing Game
# Purpose: Have the user guess a random number between 1 and 20

import random

random_number = random.randint(1, 20)
total_num_guesses = 5

for iterator in range(0, total_num_guesses):
    guess = input(f'Guess a number between 1 and 20. You can guess up to {total_num_guesses} times: ')   
    try: 
        guess = int(guess)
        if guess == random_number:
            print('You guessed correctly!')
            break
        else:
            if iterator == total_num_guesses - 1:
                print(f'You have used all your guesses. The number was {random_number}')
            else:
                print(f'You guessed incorrectly. Try again.')
                # print(random_number)
                # print(guess)
    except:
        print('Please enter a number')


