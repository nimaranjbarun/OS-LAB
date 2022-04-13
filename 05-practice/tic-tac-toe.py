from posixpath import split
import random
from termcolor import colored
import time

type_game,game,users,options,store,start = int(input("1. user VS user\n2. user VS computer\nchoose your option : ")),[['-','-','-'],['-','-','-'],['-','-','-']],[[[],[]],[[],[]]] , [colored('X','blue'),colored('O','green')] ,[0,0],time.time();

def print_board() : 
    for row in game : 
        for column in row : print(column,end = " ")
        print()
        
def set_board(x) :
    global game,store
    if type_game == 1 or x%2 == 0 : store = input("user "+(str((x%2)+1))+" : ").split(" ")
    elif x%2 == 1 : 
        store = [random.randint(0,2),random.randint(0,2)]
        print("computer : "+str(store[0])+" "+str(store[1]))
    while game[int(store[0])][int(store[1])] != '-'  or int(store[1]) > 2  or int(store[0]) > 2 : 
        if type_game == 1: store = input("your input is incorrect . please enter your input again\nuser "+(str((x%2)+1))+" : ").split(" ")
        else : store = [random.randint(0,2),random.randint(0,2)]
    game[int(store[0])][int(store[1])] = options[x%2]
    users[x%2][0].append(int(store[0]))
    users[x%2][1].append(int(store[1]))

def print_winner(winner) : 
    print("\n****************\nafter "+(str((time.time() - start)))+" seconds , "+winner+" 🏆\n****************");
    exit()
     
def check() : 
    if (users[0][0].count(0) == 3 or users[0][0].count(1) == 3 or users[0][0].count(2) == 3 or users[0][1].count(0) == 3 or users[0][1].count(1) == 3 or users[0][1].count(2) == 3) : print_winner("user1 win")
    elif ((game[0][0] == game[1][1] == game[2][2] == colored('X','blue')) or (game[0][2] == game[1][1] == game[2][0] == colored('X','blue'))) : print_winner("user1 win")
    elif (users[1][0].count(0) == 3 or users[1][0].count(1) == 3 or users[1][0].count(2) == 3 or users[1][1].count(0) == 3 or users[1][1].count(1) == 3 or users[1][1].count(2) == 3) : 
        if type_game == 1 : print_winner("user2 win")
        else : print_winner("computer win")
    elif ((game[0][0] == game[1][1] == game[2][2] == colored('O','green')) or (game[0][2] == game[1][1] == game[2][0] == colored('O','green'))) : 
        if type_game == 1 : print_winner("user2 win")
        else : print_winner("computer win")          

for x in range(9) :
    set_board(x)
    print_board()
    if(x >= 4) : check()
print("\n****************\nafter "+(str((time.time() - start)))+" seconds , no one wins 🏳\n****************")