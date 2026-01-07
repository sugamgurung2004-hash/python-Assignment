#Broadway offers courses,store them as format:{'course':['Python','Java'],'duration':[3,4]}.Check if 'Python' is offered course.


BW_courses={'courses':['Python','Java'],'duration':[3,4]}

if 'Python' in BW_courses['courses']:
    print("Python is offer in Broadway courses")
else:
    print("Python is not offer in Broadway courses")

