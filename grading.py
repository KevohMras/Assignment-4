def calculate_grade(score, grading_scale):
    for grade, min_score in grading_scale.items():
        if score >= min_score:
            return grade
            # Default to "F" if the score is below the minimum value in the grading scale.

def main():
    grading_scale = {
        "A": 90,
        "B": 80,
        "C": 70,
        "D": 60,
    }

    num_students = int(input("Enter the number of students: "))
    student_data = {}

    for i in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {i}: ")
        student_mark = float(input(f"Enter the mark for {student_name}: "))
        student_data[student_name] = student_mark

    print("\nGrades:")
    for student, mark in student_data.items():
        grade = calculate_grade(mark, grading_scale)
        print(f"{student}: {mark} - {grade}")

if __name__ == "__main__":
    main()
