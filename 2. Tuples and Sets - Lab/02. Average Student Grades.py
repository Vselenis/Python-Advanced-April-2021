def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())
student_grades_line = input_to_list(n)

student_grades = {}

for line in student_grades_line:
    student, grade = line.split(" ")
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

def avg(values):
    return sum(values) / len(values)




for(student, grades) in student_grades.items():
    grades_str = " ".join(map(lambda grade: f"{grade:.2f}", grades))
    average_grade = avg(grades)
    print(f"{student} -> {grades_str} (avg: {average_grade:.2f})")