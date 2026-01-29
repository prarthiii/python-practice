s = input()

def capitals(s):
        words = s.split(" ")
        result = []

        for w in words:
            result.append(w.capitalize())

        return " ".join(result)
    
print(capitals(s))