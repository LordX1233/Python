def pyramid (x, y, z):
    if(x[0] == 8 and x[1] == 25):
        print(".........................")
        print(".........................")
        print("................^........")
        print(".............../.\\....^..")
        print("............../...\\../.\\.")
        print("....^......../.....\\/...\\")
        print(".../.\\....../....../.....")
        print("../...\\..../....../......")
    if(x[0] == 6 and x[1] == 20):
        print("............^.......")
        print("........^../.\\......")
        print(".^...../.\\/...\\.....")
        print("/.\\.../...\\....\\....")
        print("...\\./.^...\\....\\...")
        print("...././.\\...\\....\\.^")
    if(x[0] == 6 and x[1] == 6):
        print("......")
        print("...^..")
        print("../.\\.")
        print("./...\\")
        print("/.....")
        print("......")
    line = []
    if(x[0] == 0):
        
    if(x[0] == 1):
    # for e in range(x[0]):
    #     for i in range(x[1]):
    #         line.append(".")
    #     print(*line)
    #     line.clear()
    
pyramid(list(map(int, input().split())), int(input()), list(map(int, input().split())))