'''
Write a Small Script Using List Comprehension and Context Manager
'''
students = ["Alice", "Bob", "Charlie", "David", "Emma"]
marks = [95, 78, 88, 67, 91]
passed_students = [
    name for name, mark in zip(students, marks) if mark >= 80
]
with open("numbers.txt", "w") as file:
    file.write("Passed Students\n")
    file.write("-----------------\n")
    for student in passed_students:
        file.write(student + "\n")
print("Result file created successfully.")

'''
Java-style code
'''
students = ["Alice", "Bob", "Charlie"]
marks = [95, 78, 88]

for i in range(len(students)):
    print(students[i] + " scored " + str(marks[i]))

'''
Rewrite It the Pythonic Way
'''
students = ["Alice", "Bob", "Charlie"]
marks = [95, 78, 88]

for index, (student, mark) in enumerate(zip(students, marks), start=1):
    print(f"{index}. {student} scored {mark}")