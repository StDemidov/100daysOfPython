# Number guessing game, where player should guess a number
# which was chosen by computer

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'hard':
	attempts = 5
else:
	attempts = 10

num_to_guess = random.randint(1, 100)

while attempts != 0:
	print("You have {} attempts remaining to guess the number.".format(attempts))
	guess = int(input('Make a guess: '))
	if guess == num_to_guess:
		print("You won! The answer was {}".format(guess))
		break
	elif guess > num_to_guess:
		print("Too high.")
	else:
		print("Too low.")
	attempts -= 1
	
if attempts == 0:
	print('You lose! The answer was {}'.format(num_to_guess))		