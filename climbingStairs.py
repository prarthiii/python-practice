n = 2

if n <=2:
    print(n)

prev1 = 1
prev2 = 2

for i in range(3, n+1):
    curr = prev1 + prev2
    prev1 = prev2
    prev2 = curr

print(prev2)