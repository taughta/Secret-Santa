from random import shuffle

participants = []

#ask how many names there are
print("How many of you guys wanna play?")
numberOfPartsOK = False

while numberOfPartsOK == False:
    try:
        numberOfParts = int(input())
        assert numberOfParts
        numberOfPartsOK = True
    except Exception:
        print("*** INVALID INPUT ***")

# ask for the names and putting them into a list
nameCounter = 1
while numberOfParts > 0:
    try:
        print("Enter the name of player #%i:" %nameCounter)
        nameTemp = str(input())
        assert nameTemp
        participants.append(nameTemp)
        numberOfParts -= 1
        nameCounter += 1
    except Exception:
        print("*** INVALID INPUT ***")

# Creating another list that contains the name of participants MIXED
mixedParts = []
copyCounter = 0
for i in participants:
    mixedParts.append(participants[copyCounter])
    copyCounter += 1

# Mixing the names and verifying that there is no self-pairing

matchList = []
matchCheck = False
while matchCheck == False:
    shuffle(mixedParts)
    matchCounter = 0
    matchList = []
    for i in mixedParts:
        if participants[matchCounter] != mixedParts[matchCounter]:
            goodMatch = True
            matchList.append(goodMatch)
            matchCounter += 1
        else:
            goodMatch = False
            matchList.append(goodMatch)
            matchCounter += 1
    if False in matchList:
        continue
    else:
        matchCheck = True


print(participants, mixedParts)

printCounter = 0

for i in participants:
    name = ("%s" %mixedParts[printCounter])
    fileName = open("%s.txt" %participants[printCounter], "w+")
    fileName.write("""           
                \ /
              -->*<--
                /_\ 
               /_\_\ 
              /_/_/_\ 
              /_\_\_\ 
             /_/_/_/_\ 
             /_\_\_\_\ 
            /_/_/_/_/_\ 
            /_\_\_\_\_\ 
           /_/_/_/_/_/_\ 
           /_\_\_\_\_\_\ 
          /_/_/_/_/_/_/_\ 
               [___]
      
  Suprise him/her on christmas eve :)\n""")
    fileName.write("               %s" %name)
    fileName.close()
    printCounter += 1
