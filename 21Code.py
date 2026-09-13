# write a resursive funtion to calculate the sum of first n natural numbres

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1)+n

print(sum(int(input("Enter the n natural number"))))    

