'''

1. class keyword
2. instance attributes
3. class attributes
4. __init__ method --> constructor
5. self
'''
class Employee :
    count=0
    salary = 0
    def __init__(self):
        print("In constructor!!!")
        Employee.count+=1

    def getCount(self):
        print("Punching Attendance!!!")
        print(self.count)

emp = Employee()
emp2 = Employee()
emp3= Employee()
emp.getCount()
