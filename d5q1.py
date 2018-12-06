f = open("D5Q1.txt","r")
word = f.readline().strip()
polymer = []
for i in range(0,len(word)):
  polymer.append(word[i])

wordLen = len(polymer) + 1
while len(polymer) != wordLen:
  i = 0
  wordLen = len(polymer)
  while i < len(polymer) - 1:
    if (polymer[i].upper() == polymer[i+1].upper()) and (polymer[i] != polymer[i+1]):
      polymer.pop(i)
      polymer.pop(i)
    else:
      i += 1

print len(polymer)
