flag = True
i = input('Please enter the weight or enter the word "exit" to exit the program : ')
if input == "exit" : 
    print("Bye!!!!!")
    exit()
while flag : 
    if i == "exit" : break
    print(float(i) * 2.20462)
    i = input('Please enter the weight or enter the word "exit" to exit the program : ')
print("Bye!!!!!")