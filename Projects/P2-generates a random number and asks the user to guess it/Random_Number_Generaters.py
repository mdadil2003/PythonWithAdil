# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

import random # Importing the random module to generate random numbers
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    guessed = False

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed: # Loop until the user guesses the correct number
        try: 
            user_guess = int(input("Enter your guess: "))
            number_of_guesses += 1

            if user_guess < number_to_guess:
                print("Higher number please.")
                
            elif user_guess > number_to_guess:
                print("Lower number please.")
                
            else:
                guessed = True
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {number_of_guesses} guesses.")
        except ValueError:
            print("Please enter a valid integer.")
            
if __name__ == "__main__": # Running the game
    guess_the_number()
    