def normMarks(marks):
    if marks > 100:
        return 100
    if marks < 0:
        return 0
    return marks
def calcResult(marks):
    if marks >= 50:
        return "Pass"
    return "Fail"
def save_students(Students):
    with open("students.txt", "a") as file:
        for s in Students:
            file.write(f"{s['name']},{s['marks']},{s['result']}\n")
def process(Students,marks):
    for index,(student,mark) in enumerate(zip(Students,marks)):
        mark = normMarks(mark)
        result = calcResult(mark)
        Students[index] = {"name": student, "marks": mark, "result": result}
    save_students(Students)
def main():
    Students = list(map(str,input("Enter the students name: ").split()))
    marks = list(map(int,input("Enter the students marks: ").split()))
    process(Students,marks)
if __name__ == "__main__":
    main()