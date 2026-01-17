import random
import time

# ---------------- SUBJECTS ----------------
SUBJECTS = [
    "Scientists",
    "Politicians",
    "Celebrities",
    "Tech Companies",
    "Athletes",
    "Shah Rukh Khan",
    "Elon Musk",
    "NASA",
    "Doctors",
    "Teachers",
    "Prime Minister Modi",
    "Engineers",
    "Auto Rickshaw Drivers",
    "Mumbai Local Train Drivers",
    "Software Developers"
]

# ---------------- ACTIONS ----------------
ACTIONS = [
    "discover",
    "announce",
    "launch",
    "investigate",
    "celebrate",
    "support",
    "oppose",
    "revolutionize",
    "transform",
    "ban",
    "promote",
    "debate",
    "unexpectedly visit",
    "collaborate with",
    "surprise fans with"
]

# ---------------- PLACES / THINGS ----------------
PLACES_THINGS = [
    "a new planet",
    "a groundbreaking technology",
    "a controversial policy",
    "a viral trend",
    "a historic event",
    "a medical breakthrough",
    "an environmental initiative",
    "a social movement",
    "a sports championship",
    "a cultural festival",
    "a new movie",
    "a music album",
    "a fashion line",
    "a video game",
    "a scientific study",
    "the Red Fort",
    "India Gate",
    "a plate of samosas",
    "a cup of chai"
]

# ---------------- HEADLINE STYLES ----------------
STYLES = [
    "BREAKING NEWS",
    "JUST IN",
    "TRENDING",
    "EXCLUSIVE",
    "HEADLINES TODAY"
]

# ---------------- FUNCTIONS ----------------
def generate_fake_headline():
    subject = random.choice(SUBJECTS)
    action = random.choice(ACTIONS)
    thing = random.choice(PLACES_THINGS)
    style = random.choice(STYLES)

    return f"{style}: {subject} {action} {thing}!"

def save_headline(headline):
    with open("headlines.txt", "a", encoding="utf-8") as file:
        file.write(headline + "\n")

def show_menu():
    print("\n📰 FAKE HEADLINE GENERATOR")
    print("1. Generate a headline")
    print("2. Generate multiple headlines")
    print("3. Save headline to file")
    print("4. Exit")

# ---------------- MAIN PROGRAM ----------------
def main():
    print("🎉 Welcome to the Advanced Fake Headline Generator 🎉")

    last_headline = ""

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            last_headline = generate_fake_headline()
            print("\n" + last_headline)

        elif choice == "2":
            try:
                count = int(input("How many headlines do you want? "))
                print("\nGenerating headlines...\n")
                for _ in range(count):
                    headline = generate_fake_headline()
                    print(headline)
                    time.sleep(0.5)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            if last_headline:
                save_headline(last_headline)
                print("✅ Headline saved to headlines.txt")
            else:
                print("⚠️ Generate a headline first.")

        elif choice == "4":
            print("\n👋 Thanks for using the Fake Headline Generator. Have a fun day!")
            break

        else:
            print("❌ Invalid choice. Try again.")

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    main()
