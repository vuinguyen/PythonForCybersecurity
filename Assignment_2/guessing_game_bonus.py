# Guessing Game
# Purpose: Have the user guess a random number between 1 and 20
# Bonus: Track how many times the user has guessed
# Bonus: Limit the number of guesses and end the program after the user has guessed too many times
# Bonus: Display how many guesses the user took to get the correct answer

import random

random_number = random.randint(1, 20)
total_num_guesses = 5
total_user_guesses = 0

for iterator in range(0, total_num_guesses):
    guess = input(f'Guess a number between 1 and 20. You can guess up to {total_num_guesses} times: ')   
    try: 
        guess = int(guess)
        total_user_guesses += 1

        if guess == random_number:
            print('You guessed correctly! It took you ' + str(total_user_guesses) + ' guesses')
            break
        else:
            if iterator == total_num_guesses - 1:
                print(f'You have used all your guesses. The number was {random_number}')
            else:
                print(f"You guessed incorrectly. You've used {total_user_guesses} so far. Try again.")
                # print(random_number)
                # print(guess)
    except:
        print('Please enter a number')