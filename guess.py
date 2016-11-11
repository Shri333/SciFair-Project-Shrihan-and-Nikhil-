import random

symbols = ["#", "$", "&"]

# Random algorithm method that uses an iterator to generate passwords.


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
        # If the password is not equal to the generate password, then continue the loop and increase the counter.
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
        print("The length of the password you entered is not the length specified.")
    else:
        # Boolean variable to store if all the characters in the password match the characters listed in the symbols.4
        match = True
        # Check if the password has the right characters by iterating through the password and checking each character.
        for i in range(length):
            if password[i] != symbols[0] and password[i] != symbols[1] and password[i] != symbols[2]:
                print("the password you entered has characters that do not equal the symbols listed above.")
                match = False
                break
        # If the characters match then execute the random algorithm to guess the password.
        if match:
            random_algorithm(password, length)

# Get length of password from user.
password_length = input("Enter length of password: ")
try:
    # Try to convert password_length to an integer.
    password_length = int(password_length)
    # Check if password_length is greater than 0.
    if password_length > 0:
        execute_random_algorithm(password_length)
    # If not, then raise an error.
    else:
        raise ValueError
except ValueError:
    print("The length you entered is not a positive integer.")
