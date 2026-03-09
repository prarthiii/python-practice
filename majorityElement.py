from collections import Counter
nums = [3,2,3]

check = len(nums)/2

count = Counter(nums)

# for c in count:
#     if count[c] > check:
#         print(c)
#         break


# we can use the below method as well directly instead of looping through a dictionary data structure(count)

for num, frequency in count.items():
    if frequency > check:
        print(num)
        break