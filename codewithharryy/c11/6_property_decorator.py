class emp:                     #  Encapsulation ,  bundling data and methods together and controlling access to that data.
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):                               
        self.fname = value.split(" ")[0]                 #abstraction  , hiding unnecessary implementation details and showing only what is necessary.  
        self.lname = value.split(" ")[1]

e = emp()

e.a = 45

e.name = "vaishnavi ithape"

print(e.fname,e.lname)

e.show()