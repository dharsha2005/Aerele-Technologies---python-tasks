from models.student import Student
from database.storage import save_student

def add_student(name: str, age: int) -> None:
    student = Student(name, age)
    save_student(student)