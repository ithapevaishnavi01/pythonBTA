class emp:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


e = emp()

e.a = 45

e.name = "vaishnavi"

print(e.name)

e.show()