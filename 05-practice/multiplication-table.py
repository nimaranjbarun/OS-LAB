def make_multiplication_table(x,y) :
    for i in range(x) :
        for j in range(y) : print((i+1)*(j+1),end=" ")
        print()
make_multiplication_table(int(input("enter row : ")),int(input("enter col : ")))