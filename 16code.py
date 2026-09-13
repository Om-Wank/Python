# WAF to print the elements of a list in a single line

def elements(a):

    for val in range(0,len(a)):
        print(a[val],end = " ")
    print()

list = [1,4,6,3,6,38,3,9,345]
elements(list)
