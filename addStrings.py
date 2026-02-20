num1 = "11"
num2 = "123"

res = ""
i = len(num1) - 1
j = len(num2) - 1
carry = 0

while i >= 0 or j >= 0 or carry:
    n1 = int(num1[i]) if i >= 0 else 0
    n2 = int(num2[j]) if j >= 0 else 0

    total = n1+n2+carry
    carry = total // 10
    digit = total % 10

    res += str(digit)

    i -=1
    j -= 1


print(res[::-1])