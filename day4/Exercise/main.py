from services.student_service import add_student
from database.storage import show_students
def main():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    add_student(name, age)
    print("Student added successfully!")
    print("List of students:")
    show_students()
if __name__ == "__main__":
    main()
    