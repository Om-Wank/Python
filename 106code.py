def count():
    yield 10
    yield 20
    yield 30

result = count()
print(next(result))
print(next(result))
print(next(result))
print(next(result))