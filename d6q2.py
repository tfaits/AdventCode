X = [] #initialize x coord list
Y = [] #initialize y coord list
#Read through input, appending x/y coords as ints
with open("D6Q1.txt","r") as f:
  for line in f:
    a,b = line.strip().split(', ')
    X.append(int(a))
    Y.append(int(b))
#calculate distance at upper left corner (0,0):
maxDist = sum(X) + sum(Y)

Xdist = [0]*max(X) #initialize a list of horizontal distances
Ydist = [0]*max(Y) #initialize a list of vertical distances

for i in range(1,max(X)):
  Xdist[i] = Xdist[i-1] - sum(x >= i for x in X) + sum(x < i for x in X) #subtract 1 for each one you get closer to, add one if you go farther

for j in range(1,max(Y)):
  Ydist[j] = Ydist[j-1] - sum(y >= j for y in Y) + sum(y < j for y in Y) #subtract 1 for each you get closer to, add one if you go farther

goodArea = 0
for i in range(1,max(X)):
  for j in range(1,max(Y)):
    distance = maxDist + Xdist[i] + Ydist[j] #Manhattan distance is just X+Y, independently.
    if distance < 10000:
      goodArea += 1
print goodArea
