def add(*nums, display = False ):
    sum = 0
    for n in nums:
        if display:
            print(n)
        sum += n

    return sum


print(add(10, 20, 1, 2, 3, display=True))
print(add(10, 20, 1, 2, 3))
