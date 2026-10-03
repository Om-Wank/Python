numbers = [1, 2, 3, 4, 5]

def squares(numbers):
    for x in numbers:
        yield x*x

result = squares(numbers)

for x in result:
    print(x)

