import random

symbols = ["#", "$", "&"]

def execute_random_algorithm(password, length):
	counter = 0
	rand = ''.join(random.choice(symbols) for i in range(length))
	print(rand)
	while True:
		if password == rand:
			print(str(counter) + " attempts")
			break
		else:
			rand = ''.join(random.choice(symbols) for i in range(length))
			print(rand)
			counter += 1

def random_algorithm(length):
    pass1 = input("Enter password (" + str(length) + " symbols): ")
    if len(pass1) != length:
    	print("The password you entered is not the length specified")
    else:
    	found = True
    	for i in range(length):
    		if pass1[i] != symbols[0] and pass1[i] != symbols[1] and pass1[i] != symbols[2]:
    			print("the password you entered has characters that do not equal the symbols listed above.")
    			found = False
    			break
    	if found == True:
    		random_compute(pass1, length)
    				
execute_random_algorithm(4)
