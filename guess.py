import random

symbols = ["#", "$", "&"]

# Random algorithm method that uses a iterator to generate passwords.


def random_algorithm(password, length):
    # Initial counter for attempts.
    counter = 0
    # Python iterator for random algorithm.
    rand = ''.join(random.choice(symbols) for _ in range(length))
    # Main counter loop.
    while True:
        # If the password is equal to the generated password, then stop the loop and display the number of attempts.
        if password == rand:
            print("Match found: " + rand)
            print(str(counter) + " attempts")
            break
        # If the password is not equal to the generate password, then continue the loop and add an attempt (counter).
        else:
            rand = ''.join(random.choice(symbols) for _ in range(length))
            counter += 1

# Main method where the password is checked based on length and characters.


def execute_random_algorithm(length):
    print("Choose from " + str(symbols))
    # Take password input from the user.
    password = input("Enter password (" + str(length) + " symbols): ")
    # Check if the length of the password inputted matches the length specified.
    if len(password) != length:
        print("The password you entered is not the length specified")
    else:
        # Boolean variable to store if the password has the right characters.
        found = True
        # Check if the password has the right characters by iterating through the password and checking each character.
        for i in range(length):
            if password[i] != symbols[0] and password[i] != symbols[1] and password[i] != symbols[2]:
                print("the password you entered has characters that do not equal the symbols listed above.")
                found = False
                break
        # If the characters match then execute the random algorithm.
        if found:
            random_algorithm(password, length)

# Execute the main program with the length specified.
execute_random_algorithm(3)
