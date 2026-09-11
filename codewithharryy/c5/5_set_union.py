s1 = {11,12}
s2 = {12,13,14}
s3 = s1.union(s2) # union of two sets
print(s3)

s4= s1.intersection(s2) # intersection of two sets , common elements
print(s4)

s5= s1.difference(s2) # difference of two sets , elements present in s1 but not in s2
print(s5)

s6= s1.issubset(s2) # checks if s1 is subset of s2
print(s6)

s7= s1.issuperset(s2) # checks if s1 is superset of s2
print(s7)
