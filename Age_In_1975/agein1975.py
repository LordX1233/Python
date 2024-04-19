def printAnswer(name, age):
    born_year = 2023 - age;
    differ = born_year - 1975;
    current_year = 2023 - 1975;

    if (differ < 0):
        too_m_or_l = age - current_year
        print(name + ", you are " + too_m_or_l + " year/s too old.")

    elif (differ > 1):
        too_m_or_l = age - current_year
        print(name + ", you are " + -too_m_or_l + " year/s too young.")
    else:
        print(name + ", you were born in 1975!.")

name = str(input("Whats your name?: "))
age = int(input("Whats your age?: "))
printAnswer(name, age);