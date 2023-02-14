# Simple rock-paper-scissors game. Practicing with random library and lists
import random

def draw_the_chose(chose):
	if chose == 0:
		print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
	elif chose == 1:
		print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
	else:
		print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

list_of_choses = ["Rock", "Paper", "Scissors"]
players_chose = 3
while players_chose < 0 or players_chose > 2:
	players_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
draw_the_chose(players_chose)
pc_chose = random.randint(0, 2)
print("Computer chose:")
draw_the_chose(pc_chose)
if players_chose > pc_chose:
	if players_chose == 3 and pc_chose == 0:
		print("You lose!")
	else:
		print("You win!")
elif players_chose == pc_chose:
	print("Draw!")
else:
	print("You win!")
