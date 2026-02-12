class Employee:

    def __init__(self, em_id = None, name = None, age = None, salary = None):
        self.__em_id = em_id
        self.name = name
        self.age = age
        self.__salary = salary

    def id_setdata(self,em_id):
        self.__em_id = em_id

    def id_getdata(self):
        return self.__em_id

    def salary_setdata(self,salary):
        self.__salary = salary

    def salary_getdata(self):
        return self.__salary

    def display(self):
        print("Employee Details:")
        print(f"ID: {self.__em_id}\nName: {self.name}\nAge: {self.age}\nSalary: {self.__salary}")
    
    def __del__(self):
        print("Del Employee object deleted. \nThank you for information...")

class Manager(Employee):

    def __init__(self, em_id, name, age, salary, department):
        super().__init__(em_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):

    def __init__(self, em_id, name, age, salary, prog_lang):
        super().__init__(em_id, name, age, salary)
        self.prog_lang = prog_lang

    def display(self):
        super().display()
        print(f"Programming Language: {self.prog_lang}")

print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))

emp = None
manager = None
dev = None

while True:
    print("\n1. Create a Person\n 2. Create an Employee\n 3. Create a Manager\n 4. Create a Delveloper\n 5. Show Details\n 6. Exit")

    choice = int(input("Enter what you want to perform: "))

    match choice:
        case 1:
            name = input("Enter the person's name: ")
            age = int(input("Enter the person's age: "))

            print(f"Person created with name : {name} and age : {age}")

        case 2:
            em_id = int(input("Enter the employee Id: "))
            name = input("Enter the employee name: ")
            age = int(input("Enter the employee age: "))
            salary = int(input("Enter the employee salary: "))

            emp = Employee(em_id, name, age, salary)

            print("Employee is created...")
        
        case 3:
            man_id = int(input("Enter the Manager Id: "))
            name = input("Enter the Manager name: ")
            age = int(input("Enter the Manager age: "))
            salary = int(input("Enter the Manager salary: "))
            department = input("Enter the Manager department: ")

            manager = Manager(man_id, name, age, salary, department)

            print("Manager is created...")

        case 4:
            dev_id = int(input("Enter the developer ID: "))
            name = input("Enter the developer name: ")
            age = int(input("Enter the manager age: "))
            salary = int(input("Enter the developer salary: "))
            lang = input("Enter developer Programming Language: ")

            dev = Developer(dev_id, name, age, salary, lang)

            print("Developer is created...")

        case 5:
            print("Choose a detail to show:\n 1.Employee\n 2.Manager\n 3.Developer")

            choice = int(input("Enter what you want to perform: "))

            match choice:

                case 1:
                    emp.display()

                case 2:
                    manager.display()

                case 3:
                    dev.display()

                case _:
                    print("Invalid input...")

        case 6:
            print("Existing the system. All resources have been freed.\n")
            print("Good Bye!!")
            break

        case _:
            print("Invalid input...")