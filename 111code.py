numbers = [5, 12, 18, 7, 20, 25, 30, 9]

result = filter(lambda x: x % 2==0 and x > 10 ,numbers)
print(list(result))