
st = input("Enter a string :")
st =  ' ' + st

for idx in range(0, len(st)):
    if st[idx] == ' ':
        print(idx)

