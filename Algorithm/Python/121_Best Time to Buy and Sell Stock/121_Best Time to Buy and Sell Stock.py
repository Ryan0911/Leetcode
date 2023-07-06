prices = [7, 1, 5, 3, 6, 4]
max_profit = 0
buy = prices[0]

for i in range(1, len(prices)):
    if(max_profit < prices[i] - buy):
        max_profit = prices[i] - buy
    if(prices[i] < buy):
        buy = prices[i]
print(max_profit)
