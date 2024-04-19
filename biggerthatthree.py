ask1 = int(input("Number 1: "))
ask2 = int(input("Number 2: "))
ask3 = int(input("Number 3: "))

if (ask1 > ask2 and ask1 > ask3):
    print(ask1)
elif (ask2 > ask1 and ask2 > ask3):
    print(ask2)
else:
    print(ask3)