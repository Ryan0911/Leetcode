l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
l3 = []
length = 0
if(len(l1) < len(l2)):
    length = len(l2)
else:
    length = len(l1)
for i in range(0, length):
    try:
        l3.append(l1[i]+l2[i])
    except:
        if(len(l1) > len(l2)):
            l3.append(l1[i])
        else:
            l3.append(l2[i])
for i in range(0, len(l3)):
    try:
        l3[i+1] = int(l3[i+1]+l3[i]/10)
    except:
        l3.append(int(l3[i]/10))
    l3[i] = l3[i] % 10
print(l3)
