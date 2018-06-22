import sys

if len(sys.argv) == 1:
    print("Usage : python commonfactors  number  ...")
    sys.exit(0)  # Exit program

nums = set()
for i in range(1, len(sys.argv)):
    num = int(sys.argv[i])
    nums.add(num)


smallest = min(nums)
for i in range(2, smallest // 2 + 1):
    for n in nums:
        if n % i != 0:
            break
    else:
        print(i)
