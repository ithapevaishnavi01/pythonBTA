a=25
b=5
c=987

def fun(a,b,c):
    if(a > b and a> c):
        print("a is greater")
    elif(b > a and b > c):
        print("b is greater")
    elif ( c > b and c > a):
        print("cc is greater")

fun(a,b,c)