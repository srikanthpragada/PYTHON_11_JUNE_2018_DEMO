class Common:
    def process(self):
        print("Process of Common")


class A(Common):
    def process(self):
        print("Process of A")


class B(Common):
    def process(self):
        print("Process of B")


class C(A, B):
    def process1(self):
        print("Process of C")


obj = C()
print( C.__mro__)
