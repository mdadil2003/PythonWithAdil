class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0' # Sink it!
            
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)

        return island_count

# --- DRIVER CODE TO MAKE IT RUN ---
if __name__ == "__main__":
    sol = Solution()
    grid = [
      ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]
    ]
    print(sol.numIslands(grid))
    grid2 = [
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ]
    print(sol.numIslands(grid2))
    
import random
# Function to get difficulty level from user
def get_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (1-10, Unlimited attempts)")
    print("2. Medium (1-50, 10 attempts)")
    print("3. Hard (1-100, 5 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            return 10, None
        elif choice == "2":
            return 50, 10
        elif choice == "3":
            return 100, 5
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")
# Function to provide hints based on the closeness of the guess
def give_hint(guess, actual):
    diff = abs(guess - actual)
    if diff <= 3:
        print("🔥 Very close!")
    elif diff <= 10:
        print("🙂 Close!")
    else:
        print("❄️ Far away!")
# Main game function

def guess_the_number():
    max_num, max_attempts = get_difficulty()
    actual_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_num}.")
    if max_attempts:
        print(f"You have {max_attempts} attempts to guess it.\n")
    else:
        print("You have unlimited attempts to guess it.\n")
    while True:
        if max_attempts and attempts >= max_attempts:
            print(f"\n❌ Game Over! The correct number was {actual_number}.")
            break

        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > max_num:
                print(f"⚠️ Please enter a number between 1 and {max_num}.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")
            continue

            attempts += 1

            if guess < actual_number:
                print("⬆️ Try a higher number.")
                give_hint(guess, actual_number)
            elif guess > actual_number:
                print("⬇️ Try a lower number.")
                give_hint(guess, actual_number)
            else:
                print(f"🎉 Congratulations! You've guessed the number {actual_number} in {attempts} attempts.")
                break
                print("⬇️ Lower number please.")
                give_hint(guess, number_to_guess)
                