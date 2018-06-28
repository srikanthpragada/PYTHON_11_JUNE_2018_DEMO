# Print lines from file

try:
    with open(r"e:\classroom\python\june11\names.txt", "rt") as f:
        print(type(f))
        for n in f.readlines():
            print(n, len(n))
except:
    print("Sorry! Could not read file!")
