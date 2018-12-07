steps = []
letters = []
f = open("D7Q1.txt","r")
for line in f:
  steps.append(line.split()[1])
  letters.append(line.split()[7])

assemblyOrder = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while len(steps) > 0:
  if len(steps) == 1:
    lastOne = letters[0]
  for letter in range(0,26):
    if alphabet[letter] not in letters and alphabet[letter] in steps:
      assemblyOrder.append(alphabet[letter])
      i = 0
      while i < len(steps):
        if steps[i] == alphabet[letter]:
          steps.pop(i)
          letters.pop(i)
        else:
          i += 1
      break

print ''.join(assemblyOrder) + lastOne
