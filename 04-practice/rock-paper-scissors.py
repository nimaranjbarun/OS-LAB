import random
data = [[1,2,0,"🪨"],[2,0,1,"📜"],[0,1,2,"✂️"]]
log = []
win = [0,0]
for x in range(5) :
    log.append([int(input("Enter your choice (0: rock , 1: paper , 2: scissors) : ")),random.randint(0, 2)])
    if data[log[x][0]].index(log[x][1]) != data[log[x][1]].index(log[x][0]):
        win[0] += data[log[x][0]].index(log[x][1])
        win[1] += data[log[x][1]].index(log[x][0])
    if data[log[x][0]].index(log[x][1]) == 0 : print(data[log[x][0]][3]," VS ",data[log[x][1]][3]," ==> lose ")
    elif data[log[x][0]].index(log[x][1]) == 1 : print(data[log[x][0]][3]," VS ",data[log[x][1]][3]," ==> win ")
    else : print(data[log[x][0]][3]," VS ",data[log[x][1]][3]," ==> equal ")
if win[0] > win[1] : print("\n\n=============================\nYou Win 🏆\n=============================\n")
elif win[0] == win[1] : print("\n\n=============================\nThe Two Sides Were Equal 🏳\n=============================\n")
else : print("\n\n=============================\nYou Lose 🤦\n=============================\n")
