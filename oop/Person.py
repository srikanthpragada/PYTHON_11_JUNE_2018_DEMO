class Person:
    count = 0
    persons = []

    def __init__(self, name, mobile):
        Person.count += 1
        self.name = name
        self.mobile = mobile
       # Person.persons.append(self)

    def __del__(self):
        Person.count -= 1
        print("Deleting ", self)
        #Person.persons.remove(self)


    def __str__(self):
        return  self.name + "," + self.mobile


p1 = Person("Abc", "3943434")
print(Person.count)
p2 = Person("Pqr", "38383333")
print(Person.count)
# for p in Person.persons:
#     print(p)
del p1
print(Person.count)


