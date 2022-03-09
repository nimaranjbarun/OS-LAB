while True :
    sides = [input("a : "),input("b : "),input("c : ")]
    if (sides[0]+sides[1] > sides[2]) & (sides[0]+sides[2] > sides[1]) & (sides[1]+sides[1] > sides[0]) : 
        print("Yes")
    else : print("No")
    if input("continue ? (y/n) : ") == "n" : 
        exit('Bye!') 
    