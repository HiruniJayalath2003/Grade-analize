def calculate_grade(average):
    if average >= 75:
        return "A", "Pass"
    elif average >= 60:
        return "B", "Pass"
    elif average >= 50:
        return "C", "Fail"
    elif average >= 30:
        return "D", "Fail"
    else:
        return "F", "Fail"


def get_valid_mark(subject):
    while True:
        try:
            mark = int(input(f"{subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    name = input("\nEnter Student Name: ")

    print("\nEnter Marks:")
    science = get_valid_mark("Science")
    maths = get_valid_mark("Maths")
    english = get_valid_mark("English")

    average = (science + maths + english) / 3
    grade, status = calculate_grade(average)

    student = {
        "name": name,
        "science": science,
        "maths": maths,
        "english": english,
        "average": average,
        "grade": grade,
        "status": status
    }

    return student


def display_student(student):
    print("\n----- STUDENT REPORT CARD -----")
    print(f"Name     : {student['name']}")
    print(f"Science  : {student['science']}")
    print(f"Maths    : {student['maths']}")
    print(f"English  : {student['english']}")
    print(f"Average  : {student['average']:.2f}")
    print(f"Grade    : {student['grade']}")
    print(f"Status   : {student['status']}")
    print("-"*35)


def main():
    students = []

    while True:
        print("\n====== STUDENT MANAGER  ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student = add_student()
            students.append(student)
            print("Student added successfully!")

        elif choice == "2":
            if not students:
                print("No students available.")
            else:
                for s in students:
                    display_student(s)

        elif choice == "3":
            print("Stay motivated...!!")
            break

        else:
            print(" Invalid choice. Try again.")

main()