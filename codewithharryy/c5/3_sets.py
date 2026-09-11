d = set() #empty set dont use {} for empty set because it will create an empty dictionary

s = {3 ,346, 3, 4, 5, 6, 7, 8, 9, 10,1,2,32,2,2,2,22,}
print(type(s))  
print(s)  # prints the set with unique values only


#we cant do indexing in set because it is unordered collection of data and we cant access the elements by index
# all element in the set should me immutable data type like int, float, string, tuple etc.
# but we can add mutable data type like list, dictionary, set etc. in the set   but can cahnge the value of that 
# mutable data type in the set because it is unhashable data type and it will give error