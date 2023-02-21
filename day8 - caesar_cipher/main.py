#Practising with function declaring
#Simple caesar cipher that can encode/decode your message
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction, abc = alphabet):
	abc_len = len(abc)
	result_word = ""	
	shift %= abc_len
	for letter in text:
		if letter not in abc:
			result_word += letter
			continue
		index = abc.index(letter)
		if direction == "encode":
			new_index = index + shift
			if new_index > abc_len - 1: # To avoid cases of end of the list
				new_index -= abc_len
		elif direction == "decode":
			new_index = index - shift
		else:
			print("Please, write a encode/decode without any other symbols.")
			return
		result_word += abc[new_index]
	print("The {}d text is {}".format(direction, result_word))

print(art.logo)

continue_operation = True
while continue_operation:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(text, shift, direction)
	yes_no = input("Do you want to continue (type y - for yes, something else - to quit: ").lower()
	if yes_no != "y":
		continue_operation = False