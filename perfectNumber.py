num = 28

# res = []

# for n in range(1, num):
#     if num % n == 0:
#         res.append(n)

# print(sum(res))

# the above code is correct but leads to MLE problems, so to avoid this, we only check root of num

if num <= 1:
    print(False)

total = 1     # 1 is always a divisor, so total starts from 1

i = 2

while i * i <= num:
    if num % i == 0:
        total += i
        if i != num // i:
            total += num // i

    i += 1

print(total)
