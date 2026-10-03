class Student:
    def __init__(self,subject):
        self.subject = subject

    def __getitem__(self,index):
        return self.subject[index]

student = Student(["Python","SQL","Java","AI"])

print(student[0])
print(student[2])
    
        