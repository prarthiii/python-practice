ransomNote = "aa"
magazine = "ab"

magazine = list(magazine)

for i in ransomNote:
    if i in magazine:
        magazine.remove(i)
    else:
        print("false")
        break
else:
    print("true")