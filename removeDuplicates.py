def dups():

    nums = [1,1,2]
    k = 0
    seen = set()

    for n in nums:
        if n not in seen:
            seen.add(n)
            nums[k] = n
            k += 1

    return k

print(dups())