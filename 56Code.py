class Employee:
    company = "Accenture"

    def __init__(self,name):
        self.name = name

emp1 = Employee("Om")
emp2 = Employee("Amit")

print(emp1.name)
print(emp1.company)
print(emp2.name)
print(emp2.company)
