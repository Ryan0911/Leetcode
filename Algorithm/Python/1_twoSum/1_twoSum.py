inputArray = [3, 2, 95, 4, -3]
target = 92
temp = 0
flag1 = 0
flag2 = 0
flag_1 = False
flag_2 = False


def p_n(target, flag1, flag2, flag_1, flag_2):
    for index in range(flag1, len(inputArray)):
        if(flag_1 == False):
            temp = target - inputArray[index]
            flag1 = index
            flag_1 = True
        if(flag_1 == True and inputArray[index] == temp):
            flag2 = index
            flag_2 = True
            return flag1, flag2, flag_1, flag_2
    return flag1+1, flag2, flag_1, flag_2


while True:
    flag1, flag2, flag_1, flag_2 = p_n(target, flag1, flag2, flag_1, flag_2)
    if(flag_1 == True and flag2 == False):
        flag_1 = False
        continue
    if(flag_1 == True and flag_2 == True):
        break
print(flag1, flag2)
