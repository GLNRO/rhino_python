#Generates a 3d Walker

import rhinoscriptsyntax as rs
import random as r
r.seed(seed)


pList = []
for n in range(count):
    rand = r.gauss(mean,sd)
    rand2 = r.gauss(mean,sd)
    rand3 = r.gauss(mean,sd)
    pList.append(rs.AddPoint(rand,rand2,rand3))
    
a = pList
