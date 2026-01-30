def valid(s):
    mapping = { '}' : '{', ')' : '(', ']' : '['}
    stack = []

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack
            
                

s = input()
res = valid(s)
print(res)