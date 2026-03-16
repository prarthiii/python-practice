pattern = "aba"
s = "cat cat cat dog"

s = s.split(' ')

if len(pattern) != len(s):
    print(False)

print(len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)))