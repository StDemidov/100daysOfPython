############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Added bids (without checking)

import random
from art import logo

def start_end_game():
	return (input("Do you want to play Blackjack? Type 'y' or 'n': "))

def take_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return(random.choice(cards))

def take_another_card(players_cards):
	new_card = take_card()
	if new_card == 11:
		if sum(players_cards) + new_card > 21:
			new_card = 1
	players_cards.append(new_card)


def show_cards(players_cards, dealers_cards):
	print("Your cards: {}, current score: {}".format(players_cards, sum(players_cards)))
	print("Dealer's first card: [{}]\n".format(dealers_cards[0]))

def get_results(players_cards, dealers_cards, current_bank, current_bet):
	players_score = sum(players_cards)
	dealers_score = sum(dealers_cards)
	print("Your final hand: {}, final score: {}".format(players_cards, players_score))
	print("Dealer's final hand: {}, final score: {}\n".format(dealers_cards, dealers_score))
	if players_score > 21:
		print("You went over. You lose {}! Your bank: {}\n".format(current_bet, current_bank))
		return(current_bank)

	elif dealers_score > 21:
		current_bank += current_bet * 2
		print("Dealer went over. You won {}! Your bank: {}\n".format(current_bet * 2, current_bank))
		return(current_bank)

	elif players_score > dealers_score:
		current_bank += current_bet * 2
		print("You won {}! Your bank: {}\n".format(current_bet * 2, current_bank))
		return(current_bank)

	elif players_score < dealers_score:
		print("Dealer's hand is higher! You lose {}! Your bank: {}\n".format(current_bet, current_bank))
		return(current_bank)

	else:
		current_bank += current_bet
		print("It's a draw. Your bank: {}\n".format(current_bank))
		return(current_bank)

bids = [10, 50, 100, 500, 1000, 'all-in']

bank = 10000

while bank != 0 and start_end_game() == 'y' :
	print('\n' * 100)
	print(logo)
	print("Your bank is {}".format(bank))

	bet = 1000000
	while 1:
		bet = 1000000
		print(bids)
		bet = input("Choose your bet from the list above or type 'all' for 'all-in': ")	
		if bet == 'all':
			bet = bank
		else:
			bet = int(bet)
		if bet > bank:
			print("Your bet is higher than your bank. Decrease it.")
			continue
		else:
			bank -= bet
			break

	print("Your bet is {}".format(bet))
	players_cards = [take_card(), take_card()]
	dealers_cards = [take_card(), take_card()]

	players_score = sum(players_cards)
	dealers_score = sum(dealers_cards)

	##Checking if player has [A, A]
	if players_score == 22:
		players_cards[1] = 1
	#Checking if anyone have Blackjack
	if dealers_score == 21:
		print("You lose {}! Dealer has BlackJack. Your bank: {}. Dealer's cards: {}. Your score is {}\n".format(bet, bank, dealers_cards, players_score))
		continue
	elif players_score == 21:
		bank -= bet
		print("You won {}! You have BlackJack. Your bank: {}. Dealer's score: {}. Your cards: {}\n".format(bet, bank, dealers_score, players_cards))
		continue
	if dealers_score == 22:
		dealers_score = 12
		dealers_cards[1] = 1
	
	show_cards(players_cards, dealers_cards)

	#Let player take some more cards
	continue_game = True
	while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
		take_another_card(players_cards)
		if sum(players_cards) > 21:
			continue_game = False
			break
		else:
			show_cards(players_cards, dealers_cards)

	while dealers_score < 17 and continue_game == True:
		take_another_card(dealers_cards)
		dealers_score = sum(dealers_cards)
		if dealers_score > 21:
			break

	bank = get_results(players_cards, dealers_cards, bank, bet)

