s = {3 ,346, 3, 4, 5, 6, 7, 8, 9, 10,1,2,32,2,2,2,22,"vaish"}

print(s , type(s))  # prints the set with unique values only and its type which is set

# s.add(100)  # adds 100 to the set
s.remove( 5)
print(s)  


# add() – Adds an element.
# remove() – Removes an element; error if not found.
# discard() – Removes an element; no error if not found.
# union() – Combines two sets without duplicates.
# intersection() – Finds common elements.
# difference() – Finds elements present only in the first set.
# issubset() – Checks if one set is contained in another.
# issuperset() – Checks if one set contains another.
# isdisjoint() – Checks if two sets have no common elements.
#pop() – Removes and returns a random element.