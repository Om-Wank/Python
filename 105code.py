def first():
    yield 1
    yield 2
    yield 3

def second():
    yield 4
    yield 5
    yield 6

def combined():
    yield from first()
    yield from second()

for x in combined():
    print(x)