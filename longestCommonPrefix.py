strs = ["flower","flow","flight"]

if not strs:
    print("")

# prefix = strs[0]

# for i in range(len(prefix)):
#     char = prefix[i]

#     for s in strs[1:]:
#         if i >= len(s) or s[i] != char:
#             prefix[:i]

#             print(prefix)

# the above method can be used in interviews, we also have another logic to solve this using the zip() method, following is the code:

prefix = ""

for chars in zip(*strs):
    if len(set(chars) == 1):
        prefix += chars[0]
    else:
        break

print(prefix)