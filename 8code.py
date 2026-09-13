dis = {}

x = int(input("Enter a math score: "))
dis.update({
   "math" : x
})
x = int(input("Enter a physics score: "))
dis.update({
    "physics" : x
})

print(dis)