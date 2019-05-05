# Rick and Morty episode guessing game
import random
maxNum = 31
rickNum = random.randint(1, maxNum)

print('Hey Morty!')
print('*burrp*')
print('Heyy Morrrtyyyy!')
print('I-I\'m thinking of an episode Morty, try and guess it!')

firstGuess = int(input())

if firstGuess == rickNum:
    print('What the fuck...nice guess Morty!')
    print('You guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    exit()
elif firstGuess < 0:
    print('Way to waste a guess on a NEGATIVE number Morty, hats...hats off to you')
elif firstGuess > 0 and firstGuess <= maxNum:
    print('Close but no cigar Mortyy, there\'re only ' + str(maxNum) + ' episodes')
    if firstGuess > rickNum:
        print('Take it down a notch buddy, that was too high!')
    else:
        print('Lol gotta get it up buddy, too low!')
else:
    print('Wrong! Haha, *burrp* there\'s only ' + str(maxNum) + ' epsidodes dumbass')

for guessesTaken in range(2, 7):  # gives morty 5 guesses, starting at 2 counts the first guess above 
    print('*burrrp* guess again Moertyy')
    guess = int(input())
    try:
        if guess < rickNum:
            print('Tooo looowww brooo')
        elif guess > rickNum:
            print('Little too high Mortyy, just like grandpa!')
        else:
            break
    except ValueError:
        print('Yeah, that\'s not a number, guess again you little turd...')

if guess == rickNum:
    print('You guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    print(str(guessesTaken) + ' guesses, not bad Morty!')
else:
    print('Your feeble capacity to guess an episode from a finite number set')
    print('is making me sober Morty! The episode was number ' + str(rickNum) + '!')