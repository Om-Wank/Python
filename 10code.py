#loop for

list = (1,3,5,6,7,8)

x = int(input("Enter the the value"))

for val in list:

    if(x == val):
     print("found " ,val)
     break
else:
    print("Not found")