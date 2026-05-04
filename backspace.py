def f(s):
    res = []

    for c in s:
        if c == '#':
            res and res.pop()
        else:
            res.append(c)
    return res

def logic(s, t):
    return f(s) == f(t)
