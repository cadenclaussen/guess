import random

guessCount = 0

print('Hello!  What is your name?')
name = input();

number = random.randint(1, 25)

for guessCount in range(6):
    print('Take a guess: ')
    guess = input()
    guess = int(guess)

    if guess == number:
        break

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

if guess == number:
    guessCount = str(guesCount + 1)
    print('Good job!  You guessed my number in ' + guessCount + ' guesses.')

if guess != number:
    print('Sorry, my number was ' + number)
