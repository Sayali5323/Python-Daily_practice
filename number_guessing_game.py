import random

print("Welcome to Number Guessing Game!")

a=random.randint(1,50)
attempts=0

while True:
    num1=int(input("Guess a number between 1 and 50:"))
    attempts+=1
    if num1>a:
        print("Too High!")
    elif num1<a:
        print("To Low!")
    else:
        print("Congratulations! You guessed correctly.")
        break

print("Total attempts:",attempts)

