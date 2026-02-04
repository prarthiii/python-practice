x = 4


# for i in range(x+1):
#     # res = 0
#     if i*i <= x:
#         res = i

# print(res)

# the above method is the brute force method and hence fails upon larger input, hence we use binary search so that time complexity decreases

left = 0
right = x
ans = 0

while left <= right:
    mid = (left+right)//2

    if mid * mid == x:
        print(mid)

    elif mid * mid < left:
        ans = mid
        left = mid + 1

    else:
        right = mid - 1

print(ans)