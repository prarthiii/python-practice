nums = [3,0,1]

for _ in nums:
    for n in range(len(nums)+1):
        if n not in nums:
            print(n)