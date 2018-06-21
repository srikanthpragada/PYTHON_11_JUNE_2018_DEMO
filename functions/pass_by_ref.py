def add_item(items, item):
    items.append(item)


def clear_items(items):
    items.clear()


names = ['Python', 'Java']
add_item(names, 'Typescript')

for n in names:
    print(n)

clear_items(names)

print(len(names))
