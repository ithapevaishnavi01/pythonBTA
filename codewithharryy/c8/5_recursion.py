'''
factorial(5)=5x4x3x2x1

factorial(n)- n * factorial(n-1)

''' 
def fact(n):
    if (n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int (input("eneter a no :" ))
print(f"factorail of the no is {fact(n)}")

