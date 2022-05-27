value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
          50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
num = 20
ans = ""
while num != 0:
    for i in value:
        if(num - i >= 0):
            num -= i
            ans += symbol[i]
            break
print(ans)
# return ans
