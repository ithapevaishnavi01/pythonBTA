class a():
    a=1

class b(a):
    b=2

class c(b):
    c=3


d=c

print(c.b)
print(c.a)