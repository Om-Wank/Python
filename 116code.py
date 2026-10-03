def create_user(name, age, role):
    print(name, age, role)

user = {
    "name": "Om",
    "age": 25,
    "role": "Developer"
}

create_user(**user)