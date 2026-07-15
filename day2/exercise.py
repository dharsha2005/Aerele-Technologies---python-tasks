# Day 2 Exercise
# Student Management and Salary Management
# Author: Dharshan B

# ---------------- Student Management ---------------- #

def normalize_marks(marks: int) -> int:
    """Ensure marks are between 0 and 100."""  #type hints
    if marks < 0:
        return 0
    if marks > 100:
        return 100
    return marks

def calculate_result(marks: int) -> str:
    """Return student's result."""  #type hints     
    if marks >= 50:
        return "Pass"
    return "Fail"


def save_student(name: str, result: str) -> None:
    """Save the student result."""  
    with open("students.txt", "a") as file:
        file.write(f"{name} - {result}\n")


def process_student(name: str, marks: int) -> None:
    """Process student details."""

    print("\nProcessing Student...")

    marks = normalize_marks(marks)
    result = calculate_result(marks)

    print("Name   :", name)
    print("Marks  :", marks)
    print("Result :", result)

    save_student(name, result)

    print("Student details saved.")


# ---------------- Salary Management ---------------- #

def validate_salary(salary: float) -> float:
    """Return valid salary."""
    if salary < 0:
        return 0
    return salary


def calculate_tax(salary: float) -> float:
    """Calculate 10% tax."""
    return salary * 0.10


def calculate_net_salary(salary: float) -> float:
    """Return salary after tax."""
    tax = calculate_tax(salary)
    return salary - tax


def save_salary(name: str, net_salary: float) -> None:
    """Save salary details."""
    with open("salary.txt", "a") as file:
        file.write(f"{name} - {net_salary}\n")


def process_salary(name: str, salary: float) -> None:
    """Process salary details."""

    print("\nProcessing Salary...")

    salary = validate_salary(salary)
    tax = calculate_tax(salary)
    net_salary = calculate_net_salary(salary)

    print("Employee   :", name)
    print("Salary     :", salary)
    print("Tax        :", tax)
    print("Net Salary :", net_salary)

    save_salary(name, net_salary)

    print("Salary details saved.")


# ---------------- Main Program ---------------- #

def main() -> None:     #type hints

    process_student("Dharshan", 85)
    process_student("Deepak", 40)
    process_student("Hari", 120)

    process_salary("Dharshan", 50000)
    process_salary("Deepak", 35000)
    process_salary("Hari", -2000)


if __name__ == "__main__":
    main()