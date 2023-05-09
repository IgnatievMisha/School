class School:
    def __init__(self, name, students):
        self.name=name
        self.students=students #spisok
    def admit_students(self, student):
        self.students.append(student)
        print(f'{}') #dopisati

class Student:
