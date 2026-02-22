nums = [1,0,1,1]
k = 1

seen = {}

for i in range(len(nums)):
    if nums[i] in seen:
        if i - seen[nums[i]] <= k:
            print("true")

    seen[nums[i]] = i
 