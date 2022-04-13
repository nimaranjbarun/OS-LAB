def make_chess(x,y) :
    for item in range(x*y) : 
        if (item+1)%y == 0 : print("🟨" if item%2 == 0  else "🟩",end = "\n")
        else : print("🟨" if item%2 == 0  else "🟩",end = "")
    print()
make_chess(int(input("enter row : ")),int(input("enter col : ")))