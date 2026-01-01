import random
from collections import Counter

CHOICES = ["snake", "water", "gun"]
ALIAS = {"s": "snake", "w": "water", "g": "gun"}
BEATS = {"snake": "water", "water": "gun", "gun": "snake"}


def normalize_choice(raw):
    raw = raw.strip().lower()
    if raw in CHOICES:
        return raw
    return ALIAS.get(raw)


def round_result(player, comp):
    if player == comp:
        return "draw"
    return "win" if BEATS[player] == comp else "lose"


def smart_computer_choice(player_history):
    """
    Adaptive AI:
    - If player repeats a choice often, counter it
    - Otherwise choose randomly
    """
    if not player_history:
        return random.choice(CHOICES)

    most_common = Counter(player_history).most_common(1)[0][0]
    # Computer plays what beats player's frequent choice
    for move, beats in BEATS.items():
        if beats == most_common:
            return move
    return random.choice(CHOICES)


def play_game():
    print("\n🎮 SNAKE–WATER–GUN (ADVANCED MODE)")
    print("Choose: [s]nake, [w]ater, [g]un")
    print("Type 'q' anytime to quit\n")

    # Game setup
    while True:
        try:
            rounds = int(input("Enter total rounds (odd number recommended): "))
            if rounds > 0:
                break
        except ValueError:
            pass
        print("❌ Enter a valid positive number.")

    player_score = comp_score = draws = 0
    player_history = []
    history_log = []

    for round_no in range(1, rounds + 1):
        print(f"\n🔹 Round {round_no}/{rounds}")

        user_input = input("Your move: ").lower()
        if user_input == "q":
            print("\nGame exited early.")
            break

        player = normalize_choice(user_input)
        if not player:
            print("❌ Invalid choice. Round skipped.")
            continue

        computer = smart_computer_choice(player_history)
        result = round_result(player, computer)

        player_history.append(player)
        history_log.append((player, computer, result))

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        if result == "win":
            print("✅ You WIN this round!")
            player_score += 1
        elif result == "lose":
            print("❌ Computer wins this round.")
            comp_score += 1
        else:
            print("⚖️ Draw.")
            draws += 1

        print(f"Score → You: {player_score} | Computer: {comp_score} | Draws: {draws}")

        # Early win condition
        if player_score > rounds // 2 or comp_score > rounds // 2:
            print("\n🏁 Match decided early!")
            break

    # Final summary
    print("\n📊 MATCH SUMMARY")
    print("-" * 30)
    for i, (p, c, r) in enumerate(history_log, start=1):
        print(f"Round {i}: You={p} | Comp={c} | Result={r}")

    print("\n🏆 FINAL RESULT")
    print(f"You: {player_score} | Computer: {comp_score} | Draws: {draws}")

    if player_score > comp_score:
        print("🎉 CONGRATULATIONS! You won the match.")
    elif comp_score > player_score:
        print("🤖 Computer wins the match.")
    else:
        print("🤝 Match drawn.")

    total_played = player_score + comp_score + draws
    if total_played:
        win_rate = (player_score / total_played) * 100
        print(f"📈 Your win rate: {win_rate:.2f}%")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
