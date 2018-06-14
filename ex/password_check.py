import sys

pwd = input ('Enter password :')
if  len(pwd) < 6:
    print("Invalid password. Length must be >= 6")
    sys.exit()

upper = False
digit = False
special = False

for ch in pwd:
    if ch.isdigit():
        digit = True
    elif ch.isupper():
        upper = True
    elif not ch.islower():
        special = True

if upper and digit and special:
    print("Valid password!")
else:
    print("Invalid password")

# u = d = s = 1
# if u == 1 and d == 1 and s == 1:
#    print("Valid")


