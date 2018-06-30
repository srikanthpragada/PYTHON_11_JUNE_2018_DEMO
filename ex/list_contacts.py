import re


def get_details(line):
    # look for name
    match = re.search("[a-zA-Z]+", line)
    if not match:
        return None
    else:
        name = match.group()

    match = re.search("\d{10}", line)
    if not match:
        return None
    else:
        mobile = match.group()

    return (name, mobile)  #return tuple


f = open("contacts.txt", "rt")

teldir = dict()
for line in f:
    details = get_details(line)
    if details:
        teldir[details[0]] = details[1]

for (name, mobile) in sorted(teldir.items()):
    print("%-20s %10s" % (name, mobile))
