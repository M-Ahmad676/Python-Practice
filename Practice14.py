class Student:
    def __init__(self,name,marks,no_of_subjects):
        self.name = name
        self.marks = marks
        self.no_of_subjects = no_of_subjects

    def average_marks(self):
        ave = self.marks/self.no_of_subjects
        return ave

name = input("Enter Your Name: ")
no_of_subjects = int(input("Enter Number of Subjects: "))
marks = int(input("Enter marks: "))

student1 = Student(name,marks,no_of_subjects)

print(student1.average_marks())

