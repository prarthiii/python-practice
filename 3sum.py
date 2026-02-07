nums = [-1,0,1,2,-1,-4]

res = set()
n = len(nums)

for i in range(n):
    seen = set()
    target = -nums[i]

    for j in range(1+i, n):
        need = target - nums[j]

        if need in seen:
            triplet = tuple(sorted([nums[i], nums[j], need]))
            res.add(triplet)

        seen.add(nums[j])

print(list(res))