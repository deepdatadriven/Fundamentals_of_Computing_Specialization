# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Please input one word of them: rock, Spock, paper, lizard, scissors."
    
    #print name_to_number("paper")
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
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
    
    
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


