from collections import defaultdict

words = [
    ("fruit", "apple"),
    ("fruit", "banana"),
    ("vegetable", "carrot"),
    ("fruit", "mango"),
    ("vegetable", "potato")
]

data = defaultdict(list)


for x,y in words:
    data[x].append(y)

print(data)    