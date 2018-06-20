
directory = {}

while True:
    name = input("Enter name [end to stop]: ")
    if name == "end":
        break

    mobile = input("Enter mobile number :")
    if name in directory:
        directory[name].add(mobile)
    else:
        numbers = set()
        numbers.add(mobile)
        directory[name] = numbers  # add new entry

for  name,numbers in  sorted(directory.items()):
    print("{0:20s}".format(name),end= '')
    for n in numbers:
        print("{0:12s}".format(n), end = '')
    else:
        print()  # come to next line





