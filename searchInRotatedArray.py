# class Solution(object):
#     def search(self, nums, target):

#         if target in nums:
#             return True
#         else:
#             return False
        
#  the above solution is also correct, but leetcode accepts binary search approach for this problem

nums = [2,5,6,0,0,1,2]
target = 0

left = 0
right = len(nums) - 1

mid = (left + right)//2

while left <= right:
    if target == nums[mid]:
        print(target)
        break

    elif nums[left] == nums[mid] == nums[right]:
        left += 1
        right -= 1

    elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:
        if nums[mid] <= target < nums[right]:
            left = mid + 1
        else:
            right = mid - 1

print(False)