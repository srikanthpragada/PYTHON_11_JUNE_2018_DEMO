# Take numbers until 0 is given and display average

sum = 0
count = 0
while True:
    num = int(input("Enter a number [0 to stop] : "))
    if num == 0:
        break

    sum = sum + num
    count += 1

print("Average = ", sum // count)
