with open("D8Q1.txt","r") as f:
  thing = f.readline().strip().split()

def runMetaSum(stuff):
    total = 0
    children = int(stuff[0])
    metadata = int(stuff[1])
    stuff = stuff[2:]
    if children == 0:
      for i in range(0,metadata):
        total += int(stuff[i])
    else:
        childValues = []
        for j in range(0,children):
          stuff,child = runMetaSum(stuff)
          childValues.append(child)
        for i in range(0,metadata):
          if int(stuff[i]) < children + 1:
            total += childValues[int(stuff[i])-1]
    return(stuff[metadata:],total)

finalstuff,finaltotal = runMetaSum(thing)
print finaltotal
