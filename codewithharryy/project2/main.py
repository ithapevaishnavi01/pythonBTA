import random
n = random.randint(1,100)
a = -1 
guesses=1
while(a != n ):
    guesses += 1 
    a = int(input("Guess the no : "))
    if(a > n):
        print("lower no please!")
        guesses += 1
    elif(a<n):
        print("higher no please!")
        guesses += 1 


print(f"you have guess the no {n}, in {guesses} attempts")
