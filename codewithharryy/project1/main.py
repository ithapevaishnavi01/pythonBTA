'''
1=snake
-1 = for water
0 = for gun
'''

import random

computer = random.choice([1,-1,0])

youStr = input("Enter your choice: ")

youDict = {"1": 1, "2": -1, "3": 0}

rev_dict={1:"snake",-1:"water",0:"gun"}

you = youDict[youStr]


#we have 2 nos (variables) you and computer

print(f"you chose {rev_dict[you]} \ncomputer chose {rev_dict[computer]}")

if computer == you:
    print("its drow")
else:
    if computer == -1 and you== 1:
        print("you win")

    elif computer == -1 and you == 0:
        print("computer win")

    elif computer == 1 and you == -1:
        print("compuuter win")

    elif computer == 1 and you == 0:
        print("compuuter win")

    elif computer == 0 and you == -1:
        print("compuuter win")

    elif computer == 0 and you == 1:
        print("you win")

    else:
        print("something went wrong")