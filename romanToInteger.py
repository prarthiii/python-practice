s = input()

mapping = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
print(mapping.values())

total = 0
prev = 0

for ch in reversed(s):
    curr = mapping[ch]

    if curr < prev:
        total -= curr
    else:
        total += curr

    prev = curr

print(total)