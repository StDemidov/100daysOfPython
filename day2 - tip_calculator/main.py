# Simple tip calculator to practise diffferent data types and data type converting
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_persons = int(input("How many people to split the bill? "))
percentage = (tip_perc / 100) + 1
print("Each person should pay: ${}".format(round((total_bill * percentage) / num_of_persons), 2))