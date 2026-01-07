# Write a function that takes name of student and course enrolled as input and display: Hello{std}, Welcome to course {course}. If course is not passed to function it has to be python in default.

def student_info(name, course='Python'):
    print(f"Hello {name}, Welcome to {course}")

student_info("sugam","BIT")
student_info('sugam')


