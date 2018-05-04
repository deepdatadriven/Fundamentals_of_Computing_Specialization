# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, range)
    global n
    n = int(math.ceil((math.log((range + 1), 2))))
    print 'New game. Range is from 0 to ' + str(range)
    print 'Number of remaining guess is ' + str(n)
    print ''
    # remove this when you add your code    
    #pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()
    
    # remove this when you add your code    
    #pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range 
    range = 1000
    new_game()
    #pass
    
def input_guess(guess):
    # main game logic goes here	
    global n
    guess = int(guess)
    n = n - 1
    print 'Guess was ' + str(guess)
    if n > 0:
        if guess < secret_number: 
            print 'Number of remaining guess is ' + str(n)
            print 'Higher'
            print ''
        elif guess > secret_number:
            print 'Number of remaining guess is ' + str(n)
            print 'Lower'
            print ''
        else:
            print 'Correct! You win the game!'
            print ''
            new_game()
    elif n == 0:
        if guess == secret_number:
            print 'Correct! You win the game!'
            print ''
        else:
            print 'Number of remaining guess is 0'
            print 'Game over, you can try it again :)'
            print 'The correct number was: ' + str(secret_number)
            print ''
        new_game()
    # remove this when you add your code
    #pass

    
# create frame
f = simplegui.create_frame('Guess the number', 200, 200)
# register event handlers for control elements and start frame
f.add_button('Range is [0,100)', range100, 200)
f.add_button('Range is [0,1000)', range1000, 200)
f.add_input('Input guess: ', input_guess, 200)
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
