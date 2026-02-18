n = 14

if n<=0:
    print("false")

for i in [2,3,5]:
    while n % i == 0:
        n //= i

if n == 1:
    print("true")
else:
    print("false")