password = str(input("Password: "))
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','"','<',',','>','.','?','/']

if not (password == password.lower()):
    if any(char.isdigit() for char in password):    
        if any(substring in password for substring in symbols):    
            if len(password) >= 10:
                print ("Your password is secure")
            else:
                raise SyntaxError("Your password is not long enough")
        else:
            raise SyntaxError("Your password does not contain symbols")
    else:
        raise SyntaxError("Your password does not contain a number")
else:
    raise SyntaxError("Your password does not contain an uppercase")