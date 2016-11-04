symbols = ["#", "$", "&"]

password = input("Enter password (1 symbol): ")

if len(password) == 1:
    for i in range(0,len(password)):
        for j in symbols:
            if password[i] == j:
                print("OK")
            else:
                print("BAD")
else:
    print("BAD")
