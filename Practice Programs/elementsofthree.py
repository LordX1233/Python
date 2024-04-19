#List1
mylist = [1,2,3,4,5]
print(mylist[0:3])

#List2
print(mylist[-3: ])

#List3
mylist2 = [1,2,3,4,5,6,7,8,9,10]
print(mylist2[: : 2])

#List4
mylist3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(mylist3[6: : 2])

#List5
mylist2.reverse()
print(mylist2)

#List6
length = int(len(mylist)/2)
print(mylist[length: length + 1])