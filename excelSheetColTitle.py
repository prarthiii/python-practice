colNumber = 26

res = ""

while colNumber > 0:
    colNumber -= 1
    remainder = colNumber % 26
    res = chr(remainder + ord('A')) + res
    colNumber //= 26

print(res)