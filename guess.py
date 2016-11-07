import random

symbols = ["#", "$", "&"]

def random_algorithm(password, length):
	counter = 0
	rand = ''.join(random.choice(symbols) for i in range(length))
	while True:
		if password == rand:
			print("Match found: " + rand)
			print(str(counter) + " attempts")
			break
		else:
			rand = ''.join(random.choice(symbols) for i in range(length))
			counter += 1
    		
def execute_random_algorithm(length):
	print("Choose from " + str(symbols))
	password = input("Enter password (" + str(length) + " symbols): ")
	if len(password) != length:
		print("The password you entered is not the length specified")
	else:
		found = True
		for i in range(length):
			if password[i] != symbols[0] and password[i] != symbols[1] and password[i] != symbols[2]:
				print("the password you entered has characters that do not equal the symbols listed above.")
				found = False
				break
		if found == True:
			random_algorithm(password, length)

execute_random_algorithm(6)
