num = 5
res = ''
binaryNumber = bin(num)[2:]
print(binaryNumber)
for i in binaryNumber:
    if i == '1':
        res += '0'
    else:
        res += '1'
print(res)
print(int(res, 2))

