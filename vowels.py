# count the number of vowels in a given string using a function

def count_vowels(s):
    count = 0
    for vow in s:
        if vow == 'a' or vow == 'e' or vow == 'i' or vow == 'o' or vow == 'u':
            count += 1

    return count

if __name__ == '__main__':
    s = input()
    res = count_vowels(s)
    print(res)