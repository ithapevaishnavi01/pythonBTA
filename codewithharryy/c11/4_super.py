class emp:
    def __init__(self):
        print("constructor of emp")

    a = 1


class programmer(emp):
    def __init__(self):
        print("constructor of programmer")

    b = 2


class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructor of manager")

    c = 3


d = manager()

print(d.a, d.b, d.c)