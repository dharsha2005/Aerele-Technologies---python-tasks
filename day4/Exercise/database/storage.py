student = []
def save_student(std):
    student.append(std)
def show_students():
    for s in student:
        print(f"Name: {s.name}, Age: {s.age}")