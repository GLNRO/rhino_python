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
       randX = r.uniform(-1,1)
       randY = r.uniform(-1,1)
       randZ = r.uniform(-1,1)
     
       
       self.x += randX
       self.y += randY
       self.z += randZ
      
#time

w = Walker()
pList = []
for t in range(time):
    w.step()
    pList.append(w.display())
    
a = pList
print pList