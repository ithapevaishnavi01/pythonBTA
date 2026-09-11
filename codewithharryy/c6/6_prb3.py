p1="hello"
p2="hhhheyyy"

message = input("enter the comment:")

if p1 in message.lower() or p2 in message.lower():   #using lower it solve the issue of enetring the string in capitale and smaller
    print("its hi hello")
else:
    print("anything else")
