
try:
    a= int (input("enter a no :"))
    print(a)

except ValueError as v:
    print(v)
except Exception as e:
    print(e)

print("thanku")