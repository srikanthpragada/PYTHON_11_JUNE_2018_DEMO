import sys
import os


def string_exists(filename, searchstring):
    try:
        f = open(filename, "rt")
        for line in f:
            if line.find(searchstring) >= 0:
                return True
        else:
            return False
    except:
        return False

    
# take values from command line arguments
if len(sys.argv) < 3:
    print("Usage : python searchstring startdir  searchstring")
    sys.exit(1)

startdir = sys.argv[1]  # r"e:\classroom\python\june11"
searchstring = sys.argv[2]  # input

for (dn, dl, fl) in os.walk(startdir):
    for f in fl:
        if f.endswith('.py'):
            if string_exists(dn + "\\" + f, searchstring):
                print(dn + "\\" + f)
