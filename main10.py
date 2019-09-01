#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #This will automatically put the words 'Greeting' for the person
colors = ['red','orange','yellow','green','blue','violet','purple'] #Gives the variables of which will be the right answer
play_again = '' #This will ask the person if they wish to play again
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #if the person writes 'n' or 'no', then the very last action will run
    match_color = random.choice(colors) #this will select one of the variables above as the right answer
    count = 0 #at this point, the person hasn't made any guess yet so the computer will count their guesses at 0
    color = '' #I actually have no clue what this is for. I got rid of it and ran the program, but everything seemed to run fine and I couldn't find out what is meant online
    while (color != match_color): #after a color is chosen, the actions below will run
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #this will make everything lowercase and remove all spaces after and before what is written
        count += 1 #1 try will be added to the person's count of how many time they have guessed
        if (color == match_color): #if the color that was chosen randomly by the computer is selected, then the action below will run
            print('Correct!') #this will pop up if the person meets the requirements above
        else: #if the action below does not have it's requirements met, the action below will run
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #this will be printed with the number of tries this person has taken if they don't get it right
    print('\nYou guessed it in {0} tries!'.format(count)) #This will be written after the answer is found and the count of how many the person has tried will be written
    if (count < best_count): #If the count for this game is less than the "best count", the actions below will be shown
        print('This was your best guess so far!') #if the count was smaller than the "best count", it will print those words
        best_count = count #if the "best count" is equal to the
    play_again = input("\nWould you like to play again? ").lower().strip() #This will be after someone answers correctly and it will give the question of if the person wants to try again or not and the person may answer for various results
print('Thanks for playing!') #This will automatically put the words after the person answers no to would they like to play again