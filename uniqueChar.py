from collections import Counter

s = "loveleetcode"
count = Counter(s)
print(count)

for i, val in enumerate(s):
    if count[val] == 1:
        print(i)
        break