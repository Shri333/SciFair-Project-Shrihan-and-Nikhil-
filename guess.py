import random

symbols = ["#", "$", "&"]


def random_algorithm(length):
    pass1 = input("Enter password (" + str(length) + " symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(length))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(length))
            print(rand)
            counter += 1


random_algorithm(3)
