#! python3

# Rick and Morty episode guessing game

import random
maxNum = 31
minNum = 1
rickNum = random.randint(minNum, maxNum) # Rick's episode

print()
print('Hey Morty! *burrrrrp* Heyy Morrrtyyyy!')
print('I-I\'m thinking of an episode Morty, try and guess it!')
#print('DEBUG: Rick chose episode ' + str(rickNum))
print()

firstGuess = int(input('Guess a number: '))
print()

if firstGuess == rickNum:
    print('What the fuck...nice guess Morty! That\'s like a 0.032% chance')
    print('I can\'t believe you fuckin guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    exit()
elif firstGuess < 0:
    print('Way to waste a guess on a NEGATIVE number Morty, hats...hats off to you')
elif firstGuess > 0 and firstGuess <= maxNum:
    print('Close but no cigar Mortyy, there\'re only ' + str(maxNum) + ' episodes') # hint at parameters
    if firstGuess > rickNum:
        print('Take it down a notch buddy, that was too high!')
    else:
        print('Lol gotta get it up buddy, too low!')
else:
    print('Wrong! Haha, *burrp* there\'s only ' + str(maxNum) + ' epsidodes dumbass')
    # by default, any other guess is greater than maxNum

for guessesTaken in range(2, 6):  # gives morty 5 guesses, starting at 2 counts firstGuess  
    print('*burrrp* guess again Moertyy')
    #print('DEBUG: Rick chose episode ' + str(rickNum))
    print()
    guess = int(input('Guess a number: '))
    print()
    try:
        if guess == 0:
            print('Nice, wasting a precious guess on a goose egg, real smooth...')
        elif guess < 0:
            print('I\'m not asking you about your IQ Morty, pick a positive number...')
        elif guess > maxNum:
            print('I just said there\'re only ' + str(maxNum) + ' episodes...you deserve to lose')
        elif guess < rickNum:
            print('Tooo looowww brooo...')
        elif guess > rickNum:
            print('Little too high Mortyy, just like grandpa!')
        else:
            break # condition for the correct guess
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