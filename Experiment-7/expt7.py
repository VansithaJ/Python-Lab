Aim:
To demonstrate Object-Oriented Programming concepts using Python classes and inheritance.

Algorithm:
Step1: Start
Step2: Create a class student to get student name and USN
Step3: Create a derived class marks to input marks
Step4: Calculate total marks
Step5: Display student details and total marks
Step6: End.

Source code:
class student:
    def get_student(self):
        self.student=input("enter student name:")
        self.usn=input("enter usn:")

class marks(student):
    def get_marks(self):
        self.marks1=int(input("enter marks of subject 1:"))
        self.marks2=int(input("enter marks of subject 2:"))
        self.marks3=int(input("enter marks of subject 3:"))
        self.marks4=int(input("enter marks of subject 4:"))
        self.marks5=int(input("enter marks of subject 5:"))

    def calculate(self):
        print("student:",self.student)
        print("total marks:",self.marks1+self.marks2+self.marks3+self.marks4+self.marks5)

obj=marks()
obj.get_student()
obj.get_marks()
obj.calculate()

Output:
enter student name:Bhavya
enter usn:24bcar0013
enter marks of subject 1:50
enter marks of subject 2:75
enter marks of subject 3:89
enter marks of subject 4:45
enter marks of subject 5:100
student: Bhavya
total marks: 359
