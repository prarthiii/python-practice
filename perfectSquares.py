n = 12

squares = []
i = 1

while i * i <= n:
    squares.append(i * i)
    i += 1

print(squares)      

dp = [float('inf')] * (n + 1)
dp[0] = 0

for num in range(1, n + 1):
    for sq in squares:
        if sq <= num:
            dp[num] = min(dp[num], dp[num - sq] + 1)

print(dp)
print(dp[n])