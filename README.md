# Employee Management System

A console-based Employee Management System built in **Core Python**. It manages employee records, attendance, and salary details using Object-Oriented Programming, file handling for persistent storage, and exception handling for input validation.

## Features

- **Add Employee** — create a new employee record with ID, name, department, and salary
- **View All Employees** — display all stored employee records
- **Search Employee** — look up an employee by ID
- **Update Employee** — edit name, department, or salary for an existing employee
- **Delete Employee** — remove an employee record (with confirmation)
- **Mark Attendance** — increment an employee's attendance count
- **Calculate Payable Salary** — compute salary owed based on monthly salary and days attended

## Tech / Concepts Used

- Core Python
- Object-Oriented Programming (classes, methods, static methods)
- Functions
- File Handling (JSON-based persistent storage)
- Exception Handling (input validation, safe file I/O)

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python's built-in `os` and `json` modules)

## How to Run

1. Make sure Python is installed:
   ```bash
   python --version
   ```
2. Run the script:
   ```bash
   python employee_management_system.py
   ```
3. Use the on-screen menu (options 1–8) to manage employee records.

## Data Storage

All employee records are saved automatically to a file named `employees.json` in the same directory as the script. This file is created on first run and updated after every add, update, or delete operation, so your data persists between sessions.

Example `employees.json` structure:
```json
{
    "E001": {
        "emp_id": "E001",
        "name": "John Doe",
        "department": "IT",
        "salary": 30000.0,
        "attendance": 5
    }
}
```

## Project Structure

```
employee_management_system.py   # Main application file
employees.json                  # Auto-generated data file (created on first run)
README.md                       # Project documentation
```

## Possible Future Enhancements

- Replace JSON storage with a SQL Server / SQLite database
- Add password-protected admin login
- Export employee reports to CSV or PDF
- Add a graphical user interface (Tkinter or web-based)

## Author

**Reddi Kishor**
📧 kishorreddi1310@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/kishor-reddi-182a2427a) · [GitHub](https://github.com/Kisho-re)
