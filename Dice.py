import random

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

TotalRoll = 0

Dice = int(input("How many rolls do you want? "))

while TotalRoll < Dice:
  ThisRoll = random.randint(1,6)
  TotalRoll += 1
  if ThisRoll == 1:
  	ones += 1
  elif ThisRoll == 2:
    twos += 1
  elif ThisRoll == 3:
    threes += 1
  elif ThisRoll == 4:
    fours += 1
  elif ThisRoll == 5:
    fives += 1
  else:
    sixes += 1

  print ("Percentages: ")
  print("1s - " + str(ones/(TotalRoll)*100) + "%")
  print("2s - " + str(twos/(TotalRoll)*100) + "%")
  print("3s - " + str(threes/(TotalRoll)*100) + "%")
  print("4s - " + str(fours/(TotalRoll)*100) + "%")
  print("5s - " + str(fives/(TotalRoll)*100) + "%")
  print("6s - " + str(sixes/(TotalRoll)*100) + "%")

  print ("Roll number " + str(TotalRoll) + "\n" + "Dice rolled: " + str(ThisRoll))
  print ("1s = " + str(ones))
  print ("2s = " + str(twos))
  print ("3s = " + str(threes))
  print ("4s = " + str(fours))
  print ("5s = " + str(fives))
  print ("6s = " + str(sixes))