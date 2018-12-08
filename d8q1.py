with open("D8Q1.txt","r") as f:
  thing = f.readline().strip().split()

def runMetaSum(stuff,total):
    children = int(stuff[0])
    metadata = int(stuff[1])
    stuff = stuff[2:]
    for j in range(0,children):
      stuff,total = runMetaSum(stuff,total)
    for i in range(0,metadata):
      total += int(stuff[i])
    return(stuff[metadata:],total)

finalstuff,finaltotal = runMetaSum(thing,0)
print finaltotal
