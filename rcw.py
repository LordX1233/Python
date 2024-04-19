accounts = [[1,5],[7,3,6],[3,5],[1,3],[7,3],[3,5,8]]

x = 0
y = 0

for i in range (len(accounts)):
    for e in range(len(accounts[i])):
        x += accounts[i][e]
        #print(x)
        if (x > y):
            y = x
    x = 0
print(y)