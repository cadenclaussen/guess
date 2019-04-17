import random


def debug(s):
  print("[DEBUG: " + s + "]")


def validate(guessString):
  if guessString.isdigit() == False:
    print('Your guess must be a number')
    return False
  guess = int(guessString)
  if guess > 25:
    print('Your guess must be between 1 and 25!!!')
    return False
  if guess < 1:
    print('Your guess must be between 1 and 25!!!')
    return False
  return True


print("Hi, what is your name?")
name = input()

print("Hi " + name + ", I have a random number between 1 and 25, can you guess it?")
randomNumber = random.randint(1, 25)
debug("Random number: " + str(randomNumber))

numberOfGuesses = 1
winner = False

while numberOfGuesses <= 6 and winner == False:

  print("Make a guess [count " + str(numberOfGuesses) + "]: ")
  guessString = input()

  valid = validate(guessString)
  if (valid == False):
    continue

  guess = int(guessString)

  if guess < randomNumber:
    print("You are too low!")

  if guess > randomNumber:
    print("You are too high!")

  if guess == randomNumber:
     print('You won')
     winner = True

  numberOfGuesses = numberOfGuesses + 1
