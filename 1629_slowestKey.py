releaseTimes = [1, 2]
keysPressed = "ba"
maxNum = releaseTimes[0]
maxIndex = 0
for i in range(1, len(releaseTimes)):
    if maxNum < (releaseTimes[i] - releaseTimes[i-1]):
        maxNum = releaseTimes[i] - releaseTimes[i-1]
        maxIndex = i
    elif(maxNum == (releaseTimes[i] - releaseTimes[i-1])):
        if(keysPressed[maxIndex] <= keysPressed[i]):
            maxIndex = i
print(keysPressed[maxIndex])
