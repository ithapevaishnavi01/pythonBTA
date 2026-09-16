class emp:
    salary = 432
    increment = 50

    @property
    def Salaryafterinc(self):
        return (self.salary + self.salary * (self.increment / 100))


e = emp()
print(e.Salaryafterinc)
