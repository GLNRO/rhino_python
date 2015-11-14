import rhinoscriptsyntax as rs
#randomness
import random as r
r.seed(seed)
#class

class Walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def display(self):
        shape = rs.AddPoint(self.x,self.y,0)
        return shape
        
    def step(self):
        choice = r.randint(0,3)
        if(choice == 0):
            self.x += 1
        elif(choice == 1):
            self.y += 1
        elif(choice == 2):
            self.x -= 1
        else:
            self.y -= 1
#time
w = Walker()
pList = []
for t in range(time):
    w.step()
    pList.append(w.display())
    
a = pList
print pList