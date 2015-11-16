import rhinoscriptsyntax as rs

pos = [50,50,1]
boundary = 90

vel = velocity

pList = []
for t in range(time):
    
    pos = rs.VectorAdd(pos,vel)
    
    if pos[0] < 0 or pos[0] > boundary:
        vel[0] *= -1
    if pos[1] < 0 or pos[1] > boundary:
        vel[1] *= -1
    
    pt = rs.AddPoint(pos)
    pList.append(pt)

a = pList