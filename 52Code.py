def power(num1,num2):
    if num2 == 0:
        return 1
    mult =num1*power(num1,num2-1)
    return mult

print(power(2,4))