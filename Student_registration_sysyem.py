students = []

def register_student():
    name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")
    students.append({"name": name, "matric": matric_number})
    print("Student registered successfully")

def view_students():
    if not students:
        print("No students registered")
    else:
        for student in students:
            print(student["name"], "- Matric No:", student["matric"])

def main():
    while True:
        print("1. Register Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
