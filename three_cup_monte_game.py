# Tree cup monte is a game in which a ball is put under one of the three cups and then the cups are shuffled, and a person has to guess which cope has the ball under.
# This game is an example of how functions are used in python

#import required library or specific function from a library
from random import shuffle

# The shuffle function dosent return anything, hence cannot be assigned to a variable directly.

# hence the below custom function
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# Create a guess function for user input
def player_guess():

    guess = ""
    
    while guess not in [1,2,3]:
        guess = int(input("Pick a number from 1,2 or 3: "))
    return guess - 1

# Create a function to check location of the ball and user guess
def check_guess(mylist,guess):
    if mylist[guess] == ["O"]:
        print("Correct!")
        print(mylist)
    else:
        print("Wrong guess!")
        print(mylist)

# Now we use above functions together below

# Initial list
cup_config = [[" "],["O"],[" "]]

# Shuffle list
shuffled_cups = shuffle_list(cup_config)

# User guess  
user_input = player_guess()

# check guess
check_guess(shuffled_cups,user_input)