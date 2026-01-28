# count digits 

def count_digits(s):
    count = 0
    for d in s:
        if d.isdigit():
            count += 1

    return count
if __name__ == '__main__':
    s = input()
    res = count_digits(s)
    print(res)