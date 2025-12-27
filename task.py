import json
import os

file_name = "students.json"


# ----------- Helper Functions -----------
def load_students():
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as f:
        return json.load(f)


def save_students(students):
    with open(file_name, "w") as f:
        json.dump(students, f, indent=4)
# ----------- Add Student -----------
def add_student():
    students = load_students()

    print("\n Let's add a new student!")
    sid = input("Enter Student ID: ").strip()

    # check if already exists
    for s in students:
        if s["id"] == sid:
            print(" This ID already exists! Try with a new ID.")
            return

    name = input("Enter Student Name: ").strip()

    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                print(" Age cannot be 0 or negative. Try again.")
                continue
            break
        except:
            print(" Please enter a valid number for age.")

    while True:
        try:
            marks = float(input("Enter Marks: "))
            break
        except:
            print(" Please enter valid marks.")

    student = {"id": sid, "name": name, "age": age, "marks": marks}
    students.append(student)
    save_students(students)

    print(" Student Added Successfully!")


# ----------- View Students -----------
def view_students():
    students = load_students()

    print("\n Showing all student records...")

    if len(students) == 0:
        print(" No students found. Please add some first.")
        return

    print("\n-------------------------------------------------")
    print("ID\tName\t\tAge\tMarks")
    print("-------------------------------------------------")

    for s in students:
        print(f"{s['id']}\t{s['name']}\t\t{s['age']}\t{s['marks']}")


# ----------- Update Student -----------
def update_student():
    students = load_students()

    sid = input("\n Enter Student ID you want to update: ").strip()

    for s in students:
        if s["id"] == sid:
            print(" Student Found! Enter new details")
            print(" Leave empty if you do not want to change")

            name = input("New Name: ").strip()
            age = input("New Age: ").strip()
            marks = input("New Marks: ").strip()

            if name != "":
                s["name"] = name
            if age != "":
                s["age"] = int(age)
            if marks != "":
                s["marks"] = float(marks)

            save_students(students)
            print(" Student Updated Successfully!")
            return

    print(" Student not found!")


# ----------- Delete Student -----------
def delete_student():
    students = load_students()

    sid = input("\n Enter Student ID to delete: ").strip()

    new_list = [s for s in students if s["id"] != sid]

    if len(new_list) == len(students):
        print(" Student not found!")
        return

    save_students(new_list)
    print(" Student Deleted Successfully!")

# Main Loop 
while True:
    print("\n==============================")
    print(" STUDENT RECORD SYSTEM")
    print("1  Add Student")
    print("2  View Students")
    print("3  Update Student")
    print("4  Delete Student")
    print("5 Exit")

    choice = input(" Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\n Thank you! Program closed. Have a great day!")
        break
    else:
        print(" Invalid choice! Please select correct option.")
