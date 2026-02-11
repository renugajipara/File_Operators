class Employee:

    def setdata(self):
        self.em_id = em_id
        self.name = name
        self.age = age
        self.salary = salary
    
    def __init__(self, em_id, name, age, salary):
        self.em_id = em_id
        self.name = name
        self.age = age
        self.salary = salary
        
    def getdata(self):
        print(f"Employee_Id : {self.em_id}    |    Salary : {self.salary}")

    def __del__(self):
        print("Thank you for information...")

class Manager(Employee):
    pass

class Developer(Employee):
    pass

em_id = int(input("Enter the employee Id: "))
name = input("Enter the employee name: ")
age = int(input("Enter the employee age: "))
salary = int(input("Enter the employee salary: "))

obj = Employee(em_id, name, age, salary)
obj.setdata()
obj.getdata()
