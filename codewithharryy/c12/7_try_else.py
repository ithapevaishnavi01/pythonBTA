
try:
    a= int (input("enter a no :"))
    print(a)


except Exception as e:
    print(e)                       
else:                                      #goes in else condition when try is sucessful
    print("i am inside else")

print("thanku")