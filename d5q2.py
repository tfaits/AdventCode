f = open("D5Q1.txt","r")
word = f.readline().strip()

def collapseWord(word):
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
  return(len(polymer))

bestChar = 'a'
bestLen = 9380
lowerCases = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
  tmp = collapseWord(word.replace(lowerCases[i],"").replace(lowerCases[i].upper(),""))
  if tmp < bestLen:
    bestLen = tmp
    bestChar = lowerCases[i]
    print bestLen
    print bestChar
  else:
    print lowerCases[i], "is not better than the best. It's only", str(tmp), "which is higher than", str(bestLen)
