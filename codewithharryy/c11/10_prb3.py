class emp:
    salary = 432
    increment = 50

    @property
    def Salaryafterinc(self):
        return (self.salary + self.salary * (self.increment / 100))

    @increment.setter
    def increment(self,salary):
        
e = emp()
print(e.Salaryafterinc)
