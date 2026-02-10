nums = [1,3]
target = 1

ans = []

for i, val in enumerate(nums):
    if val == target:
        ans.append(i)

if not ans:
    ans = [-1, -1]

ans = [ans[0], ans[-1]]


print(ans)
# print(len(ans))