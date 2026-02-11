# n =1
# k= 1

# templ = []

# for i in range(1,n+1):
#     for j in range(i+1,n+1):
#         new = [i,j]
#         templ.append(new)

# print(templ)

# the above method fails for more than 3 inputs

def combine(n,k):
    res =[]

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(start, n+1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return res