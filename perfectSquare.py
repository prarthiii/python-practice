num = 256

# for n in range(num+1):
#     if n * n == num:
#         print(n)

# the above solution is correct, but not memory efficient, for larger number this fails

if num < 2:
    print(True)

left = 1
right = 1
num // 2

while left <= right:
    mid = (left + right)//2
    square = mid * mid

    if square == num:
        print(f"square root exists and the num is: {num}")
    elif square < num:
        left = mid + 1
    elif square > num:
        right = mid - 1
