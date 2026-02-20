nums = [2,14,18,22,22]

# def check(nums):

#     res = 0

#     for n in nums:
#         print(f"{n} count = {nums.count(n)}")
#         if nums.count(n) >= 2:
#             res += 1


#     if res >= 2:
#         return True
#     else:
#         return False
#     # print(n)
# print(check(nums))

# the complexity of above solution is O(n2) as the count() function is declare inside the function, so we need to use set
# so above method fails even tho all test cases pass!

seen = set()

for n in nums:
    if n in seen:
        print(True)
    seen.add(n)

print("false")