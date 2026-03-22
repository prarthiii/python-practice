num = 100
res = ''

is_negative = num<0
num = abs(num)

while num > 0:
    rem = num % 7
    quo = num // 7

    res += str(rem)

    num = quo
res = res[::-1]

if is_negative:
    res = '-' + res
print(res)