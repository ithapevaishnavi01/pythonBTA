k = {} #empty dictionary


marks = {
    "vaishnavi": 90,
    "vinod": 80,
    "Aditi": 70,
    "list": [1, 2, 3, 4, 5],
    0:"zero",
    "rit":100
}

print(marks.items())  # prints the items of the dictionary as a list of tuples
print(marks.keys())  # prints the keys of the dictionary as a list
print(marks.values())  # prints the values of the dictionary as a list
marks.update({"vaishnavi": 100})  # updates the value of key "vaishnavi" to 100


print(marks)  # prints the updated dictionary




print(marks.get("vaishnavi"))  # prints the value of key "vaishnavi" which is 100
print(marks ["vaishnavi"])  # prints the value of key "vaishnavi" which is 100

# if we try to access a key that does not exist in the dictionary, it will raise a KeyError in print(marks["vaishnavi"]) , 
# but print(marks.get("vaishnavi")) will return None instead of raising an error


# get() – Returns the value of a specified key.
# keys() – Returns all keys in the dictionary.
# values() – Returns all values in the dictionary.
# items() – Returns all key-value pairs.
# update() – Adds new data or updates existing data.
# pop() – Removes a specified key and returns its value.
# popitem() – Removes and returns the last key-value pair.
# clear() – Removes all items from the dictionary.
# copy() – Creates a copy of the dictionary.
# setdefault() – Returns a key's value; adds it if the key doesn't exist.
# fromkeys() – Creates a new dictionary using given keys.