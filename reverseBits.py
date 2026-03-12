n = 43261596

binary = bin(n)[2:].zfill(32)

print(f"binary is: {binary}")

res = binary[::-1]
print(int(res, 2))