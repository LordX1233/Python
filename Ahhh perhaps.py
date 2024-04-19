# P1

name = str(input("Name: "))
print("P is in your name") if "p" in name else print("P is not in your name")

# P2

list = [2, 65, 4, 355, 213, 32, 43, 8, 9]
age = int(input("Age: "))
number = int(input("Number: "))
x = list.index(number)
if number in list:
     list[x] = (number *  age)
     print(list)

else:
    print("Not Found, List: " + str(list))