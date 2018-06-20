def iseven(n):
    return n % 2 == 0


nums = [10, 11, 15, 20]

evennums = filter(iseven, nums)
oddnums = filter(lambda n: n % 2 == 1, nums)

for n in evennums:
    print(n)

for n in oddnums:
    print(n)
