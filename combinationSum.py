from collections import Counter
nums = [1,2,2,4]
length = len(nums)
count = Counter(nums)

for i in range(1, len(nums)+ 1):
    if count[i] == 2:
        duplicate = i
    if count[i] == 0:
        missing = i

print([duplicate, missing])