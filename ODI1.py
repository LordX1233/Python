def protest(x, y):
    number = 1
    unique_count = 0
    changes = 0
    
    y.sort()
    
    if (x[1] == 1):
        for i in range(x[0] - 1):
            if (y[i] != y[i+1]):
                number += 1
        print(number)
        
    if (x[1] == 2):
        sizesorted = sorted(y,key=y.count,reverse=True)
        if (len(set(sizesorted)) != x[2]):
            while (unique_count != x[2]):
                sizesorted.pop()
                changes += 1 
                unique_count = len(set(sizesorted))   
        print(changes)
            
protest(list(map(int, input().split())), list(map(int, input().split())))