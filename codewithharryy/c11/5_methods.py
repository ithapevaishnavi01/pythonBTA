class emp:
    a = 1                  #class attribute 

    @classmethod
    def show(self):
        print(f"the value of a is {self.a}")



e = emp()
e.a=45                    #instance attribute
  
e.show()