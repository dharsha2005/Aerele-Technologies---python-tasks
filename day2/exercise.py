# Day 2 Exercise
# Student Management #
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
    """Save the student result."""  #type hints
    with open("students.txt", "a") as file:
        file.write(f"{name} - {result}\n")

def process_student(name: str, marks: int) -> None:
    """Process student details."""  #type hints

    print("\nProcessing Student...")

    marks = normalize_marks(marks)
    result = calculate_result(marks)

    print("Name   :", name)
    print("Marks  :", marks)
    print("Result :", result)

    save_student(name, result)

    print("Student details saved.")

def main() -> None:     #type hints

    process_student("Dharshan", 85)
    process_student("Deepak", 40)
    process_student("Hari", 120)

if __name__ == "__main__":
    main()