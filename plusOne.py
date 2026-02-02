digits = [9]

num = int("".join(map(str, digits)))
num += 1
print(list(map(int, str(num))))