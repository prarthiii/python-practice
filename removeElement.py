# nums = [3,2,2,3]
# val = 3

# temp = []

# for n in nums:
#     if n != val:
#         temp.append(n)

# print(len(temp))

# without creating a new list: (leetcode version)

nums = [3,2,2,3]
val = 3

k = 0

for n in nums:
    if n != val:
        nums[k] = n
        k += 1

print(k)