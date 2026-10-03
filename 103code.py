numbers = [1, 2, 3, 4, 5, 6]

def squear_even(numbers):
    for x in numbers:
        if x % 2 == 0:
            yield x*x

result = squear_even(numbers)

for x in result:
    print(x)