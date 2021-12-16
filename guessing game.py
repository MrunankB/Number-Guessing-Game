import random as r
r = r.randrange(1, 10)

guess = int(input("Enter your first guess: "))
if guess == r:
    print("Congo! You win!")
elif guess > r:
    print("No! My number is Smaller...")
else:
    print("No! My number is larger...")
    
if guess != r:
    guess = int(input("\nEnter your 2nd guess: "))
    if guess == r:
        print("Congo! You win!")
    elif guess > r:
        print("No! My number is Smaller...")
    else:
        print("No! My number is larger...")
        
if guess != r:
    guess = int(input("\nEnter your 3rd guess: "))
    if guess == r:
        print("Congo! You win!")
    elif guess > r:
        print("No! My number is Smaller...")
    else:
        print("No! My number is larger...")
        
if guess != r:
    guess = int(input("\nEnter your 4th guess: "))
    if guess == r:
        print("Congo! You win!")
    elif guess > r:
        print("No! My number is Smaller...")
    else:
        print("No! My number is larger...")
        
if guess != r:
    guess = int(input("\nEnter your 5th guess: "))
    if guess == r:
        print("Congo! You win!")
    else:
        print("Better Luck Next Time!")
        print(" My number was ")
        print(guess)