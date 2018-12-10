f = open("D10Q1.txt","r")
x = []
y = []
xvel = []
yvel = []
for line in f:
  trash,pos,vel = line.strip().split("<")
  x.append(int(pos.split(",")[0]) + 55000)
  y.append(int(pos.split(",")[1].strip("> velocity=")) + 55000)
  xvel.append(int(vel.split(",")[0]))
  yvel.append(int(vel.split(",")[1].strip(">")))

def drawGrid(x,y):
    tmp = []
    for i in range(0,20):
        tmp.append(["."]*80)
    for i in range(0,len(x)):
        tmp[y[i]-min(y)][x[i]-min(x)] = "#"
    for i in range(0,len(tmp)):
        print "".join(tmp[i])

def movePoints(x,velx,y,vely):
    for i in range(0,len(x)):
        x[i] += velx[i]
        y[i] += vely[i]
    return(x,y)

for i in range(0,25000):
  if (max(x) - min(x)) < 81 and (max(y) - min(y)) < 21:
    print " "
    print "~~~~~~~~~~~~~~~~~~~~~~~"
    drawGrid(x,y)
    print i
  x,y = movePoints(x,xvel,y,yvel)
