def fun1():
    print("In fun1()")

def fun2(p1):
    print("In fun2() ", p1)

def fun2(p2):
    print("In second fun2() ", p2)


fun1()
fun2(100)
fun2("Abc")

fun3 = fun2
fun3(100)


def fun2():
    print("in new fun2()")

fun2()
fun3(100)

