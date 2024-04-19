word1 = str(input("Word1: "))
word2 = str(input("Word2: "))
newword = ""

for i in range(len(word1) + len(word2)):
    if(i < len(word1)):
        newword += (word1[i])
    if(i < len(word2)):
        newword += (word2[i])

print(newword)