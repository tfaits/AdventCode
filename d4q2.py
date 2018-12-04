#Practically the same script as d4q1.py
#Just changing the reading/output bit at the end

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
worstMinute = 60
for key in nights.keys():
 for i in range(0,60):
  if sleeps[key][i] > mostMinutes:
    mostMinutes = sleeps[key][i]
    worstMinute = i
    highestGuard = key
print "Worst guard:", highestGuard
print "Their worst minute:", str(worstMinute)
print "How many times asleep then:", str(mostMinutes)
print nights[highestGuard]
print sleeps[highestGuard]
