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