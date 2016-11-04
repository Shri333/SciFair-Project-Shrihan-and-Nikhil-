symbols = ["#", "$", "&"]

password = input("Enter password (1 symbol): ")

if len(password) == 1:
    print("OK")
else:
    print("BAD")
