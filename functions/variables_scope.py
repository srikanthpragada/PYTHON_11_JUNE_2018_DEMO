g = 10


def f():
    e = 20
    g = 100

    def f2():
        global g
        nonlocal e
        g = 20
        e = e + 10
        print(e, g)

    f2()
    print(e)
    print(g)


f()
print(g)
