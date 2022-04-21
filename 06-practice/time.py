import math

class time : 
    def __init__(self) :
        self.times = [[0,0,0],[0,0,0]]
    def fix_time(self,item) :
        if item[2] > 60 : 
            item[1] += math.floor(item[2]/60)
            item[2] = item[2]%60
        if item[1] > 60 : 
            item[0] += math.floor(item[1]/60)
            item[1] = item[1]%60
        return item
    def set_time(self,input) :  
        times = input.split(" ")
        for key, value in enumerate(times):
            store = times[key].split(":")
            self.times[key] = self.fix_time([int(store[0]),int(store[1]),int(store[2])])
    def sub(self) : return ":".join([str(abs(self.times[0][0] - self.times[1][0])),str(abs(self.times[0][1] - self.times[1][1])),str(abs(self.times[0][2] - self.times[1][2]))])
    def sum(self) : 
        s = self.fix_time([abs(self.times[0][0] + self.times[1][0]),abs(self.times[0][1] + self.times[1][1]),abs(self.times[0][2] + self.times[1][2])])
        return ":".join([str(s[0]),str(s[1]),str(s[2])])
    def timeToSec(self) : return str((int(self.times[0][0]) * 3600) + (int(self.times[0][1]) * 60) + (int(self.times[0][2]))) + " seconds"
    def secToTime(self,text) : 
        self.times[0][0] = math.floor(int(text)/3600)
        self.times[0][1] = math.floor((int(text) - (self.times[0][0]*3600))/60)
        self.times[0][2] = math.floor((int(text) - (self.times[0][0]*3600)) - (self.times[0][1]*60))
        self.fix_time(self.times[0])
        return ":".join([str(self.times[0][0]),str(self.times[0][1]),str(self.times[0][2])])

instance = time()
while True : 
    choose = int(input("1.sub time\n2.sum time\n3.time to second\n4.second to time\nyour choose : "))
    if choose == 1 : 
        instance.set_time(input("please enter your times(11:56:32 5:12:11) : "))
        print("\n*************\n"+instance.sub()+"\n*************\n")
    elif choose == 2 : 
        instance.set_time(input("please enter your times(11:56:32 5:12:11) : "))
        print("\n*************\n"+instance.sum()+"\n*************\n")
    elif choose == 3 : 
        instance.set_time(input("please enter your time(11:56:32) : "))
        print("\n*************\n"+instance.timeToSec()+"\n*************\n")
    elif choose == 4 : 
        print("\n*************\n"+instance.secToTime(input("please enter your seconds(3800) : "))+"\n*************\n")
    else : break
    