def multiply_all(*arge):
    mult = 1
    for num in arge:
        mult *=num
    return mult

print(multiply_all(2,3,4))