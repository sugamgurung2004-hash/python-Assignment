# Broadway_1 offers the courses:{'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}
# Broadway_2 offers the course:{'multimedia': {'duration': 2, 'type': 'basic'}}.
# Broadway_1 and Broadway_2 have merged into a single institute. Combine all the courses


Broadway_1={'python': {'duration': 3, 'type': 'basic'}, 'java': {'duration': 4, 'type': 'medium'}}
Broadway_2={'multimedia': {'duration': 2, 'type': 'basic'}}

Broadway_1.update(Broadway_2)
print(Broadway_1)
