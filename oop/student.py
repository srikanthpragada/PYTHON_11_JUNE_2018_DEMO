class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + "," + self.email


class PythonStudent(Student):
    def __init__(self, name, email, marks):
        super().__init__(name, email)
        self.marks = marks

    # Overriding
    def __str__(self):
        return super().__str__() + "," + str(self.marks)


class OracleStudent(Student):
    def __init__(self, name, email, marks):
        super().__init__(name, email)
        self.marks = marks

    # Overriding
    def __str__(self):
        return super().__str__() + "," + str(self.marks)

s = Student("Scott", "scott@gmail.com")
print(s)
p = PythonStudent("Bill", "bill@gmail.com", 65)
print(p)

os = OracleStudent("Larry", "larry@gmail.com", 90)
print(os)
