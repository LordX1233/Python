file = open('stringkey.txt', 'r')
counter = 0
for line in file:
    checked = False
    checked2 = False
    checked3 = False
    for i in range(len(line)):
        
        
        
        
        #! Requirement 1 
        if (i != len(line) - 1):
            if (((line[i] + line[i+1])) in line[i+2:] and checked2 == False):
                checked2 = True
        
        #! Requirement 2
        if (i == 14):
            checked3 = True
        if (not checked3):
            if (line[i] == line[i+2] and checked == False and line[i] != line[i+1]):
                checked = True 
                
                
        
                
                 
    if (checked and checked2):
        counter += 1
print(counter)