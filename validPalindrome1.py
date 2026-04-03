s = "aba"

l = 0
r = len(s) - 1

while l < r:
    if s[l] != s[r]:
        print(s[l+1 : r+1] == s[l+1 : r+1][::-1] or s[l:r] == s[l:r][::-1])

    l+=1
    r+=1