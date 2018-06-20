def length(n):
    return len(n)


names = ['Python', 'Ruby', 'TypeScript', 'c']

for n in sorted(names, key=str.lower):
    print(n)

for n in sorted(names, key=lambda n: len(n)):
    print(n)
