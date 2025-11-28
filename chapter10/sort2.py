students = [
    {'name' : 'Kim',  'age' : 21, 'grade' : 'A'},
    {'name' : 'Lee', 'age' : 19, 'grade' : 'B'},
    {'name' : 'Choi', 'age' : 20, 'grade' : 'C'},
    {'name' : 'Park', 'age' : 22, 'grade' : 'A'},
    {'name' : 'Song', 'age' : 21, 'grade' : 'B'}
]

sorted_students = sorted(students, key=lambda x: (x['age'], -ord(x['grade'])))
print(sorted_students)