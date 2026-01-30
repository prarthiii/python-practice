# str1 = input()

# str2 = str(str1)
# print(f"str2 is : {str2}")

# res = list(str2)

# print(res[::-1])


# solution using loops:

def palindrome(str1):

    str1 = str(str1)

    left = 0
    right = len(str1) - 1

    while left <  right:
        if str1[left] != str1[right]:
            print("not palindrome")
        else:
            print("yes palindrome")
        left +=1
        right -=1

print(palindrome(121))