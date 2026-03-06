nums = [1,1,0,1,1,1]

count = 0
max_count = 0

for n in nums:
    if n == 1:
        count += 1
        max_count = max(max_count, count)
    if n == 0:
        count = 0

print(max_count)