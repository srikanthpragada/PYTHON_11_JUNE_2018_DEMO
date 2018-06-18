names = []

while True:
    print("Menu")
    print("1. Add Name")
    print("2. Remove Name")
    print("3. List")
    print("4. Exit")

    opt = input("Choice : ")
    if  opt == '1':  # Add
        name = input("Enter name : ")
        names.append(name)
    elif opt == '2':  # Remove
        name = input("Enter name : ")
        if name in names:
            names.remove(name)
        else:
            print("Name not found!")
    elif opt =='3':  # List
        print("Names")
        for n in names:
            print(n)
    else:  # Exit
        break
