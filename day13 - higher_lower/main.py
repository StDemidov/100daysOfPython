#higher-lower game. 
#followers data is not real

import random
import art
from game_data import data

start_game = True

def renew_list():
	return [x for x in range(len(data))]

def choose_celeb(celebs_list):
	new_celeb = random.choice(celebs_list)
	celebs_list.remove(new_celeb)
	return data[new_celeb]

#Function for compairing stars and returning True if answer is right with 
#right answer as dict 
def compare(a_celeb, b_celeb, answer):
	if answer == 'a' and (a_celeb['follower_count'] > b_celeb['follower_count']):
		return {'res': True, 'right_answer': a_celeb}
	elif answer == 'b' and (a_celeb['follower_count'] < b_celeb['follower_count']):
		return {'res': True, 'right_answer': b_celeb}
	else: 
		return {'res': False, 'right_answer': 0}

while start_game:
	# Refreshing all vars for new game
	start_game = False
	last_celebs = renew_list()
	right_answer = {'res': True}
	score = 0
	# Getting first celeb here, because then it will be similar to right answer
	a_celeb = choose_celeb(last_celebs)
	while right_answer['res'] and len(last_celebs) != 0:
		print(art.logo)
		# Start printing after first right answer
		if score > 0:
			print("You're right! Current score: {}".format(score))
		b_celeb = choose_celeb(last_celebs)
		print("Compare A: {}, a {}, from {}".format(a_celeb['name'], a_celeb['description'], a_celeb['country']))
		print(art.vs)
		print("Against B: {}, a {}, from {}".format(b_celeb['name'], b_celeb['description'], b_celeb['country']))
		answer = input("Who has more followers in Instagram? A or B: ").lower()
		right_answer = compare(a_celeb, b_celeb, answer)
		# Checking by 'res' key in dict from return of compare func
		# If it == FALSE then loop will break
		if right_answer['res']:
			score +=1
			a_celeb = right_answer['right_answer']
			print('\n' * 100)
	# If we are here, then game ended due to false answer or to ending of celebs
	if right_answer['res'] == False:
		print("Sorry, that's wrong. Final score: {}".format(score))
	else:
		print("Congratulations! You completed the game. Final score: {}".format(score))
	cont_game = input("Do you want to start a new game? Type 'y' or 'n': ").lower()
	if cont_game == 'y':
		start_game = True
