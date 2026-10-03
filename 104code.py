numbers = [-2, 1, -5, 3, 4, -1]

def positive_numbers(numbers):
    for x in numbers:
        if x > 0:
            yield x


def double_numbers(numbers):
     for x in numbers:
         yield x*2

result1 = positive_numbers(numbers)
result2 = double_numbers(result1)

for x in result2:
    print(x)
    