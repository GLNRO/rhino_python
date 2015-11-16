import rhinoscriptsyntax as rs


xPos = 5
yPos = 5
xSpeed = 5
ySpeed = 8

boundary = 90

for t in range(time):
    xPos += xSpeed
    yPos += ySpeed
    
    if xPos < 0 or xPos > boundary:
        xSpeed *= -1
    if yPos < 0 or yPos > boundary:
        ySpeed *= -1
        
a = rs.AddSphere([xPos,yPos,0],5)