class emp:
   
    language="python"  
    salary=100000


    def getinfo(self):
        print(f"the languaue is {self.language} and the saalry is {self.salary}")

    @staticmethod
    def greet():    
        print("good night")

harry = emp()
harry.language = "js"           
# print(harry.language,harry.salary)

harry.getinfo()
harry.greet()



