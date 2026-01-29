import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4*size - 3

    # Top half
    for i in range(size-1, -1, -1):
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = left + right
        print("-".join(row).center(width, "-"))

    # Bottom half
    for i in range(1, size):
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = left + right
        print("-".join(row).center(width, "-"))

        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)