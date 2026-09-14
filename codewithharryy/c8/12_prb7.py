

def rm(l,word):
    n = []

    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
       

l = ["vaihs", "heyoy","aditi","yoy"]
print(rm(l,"yoy"))





# def fun(l,word):
#     n =[]
#     for item in l:
#         if(item == word):
#             n.append(item.strip(word))
#     return n 

# list=
# print(fun(...))


    
#  l.remove(word)
#         return l