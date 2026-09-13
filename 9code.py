
num = (1,4,9,16,25,36,46,81,100)

x = int(input("Enter the number that need to find:"))
i=0

while(i<len(num)):
    if(num[i] == x):
      print("find")
      break
      i+=1

    else:
       print("Not find")  
    