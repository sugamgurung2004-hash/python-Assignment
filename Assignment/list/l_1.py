# Store the marks of student in a list called student_marks. You need to store marks of 5 subjects. If marks in either of the student is below 40 display,You've failed but if marks in all subject is above 40 display the grade as congrgulation !! You've passed in grade{calculatesd_grade}


maths=float(input("Enter the marks in Maths:"))
science=float(input("Enter the marks in Science:"))
english=float(input("Enter the marks in English:"))
nepali=float(input("Enter the marks in Nepali:"))
gk=float(input("Enter the marks in GK:"))

student_marks=[maths,science,english,nepali,gk]         

min_marks=min(student_marks)

if min_marks<0:
    print("Invalid marks")
elif min_marks<40:
    print("You've failed!")
else:
    # Calculate average for grade
    Total_marks=sum(student_marks) 
    avg = Total_marks/ 5

    print(f"Congratulations!! You've passed with grade {avg}")
