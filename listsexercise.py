list = []
list2 = []
list3 = []
list4 = []
list5 = []

for i in range(1, 101):
        list.append(i)
print(list)

for i in range(len(list)):
    if (list[i] % 2 == 0):
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)

for i in range(len(list2)):
    if (list2[i] % 5 != 0):
        list4.append(list2[i])
print(list4)

for i in range(len(list3)):
    if (list3[i] % 5 != 0):
        list5.append(list3[i])
print(list5)