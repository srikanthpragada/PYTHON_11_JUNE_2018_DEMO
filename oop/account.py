class Account:
    # Static variables / Class variables
    minbal = 5000
    intrate = 3.5
    nextacno = 1

    @staticmethod
    def details():
        print(Account.minbal)
        print(Account.intrate)

    @classmethod
    def create(cls, name):
        obj = cls(Account.nextacno, name)
        Account.nextacno += 1
        return obj

    def __init__(self, acno, ahname):
        self.__acno = acno
        self.__ahname = ahname
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    @property
    def customer(self):
        return self.__ahname

    @customer.setter
    def customer(self, value):
        self.__ahname = value

    def __str__(self):
        return "%d %s %d" % (self.__acno, self.__ahname, self.__balance)

    def get_balance(self):
        return self.__balance

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.__acno == other.__acno
        else:
            return False


obj1 = Account.create("Andy")
obj2 = Account.create("Scott")

print(obj1)
print(obj2)


print(Account.minbal)

a1 = Account(1, "Abc")
a1.customer = "Xyz"
# print(type(a1._Account__ahname))
print(a1.customer)

# a2 = Account(1, "Abc")
# print(a1 == a2)
# print(a1 == 1)
# print(a1 != a2)
