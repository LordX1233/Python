list = [1,3,4,2,2]
list.sort()
for i in range(len(list)):
    if list[i] == list[i-1]:
        print("Number: " + str(list[i])) 