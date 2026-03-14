from collections import Counter
n = 11

binary = bin(n)[2:]
count = Counter(binary)

for key, value in count.items():
    if key == '1':
        print(value)