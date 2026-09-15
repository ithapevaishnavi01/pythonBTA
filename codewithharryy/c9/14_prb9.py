with open("poem.txt") as f:
    content1 = f.read()

with open("log.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("content is same")
else:
    print("content is not same")

