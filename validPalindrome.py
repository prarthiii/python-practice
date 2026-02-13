s = "A man, a plan, a canal: Panama"

s = s.lower()

newlist = ""

for ss in s:
    if ss.isalnum():
        newlist += ss


if newlist == newlist[::-1]:
    print("yes")


