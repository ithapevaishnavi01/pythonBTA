try :
    a = int (input("enetr a : "))
    b = int (input("enetr b : "))
    print(a/b)
except ZeroDivisionError as v :
    print("infinite")