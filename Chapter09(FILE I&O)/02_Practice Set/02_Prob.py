# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which iseither blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    print("you are playing the game..")
    score = random.randint(1, 62)
    print(f"your score: {score}")
    if(score>hiscore or hiscore==""):
        
    return score
game()
    
    print ("congratulations! you have just broken the hiscore")
    print("your hiscore is now:", score)
    