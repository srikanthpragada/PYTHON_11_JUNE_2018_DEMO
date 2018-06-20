def line(len=10, ch='-', space=False):
    endchar = ' ' if space else ''
    for i in range(0, len):
        print(ch, end=endchar)


line()
print()
line(space=True, len=20, ch='.')  # Keyword parameters
print()
line(5, '*', True)                # Positional
