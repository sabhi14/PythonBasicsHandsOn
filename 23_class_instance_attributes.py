class Employee:
    count=0
    def __init__(self, name, salary):
        print("In constructor!!!")
        self.name=name
        self.salary=salary
        Employee.count+=1
    
    def getEmployeeDetails(self) :
        print("employee Details:")
        print("Name:-", self.name)
        print("Salary:- ",self.salary)


emp=Employee("Abhishek",50000)
emp.getEmployeeDetails()
emp2=Employee("Ahi",5000)
emp.getEmployeeDetails()
emp3=Employee("Abik",50100)
emp.getEmployeeDetails()
emp4=Employee("Abk",10000)
emp.getEmployeeDetails()
print("Count:- ",Employee.count)
print("Acess instance attributes directly!!!")
print("For Employee ",emp.name," ",str(emp.salary))