# Practising with dictionaries. Creating simple auction
auction_bids = {}
while 1:
	name = input("What is your name? ")
	bid = float(input("What is your bid? "))
	auction_bids[name] = bid
	continue_auction = input("Are there any other bidders? Type 'yes' or 'no': ")
	if continue_auction == "no":
		break
	print("\n" * 100)

max_bid = 0
winner = ''
for name in auction_bids:
	if auction_bids[name] > max_bid:
		winner = name
		max_bid = auction_bids[name]

print("And the winner is {} with bid of {}".format(winner, auction_bids[winner]))
