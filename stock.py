# prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]

# minele = min(prices)
# print(minele)

# prices = prices[minele:]
# print(prices)

# maxele = max(prices)

# res = maxele-minele
# print(res)

# if not prices:
#     print(0)

# above logic is wrong!

min_price = float('inf')
max_profit = 0

for p in prices:
    if p < min_price:
        min_price = p
        max_profit = max(max_profit, p - min_price)

print(max_profit)