s = "PAYPALISHIRING"
numRows = 3
s_list = ["" for i in range(numRows)]
count = 0
flag = False
if numRows == 1:
    print(s)
for i in s:
    if(count == numRows-1):
        flag = True
    elif(count == 0):
        flag = False
    s_list[count] = s_list[count] + i

    if(flag == True):
        count = count - 1
    else:
        count = count + 1
for i in range(numRows):
    print(s_list[i])
