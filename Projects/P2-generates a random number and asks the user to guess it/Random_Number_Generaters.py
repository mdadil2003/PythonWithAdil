# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

import random # Importing the random module to generate random numbers

def get_difficulty(): # Function to get difficulty level from the user
    print("\nChoose Difficulty Level:")
    print("1. Easy   (1–50, Unlimited guesses)")
    print("2. Medium (1–100, 10 guesses)")
    print("3. Hard   (1–200, 7 guesses)")

    while True: # Loop until a valid choice is made
        choice = input("Enter 1 / 2 / 3: ")
        if choice == "1":
            return 50, None
        elif choice == "2":
            return 100, 10
        elif choice == "3":
            return 200, 7
        else:
            print("❌ Invalid choice. Try again.")
# Function to provide hints based on the closeness of the guess
def give_hint(guess, actual):
    diff = abs(guess - actual)
    if diff <= 5:
        print("🔥 Very close!")
    elif diff <= 15:
        print("🙂 Close!")
    else:
        print("❄️ Far away!")
# Main game function
def guess_the_number():
    print("\n🎮 WELCOME TO GUESS THE NUMBER – ADVANCED MODE 🎮")

    max_range, max_attempts = get_difficulty()
    number_to_guess = random.randint(1, max_range)

    attempts = 0
    guessed = False

    print(f"\nI have selected a number between 1 and {max_range}.")
    if max_attempts:
        print(f"You have {max_attempts} attempts.\n")
    else:
        print("You have unlimited attempts.\n")

    while not guessed:
        if max_attempts and attempts >= max_attempts:
            print("\n❌ Game Over!")
            print(f"The correct number was: {number_to_guess}")
            break

        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > max_range:
                print(f"⚠️ Please enter a number between 1 and {max_range}.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("⬆️ Higher number please.")
                give_hint(guess, number_to_guess)

            elif guess > number_to_guess:
                print("⬇️ Lower number please.")
                give_hint(guess, number_to_guess)

            else:
                guessed = True
                print("\n🎉 CONGRATULATIONS!")
                print(f"You guessed the number {number_to_guess} correctly.")
                print(f"Total attempts used: {attempts}")

        except ValueError:
            print("❌ Invalid input. Please enter an integer.")
# Main function to run the game and handle replay
def main():
    while True:
        guess_the_number()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
