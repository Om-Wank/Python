def sum_n(num):
    if num == 0:
        return 0
    sum = num + sum_n(num -1)
    return sum

print(sum_n(5))   