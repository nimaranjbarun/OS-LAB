cnt = int(input("please enter your diamond height : "));
for x in range(-(cnt-1),cnt) : print((abs(x)*" ")+((2*(((cnt-1)-abs(x)%cnt))+1)*"*"));