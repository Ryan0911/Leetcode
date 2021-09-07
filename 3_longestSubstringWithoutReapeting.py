s = ""
length = 0
temp = ""
max = 0
for i in range(0, len(s)):
    if(s[i] not in temp):
        temp += s[i]
    elif(s[i] in temp):
        for count in range(0, len(temp)):
            if(temp[count] == s[i]):
                temp = temp[count+1:]
                temp += s[i]
                break
    if(len(temp) >= max):
        max = len(temp)
print(max)
