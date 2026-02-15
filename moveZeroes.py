nums = [0]

for n in nums:
    if n == 0:
        nums.remove(n)
        nums.append(n)

print(nums)