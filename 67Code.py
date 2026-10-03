class Student:
    school = "ABC School"

    def __init__(self,name):
        self.name = name

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school

s1 = Student("Om")
s2 = Student("Rahul") 

print(s1.school)
print(s2.school)

Student.change_school("XYZ School")

print(s1.school)
print(s2.school)