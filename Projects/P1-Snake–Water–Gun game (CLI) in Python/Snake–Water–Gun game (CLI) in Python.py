import random # For random choices
import json # For profile storage
import os # For file operations
from collections import Counter # For counting player history 

# ------------------ CONSTANTS ------------------
CHOICES = ["snake", "water", "gun"] # Valid choices
ALIAS = {"s": "snake", "w": "water", "g": "gun"} # Shortcuts
BEATS = {"snake": "water", "water": "gun", "gun": "snake"} # Winning logic
PROFILE_FILE = "player_profile.json" # Profile storage file

RESULT_EMOJI = {
    "win": "✅",
    "lose": "❌",
    "draw": "⚖️"
}

# ------------------ PROFILE SYSTEM ------------------
def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return {
        "name": "",
        "games": 0,
        "wins": 0,
        "losses": 0
    }

def save_profile(profile):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)

# ------------------ CORE LOGIC ------------------
def normalize_choice(raw):
    raw = raw.strip().lower()
    if raw in CHOICES:
        return raw
    return ALIAS.get(raw)

def round_result(player, comp):
    if player == comp:
        return "draw"
    return "win" if BEATS[player] == comp else "lose"

# ------------------ AI LOGIC ------------------
def smart_computer_choice(player_history):
    if not player_history:
        return random.choice(CHOICES)

    most_common = Counter(player_history).most_common(1)[0][0]
    for move, beats in BEATS.items():
        if beats == most_common:
            return move
    return random.choice(CHOICES)

def computer_choice(player_history, difficulty):
    if difficulty == "easy":
        return random.choice(CHOICES)
    elif difficulty == "medium":
        return smart_computer_choice(player_history)
    else:  # hard
        if random.random() < 0.7:
            return smart_computer_choice(player_history)
        return random.choice(CHOICES)

def explain_ai(player_history):
    if player_history:
        most = Counter(player_history).most_common(1)[0][0]
        print(f"🤖 AI Insight: You often choose '{most}'. AI adjusted strategy.")

# ------------------ ACHIEVEMENTS ------------------
def check_achievements(player_score, draws):
    if player_score >= 3:
        print("🏅 Achievement Unlocked: First Blood!")
    if draws >= 3:
        print("🎯 Achievement Unlocked: Peace Maker!")

# ------------------ GAME LOOP ------------------
def play_game(profile):
    print("\n🎮 SNAKE–WATER–GUN (ADVANCED MODE)")
    print("Commands: s/w/g | stats | help | q")
    
    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        difficulty = "medium"

    while True:
        try:
            rounds = int(input("Enter total rounds: "))
            if rounds > 0:
                break
        except ValueError:
            pass
        print("❌ Enter a valid number.")

    player_score = comp_score = draws = 0
    player_history = []
    history_log = []

    for round_no in range(1, rounds + 1):
        print(f"\n🔹 Round {round_no}/{rounds}")
        user_input = input("Your move: ").lower()

        if user_input == "q":
            print("🚪 Exiting match early.")
            break

        if user_input == "help":
            print("👉 Use s/w/g to play, stats to view profile, q to quit")
            continue

        if user_input == "stats":
            print(f"📊 Games: {profile['games']} | Wins: {profile['wins']} | Losses: {profile['losses']}")
            continue

        player = normalize_choice(user_input)
        if not player:
            print("❌ Invalid input.")
            continue

        computer = computer_choice(player_history, difficulty)
        result = round_result(player, computer)

        player_history.append(player)
        history_log.append((player, computer, result))

        print(f"You: {player} | Computer: {computer}")
        print(f"{RESULT_EMOJI[result]} Result: {result.upper()}")

        if result == "win":
            player_score += 1
        elif result == "lose":
            comp_score += 1
        else:
            draws += 1

        print(f"Score → You: {player_score} | Computer: {comp_score} | Draws: {draws}")

        if round_no % 3 == 0:
            explain_ai(player_history)

        if player_score > rounds // 2 or comp_score > rounds // 2:
            print("\n🏁 Match decided early!")
            break

    # ------------------ SUMMARY ------------------
    print("\n📊 MATCH SUMMARY")
    print("-" * 30)
    for i, (p, c, r) in enumerate(history_log, start=1):
        print(f"Round {i}: You={p} | Comp={c} | Result={r}")

    print("\n🏆 FINAL RESULT")
    print(f"You: {player_score} | Computer: {comp_score} | Draws: {draws}")

    if player_score > comp_score:
        print("🎉 YOU WON THE MATCH!")
        profile["wins"] += 1
    elif comp_score > player_score:
        print("🤖 COMPUTER WON THE MATCH!")
        profile["losses"] += 1
    else:
        print("🤝 MATCH DRAWN")

    profile["games"] += 1
    save_profile(profile)

    check_achievements(player_score, draws)

    total = player_score + comp_score + draws
    if total:
        win_rate = (player_score / total) * 100
        print(f"📈 Your win rate: {win_rate:.2f}%")

# ------------------ ENTRY POINT ------------------
def main():
    profile = load_profile()

    if not profile["name"]:
        profile["name"] = input("Enter your name: ").strip().title()
        save_profile(profile)

    print(f"\n👋 Welcome, {profile['name']}!")

    while True:
        play_game(profile)
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
