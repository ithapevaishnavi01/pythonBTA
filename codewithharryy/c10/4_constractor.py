class emp:
   
    language="python"  
    salary=100000

    def __init__(self,name,salary,language):                #dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getinfo(self):
        print(f"the languaue is {self.language} and the saalry is {self.salary}")

    @staticmethod
    def greet():    
        print("good night")

harry = emp("vaishnavi",1000000000,"py")
harry.name = "harry"           
print(harry.language,harry.salary,harry.name)






