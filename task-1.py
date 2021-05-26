import random

# a random float from 1 t0 100
random.random()

guess = int(input("enter a number"))
number = random.randint(1, 100)
count = 1

while guess<=100 and guess>=1:
    count+=1
    if guess > number:
        print("Your guess is too high")
        guess = int(input("enter a number"))
    elif guess < number:
        print("Your guess is too low")
        guess = int(input("enter a number"))
    else:
        print("Your guess was correct")
        print("your tries are", + count)
        break
