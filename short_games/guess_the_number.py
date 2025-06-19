# Guessing Game

import random

#x = 6   # number to be guessed
x = random.randint(1,100)
print('------------------------')
print("Hello Welcome to this game!")
print('------------------------')
print('------------------------')
print("Rules are Simple: ")
print("I have choosen a number from 1-100 and you need to guess it.")
print("Don't worry, there will be hints.")
print('------------------------')
print("Heyy Guess the number.")

attempts = 0
guess = -1
while guess != x:
    guess = int(input(": "))
    diff = x - guess if x > guess else guess - x
    attempts += 1
    if diff > 10:
        print("Hint: Your Guess is too Low." if x > guess else "Hint: Your Guess is too High.")
    elif diff > 5:
        print("Hint: Your Guess is Low." if x > guess else "Hint: Your Guess is High.")
    elif diff > 0:
        print("Hint: You are Close!!")
    else :
        break

print("\nFinally You have guessed it correct.")
print("Here's the result.")
print('-------------------')
print(f"Actual Number: {x}")
print(f"You guessed it in {attempts} attempts.")
