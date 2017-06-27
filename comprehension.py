import random # imports random module for later use

guessesTaken = 0 # assigns 0 to guessesTaken variable

print('Hello! What is your name?') # prints a message - Hello! What is your name? - in terminal
myName = input() # awaits a user input and assigns it to myName

number = random.randint(1, 20) # creates a random number between 1 and 20 and assings it to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # prints myName between two predefined strings

while guessesTaken < 6: # iterates through the guessesTaken variable one by one
    print('Take a guess.') # prints "Take a guess" in terminal
    guess = input() # awaits user input and assigns it to guess
    guess = int(guess) # converts the input string into int

    guessesTaken += 1 # increments guessesTaken by one

    if guess < number: # checks if the number input is smaller than the random one generated above
        print('Your guess is too low.') # prints string message

    if guess > number: # checks if the number input is greater than the random one generated above
        print('Your guess is too high.') # prints string message

    if guess == number: # checks if the number input equals the random one generated above
        break # breaks the loop

if guess == number: # checks if the number input equals the random one generated above
    guessesTaken = str(guessesTaken) # converts the iterating variable's current state into string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # prints win message containing the name and guesses taken

if guess != number: # checks if the number input does not match the random one generated above
    number = str(number) # converts the random number generated above into string
    print('Nope. The number I was thinking of was ' + number) # prints loser message with the random number in it.
