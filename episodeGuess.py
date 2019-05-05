# Rick and Morty episode guessing game
import random
maxNum = 31
rickNum = random.randint(1, maxNum)

print('Hey Morty!')
print('*burrp*')
print('Heyy Morrrtyyyy!')
print('I-I\'m thinking of an episode Morty, try and guess it!')

# Change input into an integer
firstGuess = int(input())

# If input is in between first and latest episode enter here
if firstGuess > 0 and firstGuess <= maxNum:
    # Hole in one
    if firstGuess == rickNum:
        print('What the fuck...nice guess Morty!')
        print('You guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
        exit()
    # Keep swinging
    else:    
        print('Close but no cigar Mortyy, there\'re only ' + str(maxNum) + ' episodes')
        if firstGuess > rickNum:
            print('Take it down a notch buddy, that was too high!')
        else:
            print('Lol gotta get it up buddy, too low!')
# Condition for negative input
elif firstGuess < 0:
    print('Way to waste a guess on a NEGATIVE number Morty, hats...hats off to you')
# Condition for input larger than latest episode number
else:
    print('Wrong! Haha, *burrp* there\'s only ' + str(maxNum) + ' epsidodes dumbass')

# Gives morty 5 guesses, starting at guess 2 (counts the first guess above)
for guessNumber in range(2, 8):  
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

# Condition for correct guess in guesses 2-5
if guess == rickNum:
    print('You guessed it Morty, we\'re watching episode ' + str(rickNum) + '!')
    print(str(guessNumber) + ' guesses, not bad Morty!')
# Condition for an idiot Morty
else:
    print('Your feeble capacity to guess an episode from a finite number set')
    print('is making me sober Morty! The episode was number ' + str(rickNum) + '!')