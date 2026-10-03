def count_up_to(n):
    for x in range(1,n+1):
        yield x

result = count_up_to(5)

print(next(result))
print(next(result))
print(next(result))
