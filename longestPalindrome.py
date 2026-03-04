from collections import Counter
s = "abccccdd"

count = Counter(s)
length = 0

for val in count.values():
    length += (val//2)*2

if length < len(s):
    length += 1


print(length)