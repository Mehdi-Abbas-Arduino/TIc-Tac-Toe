import random

def number():
    num = random.randint(1, 100)
    return num

guess = number()
count = 0
max_attempts = 10

for i in range(max_attempts):
    user = int(input("Guess number from 1 to 100: "))
    if user >= 1 and user <= 100:
        count += 1
        if user == guess:
            print("You win")
            break
        elif user < guess:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print("Please enter a number between 1 and 100.")

if count == max_attempts and user != guess:
    print("You lose. The number was:", guess)
