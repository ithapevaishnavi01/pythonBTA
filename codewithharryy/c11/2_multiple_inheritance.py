class emp:
    company = "ITC"
    name = "hello"
    salary = 300000

    def show(self):
        print(f"the salary is {self.salary} and the name is {self.name}")


class coder:
    language = "python"

    def printlang(self):
        print(f"your language is {self.language}")


class programmer(emp, coder):
    company = "ITC info tech"

    def showlang(self):
        print(f"the language of {self.company} is {self.language}")

a = emp()
b = programmer()
c = coder()

print(a.company)
print(b.company)
c.printlang()