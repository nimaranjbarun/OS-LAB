from array import array
import random

WordsList = ["apple","yousefi","golbahar","tehran","pride","samand","chekbar","hamed","bahram","iran","asus","lenovo","oil","emad","class","heravi"]

index = random.randint(0,15)
word =WordsList[index]

# word = random.choise(WordsList)

userwordtrue =[]
joon = 5

while(True) :
    for i in range(len(word)) :
        if word[i] in userwordtrue :
             print(word[i] , end="")
        else :     
             print("-", end="")
        
    print("\n please insert a character :")
    
    userword = input()

    if len(userword) == 1 :
        if userword in word :
            userwordtrue.append(userword)
            print("\n✅\n")   
            
        else:
            joon -= 1
            print("\n❌\n")   
    
        if joon == 0 :
            print("Game Over")
            break
        
    else :
        print("please insert a character")        
    
    if sorted(list(word)) == sorted(userwordtrue) :
        print("YOU WIN , THE WORD IS \""+word+"\"")
        break    