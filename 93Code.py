students = [
    {"name": "Om", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Rohan", "marks": 65}
]

print([student["name"] for student in students if student["marks"] >= 80])