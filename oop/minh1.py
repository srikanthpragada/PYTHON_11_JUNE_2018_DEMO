class A():
    def process(self):
        print("Process of A")


class B():
    def process(self):
        print("Process of B")


class C(A,B):
    def process1(self):
        print("Process of C")


obj = C()
print(C.__mro__)
