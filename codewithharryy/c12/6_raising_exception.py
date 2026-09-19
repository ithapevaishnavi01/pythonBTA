a = int (input("enetr a no 1: "))
b = int (input("enetr a no 2 : "))

if (b==0):
    raise ZeroDivisionError("do not divide by 0")
else:
    print(f"division a/b is : {a/b}")