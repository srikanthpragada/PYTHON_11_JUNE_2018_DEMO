# take names until end is entered
names = []

while True:
    name = input("Enter a name :")
    if name == "end":
        break
    names.append(name)

try:
    with open(r"e:\classroom\python\june11\names.txt", "wt") as f:
        for n in sorted(names):
            f.write(n + "\n")
except:
    print("Sorry! Could not write to file!")
