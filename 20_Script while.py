#1
i=0
liczba=0
poprzednia_liczba=0
while i<50:
    liczba=i+poprzednia_liczba
    print(poprzednia_liczba,'+',i,'=',liczba)
    poprzednia_liczba=liczba
    i+=1
#2
import random
my_number = random.randint(0,20)
guess=-1
trials = 0
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    trials+=1
    
    if guess == my_number:
        print("You are right! It was:",my_number,"You needed",trials,"trials.")
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")
