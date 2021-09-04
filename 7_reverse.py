x = 120

if x < 0:
    y = -1 * int(str(-x)[::-1])
else:
    y = int(str(x)[::-1])
if y > 2**31 or y < -2**31:
    y = 0
print(y)
