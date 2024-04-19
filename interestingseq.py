numbers = []

for i in range(10000):   
    egg = i + 1 
    while egg > 0:
        numbers.append(egg)
        egg -= 1
#print(numbers)

while True:
    ask2 = int(input("Number 2: "))
    print(numbers[ask2-1])
    ask3 = input("Break? ")
    if (ask3 == "y"):
        break