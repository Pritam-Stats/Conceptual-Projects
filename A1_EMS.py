# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tabulate",
# ]
# ///

## uv run A1_EMS.py or uv run --with tabulate A1_EMS.py

from tabulate import tabulate


# this will create each employee object instance
class Employee:
    def __init__(self, emp_id : int, name : str, age : int, dept : str, salary : float):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.dept = dept
        self.salary = salary

    def employee_info(self):
        print(f"ID : {self.emp_id}\t Name : {self.name}\t Age : {self.age}\t Department : {self.dept}\t Salary : {self.salary} ")


# treating this as an actual manager who will handle all the operations needed to manage the system
class EmployeeManager():
    def __init__(self):
        self.employees = {
            101 : Employee(101, "P1", 22, "Founder-CEO", 100000),
            102 : Employee(102, "P2", 22, "Co-Founder-CMO", 100000),
            103 : Employee(103, "P3", 23, "Creative-Head", 80000),
            201 : Employee(201, "John", 31, "Tech", 50000),
            207 : Employee(209, "Aalizeh", 27, "Creative", 50000),
            405 : Employee(405, "Anjali", 23, "HR", 60000)
        } #creates an dictionary to store data and added some pre added data as employees.
        # key is the employee id and value is the total employee object

    def add_employee(self, employee : Employee):
        
        self.employees[employee.emp_id] = employee
        

    def show_allemployees(self):
        if not self.employees:
            print("No Employees available.")
        else:
            print("All Employees :\n")
            table = [[emp.emp_id, emp.name, emp.age, emp.dept, emp.salary] for emp in self.employees.values()]  #value is the employee object
            print(tabulate(table, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="rounded_grid"))

    def add_employee_from_input(self):

        emp_id = int(input("Enter Employee ID: "))
        if emp_id in self.employees:
            print("❌ Employee ID already exists! Try again.")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

    # ✅ Create an Employee object
        employee = Employee(emp_id, name, age, dept, salary)

    # ✅ Add employee to dictionary
        self.add_employee(employee)

        print(f"✅ Employee {name} added successfully!")
    def search_employee(self):
        try:
            id = int(input("Enter the Employee id: "))

            if id in self.employees:
                print("\n####### Employee Found #######")
                self.employees[id].employee_info()
            else:
                print("Employee Not Found!!!!!!!!")

            
        except ValueError:
            print("❌ Invalid input!!!!!!!!!!!")


    def menu(self):
        while True:
            print("================== Welcome to the Employee Management System ==================\n 1️⃣. Add Employee \n 2️⃣. View all Employees \n 3️⃣. Search for Employee \n 4️⃣. Exit")

            choice = input("What you want to do (Type 1/2/3/4) : ").strip()

            if choice == "1":
                self.add_employee_from_input()
            elif choice == "2":
                self.show_allemployees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4" or choice == "Exit":
                print("Exiting the Program. Thank you for using the Program. 🙏🏽")
                break
            else:
                print("❌Invalid Choice!!!!!!")



# Create EmployeeManager
manager = EmployeeManager()
# Show all Employees
manager.menu()
