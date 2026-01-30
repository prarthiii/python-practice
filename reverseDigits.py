

def reversedigits():

    x = 1534236469

    start = "-"
    x = str(x)

    res = x[::-1]

    if res[-1] == '-':
        res = res.replace("-", "")
        res = start+res
        # print(int(res))

    else:
        res = x[::-1]
        # print(int(res))

    res = int(res)

    if res < -2**31 or res > 2**31 - 1:
        return 0

    return res

reversedigits()