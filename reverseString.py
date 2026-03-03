s = ["h","e","l","l","o"]

right = len(s) - 1
left = 0

while left < right:
    s[left], s[right] = s[right], s[left]
    right -= 1
    left += 1
    
print(s)