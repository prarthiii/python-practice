
nums = [4,3,2,7,8,2,3,1]
res=[]
nums.sort()
print(nums)


for n in range(1,len(nums)+1):
    if n not in nums:
        res.append(n)

print(res)