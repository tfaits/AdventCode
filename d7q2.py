first = []
second = []
f = open("D7Q1.txt","r")
for line in f:
  first.append(line.split()[1])
  second.append(line.split()[7])

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

work1 = 0
work2 = 0
work3 = 0
work4 = 0
work5 = 0
elf1 = False
elf2 = False
elf3 = False
elf4 = False
elf5 = 0

time = 0

while len(first) > 0:
    if len(first) == 1:
        lastOne = ord(second[0]) - 5
    if elf1 and work1 == 0:
        idx = 0
        while idx < len(first):
            if first[idx] == elf1:
                first.pop(idx)
                second.pop(idx)
            else:
                idx += 1
        elf1 = False
    if elf2 and work2 == 0:
        idx = 0
        while idx < len(first):
            if first[idx] == elf2:
                first.pop(idx)
                second.pop(idx)
            else:
                idx += 1
        elf2 = False
    if elf3 and work3 == 0:
        idx = 0
        while idx < len(first):
            if first[idx] == elf3:
                first.pop(idx)
                second.pop(idx)
            else:
                idx += 1
        elf3 = False
    if elf4 and work4 == 0:
        idx = 0
        while idx < len(first):
            if first[idx] == elf4:
                first.pop(idx)
                second.pop(idx)
            else:
                idx += 1
        elf4 = False 
    if elf5 and work5 == 0:
        idx = 0
        while idx < len(first):
            if first[idx] == elf5:
                first.pop(idx)
                second.pop(idx)
            else:
                idx += 1
        elf5 = False             
    for letter in range(0,len(alphabet)):
        if alphabet[letter] in first and alphabet[letter] not in second and alphabet[letter] not in [elf1,elf2,elf3,elf4,elf5]:
            if work1 == 0:
                elf1 = alphabet[letter]
                work1 = 61 + letter
            elif  work2 == 0:
                elf2 = alphabet[letter]
                work2 = 61 + letter
            elif  work3 == 0:
                elf3 = alphabet[letter]
                work3 = 61 + letter
            elif  work4 == 0:
                elf4 = alphabet[letter]
                work4 = 61 + letter
            elif  work5 == 0:
                elf5 = alphabet[letter]
                work5 = 61 + letter
    if work1 > 0:
        work1 -= 1
    if work2 > 0:
        work2 -= 1
    if work3 > 0:
        work3 -= 1
    if work4 > 0:
        work4 -= 1
    if work5 > 0:
        work5 -= 1
    time += 1

print time + lastOne
