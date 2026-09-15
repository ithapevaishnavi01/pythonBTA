

f = open("file.txt")

print(f.read())

f.close()

# the same can be return using with statemnet with this

with open("file.txt") as f:   #with statemnt open and close the file automatically
    print(f.read())

# you dont have to explicitly close the file