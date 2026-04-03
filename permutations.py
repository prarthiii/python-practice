nums = [1,2,3]

res = []

def backtrack(path):
    if len(path) == len(nums):
        res.append(path[:])
        return
    
    for n in nums:
        if n in path:
            continue

        path.append(n)
        backtrack(path)
        path.pop()

backtrack([])
