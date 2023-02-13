# Simple script that will suggest you a name for your garage band
# based on your answers. Just practicing print/input func

print("Welcome to the Band Name Generator!")
print("Nice to meet you, " + input("What's your name?\n") + "!")
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's you pet's name?\n")
print("Your band name could be {} {}!".format(city_name, pet_name))