import random

symbols = ["#", "$", "&"]

def symbol1():
    pass1 = input("Enter password (1 symbol): ")
    counter = 0
    rand = random.choice(symbols)
    while pass1 != rand:
        counter += 1
        if pass1 == rand:
            print(counter)
            break
        else:
            rand = random.choice(symbols)

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
