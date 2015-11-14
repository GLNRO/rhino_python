#Generates a 3d Walker

import rhinoscriptsyntax as rs
import random as r
r.seed(seed)

class Walker:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        
    def display(self):
        shape = rs.AddPoint(self.x,self.y,self.z)
        return shape
        
    def step(self):
        choice = r.randint(0,5)
        if(choice == 0):
            self.x += 1
        elif(choice == 1):
            self.y += 1
        elif(choice == 2):
            self.z += 1
        elif(choice == 3):
            self.x -= 1
        elif(choice == 4):
            self.y -= 1
        else:
            self.z -= 1
#time

w = Walker()
pList = []
for t in range(time):
    w.step()
    pList.append(w.display())
    
a = pList
print pList