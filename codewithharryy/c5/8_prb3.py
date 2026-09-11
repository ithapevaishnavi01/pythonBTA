s= set()
s.add(1)
s.add("1")
print(s)    #returns the set with string and integer as two different values because they are of different data types4


b = set()
b.add(1)
b.add(1.0)      
b.add("1")
print(b)    #returns the set with only one value because 1 and 1.0 are considered equal in Python