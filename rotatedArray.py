nums = [1]
target = 0


def search():
    for i, val in enumerate(nums):
        if target == val:
            return i
        if target not in nums:
            return -1

print(search())