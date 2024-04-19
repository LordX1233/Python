cuts = int(input("Number: "))
totalsquares = 0
number1 = 1
number2 = 2
multiple1 = 2
multiple2 = 0

for i in range(cuts):
    totalsquares = number1 * number2
    if (multiple1 == 2): 
        number1 += 1
        multiple1 = 0
    if (multiple2 == 2): 
        number2 += 1
        multiple2 = 0 
    multiple1 += 1
    multiple2 += 1
print(totalsquares)