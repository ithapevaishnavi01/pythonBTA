import random
n = random.randint(1,100)
a = -1 
guesses=0
while(a != n ):
    guesses += 1 
    a = int(input("Guess the no : "))
    if(a > n):
        print("lower no please!")
    else:
        print("higher no please!")

print(f"you have guess the no {n}, in {guesses} attempts")
