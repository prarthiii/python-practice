# all the numbers which are powers of two, will only have a single set bit (1) in their binary representation
# for example: 4 : 100
# for example: 8 : 1000 and so on


def power(n):
    return n > 0 and (n & (n-1) == 0)

print(power(5))

# with n & (n-1)  we check that the current number(n) and the previous number(n-1) perform the bitwise AND operation
# eg: n = 8
# 1000 & (0111) perform the AND opertion and give the op 0, in easy words, we just invert the bits and check whether the op 0
# the '&' automatically converts the numbers to binary their binary form