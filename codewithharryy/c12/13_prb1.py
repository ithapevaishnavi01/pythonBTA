try :
    with open ("my1.txt", "r")as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open ("my2.txt", "r")as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open ("my3.txt", "r")as f:
        print(f.read())
except Exception as e:
    print(e)