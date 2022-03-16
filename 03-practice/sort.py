arr = input("please Enter your values (like this : 5 6 8 9 1 ) : \n")
arr = [int(i) for i in arr.split(" ") if i!= ""]
if arr == sorted(arr) : print("\n=====================\nList is Sorted\n=====================")
else : print("\n=====================\nList is not Sorted\n=====================")
    