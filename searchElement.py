nums = [1,3,5,6]
target = 2

temp = nums.copy()

for i, val in enumerate(nums):
    if val == target:
        print(i)

if target not in nums:
    nums.append(target)  
    nums.sort()   
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)  

print(nums)