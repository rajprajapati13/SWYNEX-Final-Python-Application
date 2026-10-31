
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        print("Error: Invalid student data format.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Error: Could not read student records.")
        return []


def save_students(students):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save student records.")
        return False


def add_student(students):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    roll = input("Enter roll number: ").strip()
    if not roll:
        print("Roll number cannot be empty.")
        return

    if any(str(s.get("roll")) == roll for s in students):
        print("This roll number already exists.")
        return

    course = input("Enter course: ").strip()
    if not course:
        print("Course cannot be empty.")
        return

    students.append({"roll": roll, "name": name, "course": course})

    if save_students(students):
        print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"Roll: {student['roll']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']}"
        )


def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if str(student.get("roll")) == roll:
            print("Student found:", student)
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()

    for student in students:
        if str(student.get("roll")) == roll:
            students.remove(student)
            if save_students(students):
                print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
