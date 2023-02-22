# Trying to create simple calculator using dict, while-loop and recursion


def add(n1, n2):
	return n1 + n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

def subtract(n1, n2):
	return n1 - n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}


def calculator():
	num1 = float(input("What's the first number?: "))
	for key in operations:
			print(key)
	should_continue = True
	while should_continue:
		operation = input("Pick an operation from the line above: ")
		num2 = float(input("What's the second number?: "))
		func = operations[operation]
		answer = func(num1, num2)
		print("{} {} {} = {}".format(num1, operation, num2, answer))
		continue_calc = input("Type 'y' to continue with {}, or type 'n' to start a new calculation: ".format(answer))
		if continue_calc == 'y':
			num1 = answer
		elif continue_calc == 'n':
			should_continue = False
			calculator()

calculator()