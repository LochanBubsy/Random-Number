import random

def guess():
        x=random.randint(0,9)
        
        a = int(input("Guess a random number from 1 to 9:"))
        if a<x:
            print("You are lower than estimation")
            print(x)
        elif a==x:
            print("You are, to our estimation")
            print(x)
        else: 
            print("Conguratulations you have got the big prize")
            print(x)
guess()