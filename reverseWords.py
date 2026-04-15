s = "Let's take LeetCode contest"

s = s.split()
answer = ''

for word in s:
    ans = word[::-1]
    answer += ans + ' '

print(answer.strip())