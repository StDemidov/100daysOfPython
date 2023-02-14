# Simple answer based game for practising with if-else conditions
# There is no clearing input only lower. So any spaces, tabs etc. will trigger Game Over
print('''******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
answer = input('You are on crossroad, where do you want to go? Type "left" or "right"\n').lower()
if answer == "left":
	answer = input("You have reached the river bank. The current is quite strong,\nbut the distance to the opposite shore is very close. You can try to swim across\nor to wait for a boat that was approaching from afar.\nType 'swim' or 'boat'\n").lower()
	if answer == "boat":
		answer = input("You crossed the river by boat. You see three doors next you.\nWhich would you choose? Type 'red', 'yellow' or 'blue'\n").lower()
		if answer == "red":
			print("You was surrounded with fire. Game over.")
		elif answer == "blue":
			print("You was surrounded by beasts. Game over.")
		elif answer == "yellow":
			print("You found the treasure. You win!")
		else:
			print("Game over, fool!")
	else:
		print("You tried to cross the river. But was attacked by trout. Game over.")
else:
	print("You went right. You were surrounded by incredibly beautiful landscapes.\nAdmiring the beauties of nature, you did not follow the road at all.\nYou stumbled and fell into a hole")
	print("Game over.")