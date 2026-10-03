def even_num(n):
    for x in range(1,n+1):
        if(x % 2 == 0):
            yield x
result = even_num(10)

for x in result:
    print(x)