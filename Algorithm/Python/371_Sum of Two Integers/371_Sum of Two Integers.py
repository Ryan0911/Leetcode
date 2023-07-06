a = 2
b = 3
while(b != 0):
    carry = (a & b) << 1
    a = a ^ b
print(a)
