class Employee:

    def __init__(self,fname,lname):
        print("In Employee Cons.")
        self.fname=fname
        self.lname=lname

    def getFname(self):
        return self.fname

    
    def getlname(self):
        return self.lname

    def getEmployeeDetails(self):
        print("In Employee Class methods")

class fullStackDeveloper( Employee):

    def __init__(self,fname,lname,tech):
        super().__init__(fname,lname)
        self.tech=tech

    def getEmployeeDetails(self):
        return "Name " +self.fname+" "+self.lname+" "+self.tech

fsd1= fullStackDeveloper("abhi","sawant","JavaFSD")
print(fsd1.getEmployeeDetails())
print(fsd1.getFname())

emp1=Employee("Abhishek","Sawant")
emp1.getEmployeeDetails()