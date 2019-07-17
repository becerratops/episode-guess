# Rick and Morty episode guessing game
# Author: Adam Becerra

import random
maxNum = 31
minNum = 1
# Rick's episode
rickNum = random.randint(minNum, maxNum) 

print('\nHey Morty! *burrrrrp* Heyy Morrrtyyyy!')
print('I-I\'m thinking of an episode Morty, try and guess it!')
# print('DEBUG: Rick chose episode ' + str(rickNum))
print()

# Take input, convert into an integer
firstGuess = int(input('Guess a number: '))
print()

# Hole in One
if firstGuess == rickNum:
    print('What the fuck...nice guess Morty! That\'s like a 0.032% chance')
    print('I can\'t believe you fuckin\' guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    exit()
# Guess is a possible episode
elif firstGuess >= minNum and firstGuess <= maxNum:
    # hint at parameters
    print('Close but no cigar Mortyy, there\'re only ' + str(maxNum) + ' episodes') 
    if firstGuess > rickNum:
        print('Take it down a notch buddy, that was too high!')
    else:
        print('Lol gotta get it up buddy, too low!')
# Guess too large
elif firstGuess > maxNum:
    print('Wrong! Haha, *burrp* there\'s only ' + str(maxNum) + ' epsidodes, dumbass')
# Guess is negative
elif firstGuess < 0:
    print('Way to waste a guess on a NEGATIVE number Morty, hats...hats off to you')
# Guess is 0
else:
    print('It\'s not 0 you fucking loser...')

# Give morty 5 guesses (count is now 2, counting the first guess)
for guessesTaken in range(2, 6):    
    print('*burrrp* guess again Moertyy')
    # print('DEBUG: Rick chose episode ' + str(rickNum))
    print()
    guess = int(input('Guess a number: '))
    print()
    try:
        if guess == rickNum:
            break 
        elif guess >= minNum and guess <= maxNum:
            if guess > rickNum:
                print('Little too high Mortyy, just like grandpa!')
            elif guess < rickNum:
                print('Tooo looowww brooo...')
        elif guess > maxNum:
            print('I just said there\'re only ' + str(maxNum) + ' episodes...you deserve to lose')
        elif guess < 0:
            print('I\'m not asking you about your IQ Morty, pick a positive number...')
        else:
            print('Nice, wasting a precious guess on a goose egg, real smooth...')
    except ValueError:
        print('Yeah, that\'s not a number, guess again you little turd...')

if guess == rickNum:
    print('You guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    if guessesTaken == 5: # condition for last minute win
        print('On the last guess too, close one! I was about to verbally abuse the \n' +
              'shit out of you if you didn\'t guess that haha')
        print()
    else:
        print(str(guessesTaken) + ' guesses, not bad Morty!')
        print()
else:
    print('Your feeble capacity to guess an episode from a finite number set \n' +
          'is making me SOBER, Morty! I was thinking of episode ' + str(rickNum) + '...')
    print()