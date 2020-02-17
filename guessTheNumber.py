#Guess the number game
import random
myNumber = random.randint(1,30)
print("I am thinking of a number between 1 and 30.")

#Asking player to guess 6 the number 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < myNumber:
        print('Your guess is too low.')
    elif guess > myNumber:
        print("Your guess is too high.")
    else:
        break   #This is the correct guess.

if guess == myNumber:
    print("You guessed my number in " + str(guessesTaken) + "guesses!"))
else:
    print("The number I was thinking of was " + str(myNumber))