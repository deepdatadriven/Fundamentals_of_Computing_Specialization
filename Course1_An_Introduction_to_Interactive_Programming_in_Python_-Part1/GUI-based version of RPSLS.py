# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

     
    
# Handler for input field
def get_guess(guess):
    if len(guess) > 3:
        guess = guess[0].upper() + guess[1: ].lower()
    else:
        print 'Please input Rock, paper, scissor, lizard or Spock!'
        print ''
        
    if guess != 'Rock' and guess != 'Paper' and guess != 'Scissor' and guess != 'Spock' and guess != 'Lizard':
        print 'Please input Rock, paper, scissor, lizard or Spock!'
        print ''
    else:
        rpsls(guess)
        
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "Rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "Paper":
        return 2
    elif name == "Lizard":
        return 3
    elif name == "Scissors":
        return 4
    else:
        return "Please input one word of them: rock, Spock, paper, lizard, scissors."
    
    #print name_to_number("paper")
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"
    else:
        return "Please input one number between 0-4."
#print number_to_name(3)    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    print "Computer chooses " + number_to_name(comp_number)
    # 0 win 34, 1 win 04, 2 win 01, 3 win 12, 4 win 23
    if player_number == comp_number:
        print "Player and computer tie!"
    else:
        if player_number == 0 and (comp_number == 3 or comp_number == 4):
            print "Player wins!"
        elif player_number == 1 and (comp_number == 0 or comp_number == 4):
            print "Player wins!"
        elif player_number == 2 and (comp_number == 0 or comp_number == 1):
            print "Player wins!"
        elif player_number == 3 and (comp_number == 1 or comp_number == 2):
            print "Player wins!"
        elif player_number == 4 and (comp_number == 2 or comp_number == 3):
            print "Player wins!"
        else:
            print "Computer wins!"                       
    print ""

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
