def calculate(a, target): 

    n = len(a)

    for i in range(n):
        for j in range(i+1):
            if a[i] + a[j] == target:
                return [i, j]



