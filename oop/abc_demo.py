from abc import ABC, abstractmethod


class Student(ABC):
    @abstractmethod
    def getsubject(self):
        pass


class PythonStudent(Student):
    def getsubject(self):
        return "Python"


s = PythonStudent()
