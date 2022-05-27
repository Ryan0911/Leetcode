# Dynamic programming

s = "cbbd"
temp = []
max = s[0]
# initialize array
for i in range(0, len(s)):
    temp.append([])
    temp[i] = [False] * len(s)
for i in range(0, len(temp)):
    temp[i][i] = True
for i in range(1, len(temp)):
    if(s[i] == s[i-1]):
        temp[i-1][i] = True
        if(len(max) <= 2):
            max = s[i-1:i+1]
length = len(temp)
for i in range(length-2, -1, -1):
    for j in range(length-1, i, -1):
        if(s[i] == s[j] and temp[i+1][j-1] == True):
            temp[i][j] = True
            if(len(max) < len(s[i:j+1])):
                max = s[i:j+1]
print(max)
