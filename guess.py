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
    pass1 = input("Enter password (2 symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(2))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(2))
            print(rand)
            counter += 1

def symbol3():
    pass1 = input("Enter password (3 symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(3))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(3))
            print(rand)
            counter += 1

def symbol4():
    pass1 = input("Enter password (4 symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(4))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(4))
            print(rand)
            counter += 1

def symbol5():
    pass1 = input("Enter password (5 symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(5))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(5))
            print(rand)
            counter += 1

def symbol6():
    pass1 = input("Enter password (6 symbols): ")
    counter = 0
    rand = ''.join(random.choice(symbols) for i in range(6))
    print(rand)
    while True:
        if pass1 == rand:
            print(str(counter) + " attempts")
            break
        else:
            rand = ''.join(random.choice(symbols) for i in range(6))
            print(rand)
            counter += 1

# symbol1()
# symbol2()
# symbol3()
# symbol4()
# symbol5()
# symbol6()
