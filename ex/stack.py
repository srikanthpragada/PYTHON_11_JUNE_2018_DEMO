# stack

nums = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    nums.append(num)

# Use it a stack
while len(nums) > 0:
    print(nums.pop())

# Use it as queue
# while len(nums) > 0:
#     print(nums[0])
#     del nums[0]
