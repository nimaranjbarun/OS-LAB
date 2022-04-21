import fractions
class operation :
    operations = {"mult" : " * ","divide" : " / ","sum" : " + ","sub" : " - "}
    def __init__(self) : 
        self.inputs = [0,0] 
    def input(self,text) :
        for key in self.operations :
            op = text.split(self.operations[key])
            if len(op) == 2 : 
                self.inputs[0] = fractions.Fraction(int(op[0].split("/")[0]),int(op[0].split("/")[1]))
                self.inputs[1] = fractions.Fraction(int(op[1].split("/")[0]),int(op[1].split("/")[1]))
                return getattr(self,key)()
    def divide(self): return self.inputs[0]/self.inputs[1]
    def sum(self): return self.inputs[0]+self.inputs[1]
    def mult(self): return self.inputs[0]*self.inputs[1]
    def sub(self): return self.inputs[0]-self.inputs[1]
    
test = operation();
while(True) :
    result= test.input(input("write your phrase (like => [5/6 * 2/3] or [5/6 / 2/3] or [5/6 + 2/3] or [5/6 - 2/3] ): "))
    print("\n*****************\nresult : "+str(result)+"\n*****************\n")