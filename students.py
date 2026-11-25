students = []

def validate_student(name):
    if not name.strip():
        return False
    return True


def add_student(name):
    if not validate_student(name):
        print("Invalid student name")
    elif name in students:
        print("Student already exists")
    else:
        students.append(name)
        print("Student added successfully")

def delete_student(name):
    name = name.strip()

    if name in students:
        students.remove(name)
        print("Student deleted successfully")
    else:
        print("Student not found")


def show_students():
    if not students:
        print("No students found")
    else:
        print("Student list:")
        for student in students:
            print(student)


