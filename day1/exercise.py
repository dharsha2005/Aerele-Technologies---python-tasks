students = list(map(str,input("Enter the students name: ").split()))
marks = list(map(int,input("Enter the students marks: ").split()))
for index,(student,marks) in enumerate(zip(students,marks)):
    print(f"{index+1}. {student} - {marks}")