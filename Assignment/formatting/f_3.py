 # Take input of name and marks. Display percentage obtained assuming total marks is 80. output format :Ram you have scored 85.23% in exam

student_name = input("Enter your name: ")
student_marks = float(input("Enter your marks: "))
# obtained_marks = 85.23
total_marks = 80

print(f"{student_name} you have scored {(student_marks/total_marks)*100}% in exam")