#list1 = [1, 2, 4]
#list2 = [1, 3, 4]
list1 = []
list2 = [0]

num1 = 0
num2 = 0
ans = []
if(len(list1) == 0 and len(list2) != 0):
    print(list2)
elif(len(list2) == 0 and len(list1) != 0):
    print(list1)
else:
    while True:
        if(num1 == len(list1) or num2 == len(list2)):
            break
        if(list1[num1] < list2[num2]):
            ans.append(list1[num1])
            num1 += 1
        elif(list1[num1] == list2[num2]):
            ans.append(list1[num1])
            ans.append(list1[num1])
            num1 += 1
            num2 += 1
        else:
            ans.append(list2[num2])
            num2 += 1
    for i in range(num1, len(list1)):
        ans.append(list1[i])
    for i in range(num2, len(list2)):
        ans.append(list2[i])
    print(ans)
