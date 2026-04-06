nums = [1,2,3,4]

# nums.sort(reverse=True)
# nums = nums[:3]

# one = nums[0]
# two = nums[1]
# three = nums[2]

# print(one*two*three)

# the above solution fails for negative values

prod1 = nums[0]*nums[1]*nums[-1]
prod2 = nums[-1]*nums[-2]*nums[-3]

maximum = max(prod1, prod2)