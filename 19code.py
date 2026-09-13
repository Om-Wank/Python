  #recursion

def show(a):
    if(a == 0):
        return
    print(a)
    show(a-1)

show(5)    