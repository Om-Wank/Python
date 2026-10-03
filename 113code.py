from functools import reduce

numbers = [5, 12, 18, 7, 20, 3]

result = reduce(lambda x ,y :x + y ,filter(lambda x:x>10,numbers))
print(result)