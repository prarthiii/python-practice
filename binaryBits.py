n = 5

binary  = list(bin(n))[2:]

# print(binary)

left = 0
right = left + 1

while right < len(binary):
    if binary[left] == binary[right]:
        print("invalid")
        break
    left +=1
    right +=1

print("valid")