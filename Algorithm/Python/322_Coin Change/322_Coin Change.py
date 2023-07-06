amount = 6249
coins = [186, 419, 83, 408]
ans = 0
coins = sorted(coins)
for i in range(len(coins)-1, -1, -1):
    if(amount < coins[i]):
        continue
    else:
        ans = ans + (amount // coins[i])
        amount = amount % coins[i]
if(amount != 0):
    ans = -1
print(ans)
