ask = str(input("Do you want to calculate? T/F: "))

while (ask.lower() == 't' or ask.lower() == "true"):
    operator = str(input("Your operator: "))
    while ((operator != "+") and (operator != "-") and (operator != "*") and (operator != "/")):
        print ('Thats not an appropiate operator')
        operator = str(input("Your operator: "))
        
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    if (operator == "+"):
        answer = num1 + num2
        print("Answer:" ,answer,)
        ask = str(input("Do you want to calculate? T/F: "))
        
    elif (operator == "-"):
        answer = num1 - num2
        print("Answer:" ,answer,)
        ask = str(input("Do you want to calculate? T/F: "))
        
    elif (operator == "*"):
        answer = num1 * num2
        print("Answer:" ,answer,)
        ask = str(input("Do you want to calculate? T/F: "))
        
    elif (operator == "/"):
        answer = num1 / num2
        print("Answer:" ,answer,)
        ask = str(input("Do you want to calculate? T/F: "))
    