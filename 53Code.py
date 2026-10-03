#def reverse_string(text ,num):
 #   if(len(text) == num):
  #      return
   # reverse_string(text,num+1)
   # print(text[num])

#reverse_string("python",0)

def reverse_string(text):
    if(text == ""):
        return ""
    return reverse_string(text[1:]) + text[0]

resutl =reverse_string("python")

print(resutl)