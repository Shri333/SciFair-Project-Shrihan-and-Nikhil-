import random

symbols = ["#", "$", "&"]

def symbol1():
    pass1 = input("Enter password (1 symbol): ")
    counter = 0
    rand = random.choice(symbols)
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = random.choice(symbols)
            print(rand)
            counter += 1

def symbol2():
    pass

def symbol3():
    pass

def symbol4():
    pass

def symbol5():
    pass

def symbol6():
    pass

symbol1()
