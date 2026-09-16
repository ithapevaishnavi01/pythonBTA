class emp:
    company="ITC"
    def show(self):
        print(f"the salalry is {self.salary} and the name is {self.name}")        #base class or parent class 


# class programmer:
#     company="ITC info tech"
#     def show(self):
#             print(f"the salalry is {self.salary} and the name is {self.name}")

#     def showlang(self):
#          print(f"the language of {self.name} is {self.lang}")



class programmer(emp):                                  #inherited class or child class
    company="ITC info tech"
    def showlang(self):
       print(f"the language of {self.name} is {self.lang}")

a=emp()
b=programmer()

print(a.company,b.company)
