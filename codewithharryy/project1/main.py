'''
1=snake
-1 = for water
0 = for gun
'''


computer = -1

youStr = input("Enter your choice: ")

youDict = {"1": 1, "2": -1, "3": 0}

you = youDict[youStr]


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