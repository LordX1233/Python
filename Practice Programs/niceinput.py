file = open('stringkey.txt', 'r')
counter = 0
checked = False
vowels = 0
for line in file:
    checked = False
    for i in range(len(line)):
        if ("a" in line[i] or "e" in line[i] or "i" in line[i] or "o" in line[i] or "u" in line[i]):
            vowels += 1
        if (i != len(line) - 1):
            if ("ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line):
                if (line[i] == line[i+1] and checked == False):
                    counter += 1
                    checked = True     
    
    if (vowels < 3 and checked):
        counter -= 1;
    vowels = 0
print(counter)