divided = -2147483648
divisor = -1
count = 0
flag = False

if(divided >= 2**31):
    divided = (2**31)-1
if(divisor == 1):
    return divided
if(divisor == -1):
    divided *= -1
    return divided
if(divisor < 0 and divided > 0):
    flag = True
    divisor *= -1
if(divided < 0 and divisor > 0):
    divided *= -1
    flag = True
if(divided < 0 and divisor < 0):
    divided *= -1
    divisor *= -1
while True:
    if(divided < divisor and count == 0):
        print("output:", count)
        break
    divided -= divisor
    count += 1
    if(divided < divisor):
        break
if(flag == True):
    count *= -1
print("output:", count)
