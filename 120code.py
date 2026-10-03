students = [
    {"name": "Om", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Amit", "score": 78},
    {"name": "Rohan", "score": 95}
]

result = sorted(students,key = lambda x :x["score"], reverse =True)

for x in result:
    print(x["name"])