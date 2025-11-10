
# in python function and variable of a Object is called Attributes

class Employee:
    def __init__(self,empid=None,name=None,salary =None):
           self.empid = empid
           self.name = name
           self.salary = salary
    def setEmpid(self,empid):
          self.empid = empid
    
    def setEname(self,name):
          self.name = name

    def setSalary(self,salary):
          self.salary = salary 

    def getEmpid(self):
          return self.empid              
    
    def getEname(self):
          return self.name              
    
    def getEsalary(self):
          return self.salary  

e1 = Employee()
e2 = Employee(1,"Rahul",40000)  
e1.setEmpid(2)
e1.setEname("Ramesh")
e1.setSalary(50000)  

print(e1.getEmpid(),e1.getEname(),e1.getEsalary())
print(e2.getEmpid(),e2.getEname(),e2.getEsalary())
