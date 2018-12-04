#Input should be modified from what the AoC download is, from:
#[1518-##-## ##:##] word word word
#To:
#1518######## word word word
#And sorted.

nights = {"0000":1}
sleeps = {"0000":[0]*60}

asleep = 0

with open("tmp6.txt","r") as f:
  for line in f:
    words = line.split()
    if len(words) > 3:
      guard = words[2][1:]
      if guard not in nights.keys():
        nights[guard] = 1
        sleeps[guard] = [0]*60
      else:
        nights[guard] += 1
      asleep = 1
    else:
      for i in range(int(words[0][10:12]),60):
        sleeps[guard][i] += asleep
      asleep *= -1


highestGuard = '0000'
mostMinutes = 0
for key in nights.keys():
  if sum(sleeps[key]) > mostMinutes:
    mostMinutes = sum(sleeps[key])
    highestGuard = key
print highestGuard
print nights[highestGuard]
print sleeps[highestGuard]
print mostMinutes
#I'm printing more than I have to, but it's fun to see the results
