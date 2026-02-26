from collections import Counter
s = "abcd"
t = "abcde"

s = list(s)
t = list(t)

for letter in s:
    t.remove(letter)
print(t)