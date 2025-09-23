# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which iseither blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

def game():
    return 10 # suppose this is the score returned by the game
hiscore_file = 'Hi-score.txt'
with open(hiscore_file, 'r') as file:
    hiscore = file.read()
if hiscore == '':
    hiscore = 0
else:
    hiscore = int(hiscore)
if game() > hiscore:
    with open(hiscore_file, 'w') as file:
        file.write(str(game()))