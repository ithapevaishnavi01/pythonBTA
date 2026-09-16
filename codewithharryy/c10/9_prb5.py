from random import randint

class train:

    def __init__(self,trainno):
        self.trainno=trainno

    def book(self,fom,to):
        print(f"book ticket is book in train no P{self.trainno} from {fom} to {to}")

    def getStatus(self,):
        print(f"train no {self.trainno} is running on time")

    def getFare(self,fom,to):
         print(f"book ticket is book in train no P{self.trainno} from {fom} to {to} is {randint(222,5555)}")

t = train(2356)
t.book("pune", "mumbai")
t.getStatus()
t.getFare("pune", "mumbai")

