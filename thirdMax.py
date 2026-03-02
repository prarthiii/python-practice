nums = [1,1,2]


if len(nums) <= 2:
    print(max(nums))


nums = set(nums)
nums = list(nums)

nums.sort(reverse=True)

if len(nums) <= 2:
    print(max(nums))

print(nums[2])