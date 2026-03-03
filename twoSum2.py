numbers = [2,7,11,15]
target = 9

left = 0
right = len(numbers)-1

while left < right:
    current_target = numbers[left] + numbers[right]

    if current_target == target:
        print([left + 1, right + 1])
        break

    elif current_target < target:
        left += 1

    else:
        right -= 1

print(numbers)