from collections import Counter
nums = [1,2,1,3,2,5]

count = Counter(nums)
res = []

for key, val in count.items():
    if val == 1:
        res.append(key)

print(res)