import random
myNumber = random.randint(1,20)

print("Guess a number between 1 and 20, You have 5 guesses!")
guessesTaken = 0

allGuesses = []

while guessesTaken <5:
    guess = input()
    guess = int(guess)

    guessesTaken += 1
    allGuesses.append(guess)

    if guess < myNumber:
         print('Your guess is too low. Try again!') 

    if guess > myNumber:
         print('Your guess is too high. Try again!') 
    
    if guess == myNumber:
        break

if guess == myNumber:
    guessesTaken = str(guessesTaken)
    myNumber = str(myNumber)
    print('Good Job! You guessed the number ' + myNumber + ' in ' + guessesTaken + ' guesses!') 
else:
    myNumber = str(myNumber)
    print('Nope. The number I was thinking of was ' + myNumber)

