from collections import Counter

nums1 = [1,2,2,1]
nums2 = [2]


count = Counter(nums2)
res = []

for n1 in nums1:
    if count[n1] > 0:
        res.append(n1)
        count[n1] -= 1
print(res)