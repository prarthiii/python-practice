a = '11' 
b = '1'

a = int(a, 2)
b = int(b, 2)

print(f"a is {a} b is {b}")

res = a+b
res = bin(res)
res = str(res)
res = res[2:]
print(res)

