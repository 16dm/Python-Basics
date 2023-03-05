# creates a random variable between 1 and 5
#
import random
x = str(random.randrange (1,5))
#
# creates the input field and lets you guess a number
#
y = input("What is your Guess?" + str( ))
#
# compares the number you guessed to what x is and tells you if you won
#
if x == y: print("You Win!", x)
else:
    print("You Loose!", x)
#
# What I learned is that it is important to make sure that str or int is the same when using
# truth statements
#