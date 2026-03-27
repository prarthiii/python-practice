from collections import Counter
s1 = "ab"
s2 = "eidbaooo"

k = len(s1)

s1_count = Counter(s1)
window = Counter(s2[:k])

if window == s1_count:
    print(True)


for i in range(k, len(s2)):
    window[s2[i]]+=1
    window[s2[i-k]]-=1

    if window[s2[i-k]] == 0:
        del window[s2[i-k]]

    if window == s1_count:
        print(True)