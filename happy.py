n = int(input())
wow2 = n
list = []
while (str(n) != "1"):
    wow = 0
    for i in range(len(str(n))):
        wow += int(str(n)[i])**2
    n = wow
    if (wow2 == n or n in list):
        print("False")
    list.append(n)
print("True")