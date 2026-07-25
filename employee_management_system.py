"""
Employee Management System (Core Python)
-----------------------------------------
A console-based application to manage employee records, attendance,
and salary details. Built using OOP concepts, functions, file handling
for persistent storage, and exception handling for input validation.

Author: Reddi Kishor
"""

import os
import json

DATA_FILE = "employees.json"


# ---------------------------------------------------------------------
# Employee Class (OOP)
# ---------------------------------------------------------------------
class Employee:
    def __init__(self, emp_id, name, department, salary, attendance=0):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.attendance = attendance  # number of days present

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "attendance": self.attendance,
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            data["emp_id"],
            data["name"],
            data["department"],
            data["salary"],
            data.get("attendance", 0),
        )

    def __str__(self):
        return (
            f"ID: {self.emp_id} | Name: {self.name} | "
            f"Department: {self.department} | Salary: {self.salary} | "
            f"Attendance: {self.attendance} days"
        )


# ---------------------------------------------------------------------
# Employee Manager Class (handles all operations + file persistence)
# ---------------------------------------------------------------------
class EmployeeManager:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.employees = {}
        self.load_data()

    # ---------------- File Handling ----------------
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    raw_data = json.load(f)
                    for emp_id, emp_data in raw_data.items():
                        self.employees[emp_id] = Employee.from_dict(emp_data)
            except (json.JSONDecodeError, IOError) as e:
                print(f"[Warning] Could not load existing data: {e}")
        else:
            self.employees = {}

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(
                    {eid: emp.to_dict() for eid, emp in self.employees.items()},
                    f,
                    indent=4,
                )
        except IOError as e:
            print(f"[Error] Could not save data: {e}")

    # ---------------- Core Operations ----------------
    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ").strip()
            if emp_id in self.employees:
                print("Employee ID already exists!")
                return

            name = input("Enter Name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            department = input("Enter Department: ").strip()

            salary = float(input("Enter Salary: ").strip())
            if salary < 0:
                raise ValueError("Salary cannot be negative.")

            employee = Employee(emp_id, name, department, salary)
            self.employees[emp_id] = employee
            self.save_data()
            print(f"Employee '{name}' added successfully.")

        except ValueError as e:
            print(f"[Input Error] {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")

    def view_employees(self):
        if not self.employees:
            print("No employee records found.")
            return
        print("\n----- Employee Records -----")
        for emp in self.employees.values():
            print(emp)
        print("-----------------------------\n")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ").strip()
        emp = self.employees.get(emp_id)
        if emp:
            print(emp)
        else:
            print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee not found.")
            return

        try:
            print("Leave a field blank to keep the current value.")
            name = input(f"Name [{emp.name}]: ").strip()
            department = input(f"Department [{emp.department}]: ").strip()
            salary_input = input(f"Salary [{emp.salary}]: ").strip()

            if name:
                emp.name = name
            if department:
                emp.department = department
            if salary_input:
                new_salary = float(salary_input)
                if new_salary < 0:
                    raise ValueError("Salary cannot be negative.")
                emp.salary = new_salary

            self.save_data()
            print("Employee record updated successfully.")

        except ValueError as e:
            print(f"[Input Error] {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ").strip()
        if emp_id in self.employees:
            confirm = input(f"Are you sure you want to delete '{emp_id}'? (y/n): ")
            if confirm.lower() == "y":
                del self.employees[emp_id]
                self.save_data()
                print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    def mark_attendance(self):
        emp_id = input("Enter Employee ID to mark attendance: ").strip()
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee not found.")
            return
        emp.attendance += 1
        self.save_data()
        print(f"Attendance marked for '{emp.name}'. Total days present: {emp.attendance}")

    def calculate_salary(self):
        emp_id = input("Enter Employee ID for salary calculation: ").strip()
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee not found.")
            return
        try:
            per_day_rate = emp.salary / 30
            payable_salary = per_day_rate * emp.attendance
            print(
                f"\n{emp.name} — Attendance: {emp.attendance} days | "
                f"Monthly Salary: {emp.salary} | Payable Salary: {payable_salary:.2f}\n"
            )
        except ZeroDivisionError:
            print("[Error] Invalid salary base for calculation.")


# ---------------------------------------------------------------------
# Menu / Main Program
# ---------------------------------------------------------------------
def print_menu():
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. Calculate Payable Salary")
    print("8. Exit")
    print("=======================================")


def main():
    manager = EmployeeManager()

    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice (1-8): ").strip())
        except ValueError:
            print("[Input Error] Please enter a valid number.")
            continue

        if choice == 1:
            manager.add_employee()
        elif choice == 2:
            manager.view_employees()
        elif choice == 3:
            manager.search_employee()
        elif choice == 4:
            manager.update_employee()
        elif choice == 5:
            manager.delete_employee()
        elif choice == 6:
            manager.mark_attendance()
        elif choice == 7:
            manager.calculate_salary()
        elif choice == 8:
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 8.")


if __name__ == "__main__":
    main()
