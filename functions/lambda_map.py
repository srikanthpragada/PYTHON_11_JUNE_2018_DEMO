def concat(f, l):
    return f.upper() + " " + l.upper()


fn = ['Bill', 'Steve', 'Micheal','Mark']
ln = ['Gates', 'Jobs', 'Dell']

for n in map(lambda f, l: f + ' ' + l, fn, ln):
    print(n)

for n in map(concat, fn, ln):
    print(n)
