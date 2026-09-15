import random

computer = random.choice([1,-1,0])

youStr = input("Enter your choice: ")

youDict = {"1": 1, "2": -1, "3": 0}

rev_dict={1:"snake",-1:"water",0:"gun"} 

you = youDict[youStr]


#we have 2 nos (variables) you and computer

print(f"you chose {rev_dict[you]} \ncomputer chose {rev_dict[computer]}")


#the below logic is written on the basis of the value of computer -you
if((computer - you == -1) or (computer - you == 2)):
    print("computer win")
else:
    print("you win")