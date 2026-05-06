nums = [3,1,2,4]

# res1 = []
# res2 = []

# for n in nums:
#     if n % 2 == 0:
#         res1.append(n)
#     else:
#         res2.append(n)

# print(res1+res2)

# this method takes 10ms to run and is not very feasible, the below method runs in 1ms and is ideal for this problem

s = 0
n = len(nums)

for i in range(n):
    if nums[i] % 2 == 0:
        nums[s] , nums[i] = nums[i], nums[s]
        s+=1

print(nums)