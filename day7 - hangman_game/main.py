# Realisation of Hangman game
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

#Creating a list from string
word_as_a_list = [letter for letter in chosen_word]

number_of_letters = len(word_as_a_list)

print(hangman_art.logo)
print("Welcome to the PyHangman Game!")
guesses_list = list() #List for saving player's guesses to say him if will be repeats
lifes = 7 #Creating lifes of player
result_word = ["_" for letter in chosen_word] #In this list we will put right guesses
while number_of_letters > 0 and lifes != 0: #Until player has lifes and word unsolved
	print(" ".join(result_word)) #Printing resulted word by player's guesses
	guess = input("Guess a letter: ").lower() #Getting player's guess
	print("\n" * 100) #Clearing screen
	if guess in guesses_list:
		print("You already guessed the letter: {}!\n".format(guess))
		continue
	guesses_list.append(guess)
	if guess in word_as_a_list: #Our checking list similar to guessed word
		while guess in word_as_a_list:
			index = word_as_a_list.index(guess)
			word_as_a_list[index] = "" #Deleting every right letter
			number_of_letters -= 1
			result_word[index] = guess #Filling spaces with right ones
	else:
		lifes -= 1
		print("You guessed {}. that's not in the word. Lifes: {}\n".format(guess, lifes))
		print(hangman_art.stages[lifes])
if lifes == 0:
	print("You lose. Try again!")
else:
	print("Congratulations. You won. The word was {}".format(chosen_word.upper()))



