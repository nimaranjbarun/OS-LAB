from enum import unique
import random,collections

from click import option
win,log = [0,0,0],[0,0,0] 
options,hand = ["user","computer1","computer2"],["✋","🤚"]
for x in range(5) : 
    log[0] = int(input("Enter your choice (0: ✋ , 1: 🤚) : "))
    log[1] = random.choice([0,1])
    log[2] = random.choice([0,1])
    unique_index = [log.index(item) for item, count in collections.Counter(log).items() if count == 1];
    if len(unique_index) > 0 : win[unique_index[0]] += 1
    print(hand[log[0]]+" "+hand[log[1]]+" "+hand[log[2]])
winner = [idx for idx, val in enumerate(win) if val == int(max(win)) & val in win[:idx]]
if(len(winner) == 2) : print("\n\n=============================\nEveryone Was Equal\n=============================\n")
elif(len(winner) == 1 and (win[winner[0]] == max(win))) : print("\n\n=============================\n"+options[win.index(max(win))]+" And "+options[winner[0]]+ " Were Win 🏆\n=============================\n")
else : print("\n\n=============================\n"+options[win.index(max(win))] + " Was Win 🏆\n=============================\n")