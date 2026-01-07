# Given a list containing students’ marks, display the second highest number from the list.

student_marks = [20, 22, 82, 10, 80, 23, 56, 34, 75, 82, 45]
student_set = set(student_marks)

highest = max(student_marks)
student_set.discard(highest)
print(max(student_set))