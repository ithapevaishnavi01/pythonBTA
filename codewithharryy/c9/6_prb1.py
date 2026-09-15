f = open("poem.txt")
c = f.read()

if ("twinkle" in c):
    print("twinkel is present in the content")
else:
    print("twinkel is not present in the content")
 
f.close()