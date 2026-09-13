# Write a resursive function to print all elements in a list

list = [1,2,6,5,2,8,3,67,8,]

def printfunlis(lists ,idx):
    if(idx == len(lists)):
        return 
    print(lists[idx])
    return printfunlis(lists , idx + 1)     

printfunlis(list , 0)
