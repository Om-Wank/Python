# Create student class that takes name & marks of 3 subjects as arguments in constructor then create a methods to print the average

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def aver_marks(self):
       sum = 0

       for value  in self.marks:
        sum +=value

       print("hi",self.name,"your avg scor is:",sum/3)

s1 = Student("Om",[23,54,64])       
s1.aver_marks()