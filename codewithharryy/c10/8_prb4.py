class cal:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"{self.n*self.n} is square")

    def cube(self):
            print(f"{self.n*self.n*self.n} is cube")

    def squareroot(self):
            print(f"{self.n**1/2} is squareroot")

    @staticmethod      #when you does not need object, not need to use "self"
    def yo():
          print("hello there!")

a=cal(4)
a.square()
a.cube()
a.squareroot()
a.yo()