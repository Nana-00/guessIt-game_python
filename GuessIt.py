#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:     a guess game for a range of numbers
#
# Author:      Nana
#
# Created:     08/02/2022
# Copyright:   (c) Sample 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    pass

if __name__ == '__main__':
    main()


#This is a guess the number game.
import random
secretNumber = random.randint(1, 30)
print('WELCOME TO THE PLANET OF GUESSES BUDDY!')
print('')
print('LEVEL 1')
print('-------')
print('')
print('I am thinking of a number between 1 and 30')
print('-------------------------------------------')


#Ask the player to make 7 guesses.
for guessesTaken in range(1, 8):
    print('Make a guess gamer')

    numOfChances = 8 - guessesTaken

    print('You have ' + str(numOfChances) + ' chances left')
    print('')

    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber and guess <= 30:
        print('Your guess is too high')
    elif guess < 1:
        print('Oops! Entry is out of range')
    elif guess >= 31:
        print('Oops! Entry is out of range')
    else:
        break #The loop is exited if the above conditions are false


if guess == secretNumber:
            print('Good job! You guessed my number in ' + str(guessesTaken)+ ' guesses')
else:
    print('Game Over! The number I was thinking of was ' + str(secretNumber))
    print('START OVER!!!')


while True:
    if guess == secretNumber:
        break
    elif guess != secretNumber:
        continue


print('')
print('')
print('CONGRATULATIONS!!!')
print('------------------')
print('WELCOME TO LEVEL 2.')
print('------------------')
print('')
import random
secretNumber = random.randint(1, 50)
print('I am thinking of a number between 1 and 50')
print('-------------------------------------------')

#Ask the player to make 5 guesses.
for guessesTaken in range(1, 6):
    print('Make a guess gamer')

    numOfChances = 6 - guessesTaken

    print(f'You have ' + str(numOfChances) + ' chances left')
    print('')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber and guess <= 50:
        print('Your guess is too high')
    elif guess < 1:
        print('Oops! Entry is out of range')
    elif guess >= 51:
        print('Oops! Entry is out of range')
    else:
        break #This condition is the correct guess!


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken)+ ' guesses')
else:
    print('Game Over! The number I was thinking of was ' + str(secretNumber))
    print('START OVER!!!')


while True:
    if guess == secretNumber:
        break
    elif guess != secretNumber:
        continue


print('')
print('')
print('CONGRATULATIONS!!!')
print('------------------')
print('WELCOME TO LEVEL 3')
print('------------------')
print('')
import random
secretNumber = random.randint(1, 70)
print('I am thinking of a number between 1 and 70')
print('-------------------------------------------')

#Ask the player to make 3 guesses.
for guessesTaken in range(1, 4):
    print('Make a guess gamer')

    numOfChances = 4 - guessesTaken

    print(f'You have ' + str(numOfChances) + ' chances left')
    print('')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber and guess <= 70:
        print('Your guess is too high')
    elif guess < 1:
        print('Oops! Entry out of range')
    elif guess >= 71:
        print('Ooop! Entry out of range')
    else:
        break


if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses')
else:
    print('Game Over! The number I was thinking of was ' + str(secretNumber))


while True:
    if guess == secretNumber:
        break
    elif guess != secretNumber:
        continue


print('')
print('')
print('CONGRATULATIONS!!!')
print('------------------')
print('WELCOME TO LEVEL 4')
print('------------------')
print('')
import random
secretNumber = random.randint(2, 80)
if secretNumber % 2 == 1:
    secretNumber = secretNumber + 1
print('I am thinking of a product of 2 between 2 and 80.')
print('-------------------------------------------------')

#Ask the player to make 5 guesses.
for guessesTaken in range (1, 6):
    print('Make a guess gamer')

    numOfChances = 6 - guessesTaken

    print(f'You have ' + str(numOfChances) + 'chances left')
    print('')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber and guess <= 80:
        print('Your guess is too high')
    elif guess < 2:
        print('Oops! Entry out of range')
    elif guess >= 81:
        print('Oops! Entry out of range')
    elif guess % 2 == 1:
        print('Invalid entry')
    else:
        break


if guess == secretNumber:
    print('Good job! You guessed my number in '+ str(guessesTaken) + 'guesses')
else:
    print('Game Over! The number I was thinking of was ' + str(secretNumber))


while True:
    if guess == secretNumber:
        break
    elif guess != secretNumber:
        continue