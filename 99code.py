numbers = [1, 2, 3, 4, 5, 6]

def even_squares(numbers):
   return (x*x for x in numbers if (x % 2 == 0))


result = even_squares(numbers)

for value in result:
    print(value)