# Student records are stored as
# {'9843': {'course': 'python', 'name': 'abc', 'present': True}, '984': {'course': 'c', 'name': 'efg', 'present': False}}.Display name of students who are absent in python class.

student_records = {
    "9843": {"course": "python", "name": "abc", "present": True},
    "984": {"course": "c", "name": "efg", "present": False},
}

for student in student_records.values():
    if student["course"] == "python" and student["present"] == True:
        print(f"{student["name"]} is absent in python class")


    # elif student["course"] == "c" and student["present"]== False:
    #     print(student["name"])

