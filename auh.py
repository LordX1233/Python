# P1
# number = int(input("Number: "))
# y = 0
# x = str(number)
# for i in range(len(x)):
#     y = y + int(x[i])
# print (y)

# P2
# name = str(input("Your name: "))
# names = name.lower()
# duplicates = []
# amountofname = [i for i in names]
# for i in range(len(amountofname)):
#     for x in range(len(amountofname)):
#         if i == x:
#             break
#         elif amountofname[i] == amountofname[x] and amountofname[x] not in duplicates:
#             duplicates.append(amountofname[x])
#             print("Letter: " + amountofname[i]) 
#             break
    

# P3
# list = ["apple", "banana", "cherry", "Booze", "zoomy"]
# list2 = []
# for i in range(len(list)):
#     list2.append(list[(len(list))-i-1])
# print (list2)


# P4
# number2 = int(input("Number: "))
# y = 0
# x = str(number2)
# for i in range(len(x)):
#     y = y + int(x[i])**len(x)
# if (y == number2):
#     print("Its an armstrong number")


# P5
# line = []
# size = int(input("Size: "))
# for i in range(size):
#     for x in range(size):
#         line.append("#")
#     print(*line)
#     line.clear()


# P6
# line = []
# efs = 0
# ifs = 1
# check = False
# height = int(input("Height: "))
# for i in range(height):
#     for x in range(1 + efs):
#         for y in range(height - ifs):
#             if i == (height-1):
#                 check = True
#             if (check == False):
#                 line.append(" ")
#         check = True
#         line.append("#")
#     print(*line)
#     ifs += 1
#     efs += 2
#     line.clear()
#     check = False

# P7
# line = []
# height = int(input("Height: "))
# length = int(input("Length: "))
# for i in range(height):
#     for x in range(length):
#         line.append("#")
#     print(*line)
#     line.clear()