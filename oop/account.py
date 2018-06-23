class Account:

    def __init__(self, acno, ahname):
        self.__acno = acno
        self.__ahname = ahname
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return "%d %s %d" % (self.__acno, self.__ahname, self.__balance)

    def get_balance(self):
        return self.__balance

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.__acno == other.__acno
        else:
            return False


a1 = Account(1, "Abc")
a2 = Account(1, "Abc")
print(a1 == a2)
print(a1 == 1)
print(a1 != a2)
