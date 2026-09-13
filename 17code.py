# WAF to find the factorial of n


def factorial(a):
    b=1
    for val in range(1 ,a +1):
        b *=val
    return b 
print(factorial(int(input("Enter the number that i want factorial: "))))