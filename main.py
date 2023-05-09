class School:
    def __init__(self, name, students):
        self.name=name
        self.students=students #spisok
    def admit_students(self, student):
        self.students.append(student)
        print(f'{student.name} was admit to school {self.name}') #dopisati

class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    def promote(self):
        self.grade+=1
        print(f'{self.name} was promoted to {self.grade}')
    def demote(self):
        self.grade-=1
        print(f'{self.name} was demote to {self.grade}')