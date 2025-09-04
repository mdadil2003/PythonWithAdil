# Snake–Water–Gun game (CLI) in Python

import random

CHOICES = ["snake", "water", "gun"] # valid choices
ALIAS = {"s": "snake", "w": "water", "g": "gun"}  # handy shortcuts
BEATS = {"snake": "water", "water": "gun", "gun": "snake"} # winning choices

def normalize_choice(raw: str):
    raw = raw.strip().lower()
    if raw in CHOICES:
        return raw
    if raw in ALIAS:
        return ALIAS[raw]
    return None

def round_result(player: str, comp: str):
    if player == comp:
        return "draw"
    return "win" if BEATS[player] == comp else "lose"

def main():

    print("Snake–Water–Gun  |  choose: [s]nake, [w]ater, [g]un  |  quit: q")
    player_score = comp_score = draws = 0 

    while True:
        user_inp = input("\nYour pick (s/w/g or full word, q to quit): ").strip().lower()
        if user_inp == "q":
            break

        player = normalize_choice(user_inp)
        if not player:
            print("Invalid choice. Use s/w/g or snake/water/gun.")
            continue

        comp = random.choice(CHOICES) # computer's choice
        result = round_result(player, comp)

        # announce
        print(f"You: {player}  |  Computer: {comp}")
        if result == "win":
            print("→ You win this round!")
            player_score += 1
        elif result == "lose":
            print("→ Computer wins this round!")
            comp_score += 1
        else:
            print("→ Draw.")
            draws += 1
        print(f"Score — You: {player_score}  Comp: {comp_score}  Draws: {draws}")

    print("\nFinal Score:")
    print(f"You: {player_score}  Comp: {comp_score}  Draws: {draws}")
    if player_score > comp_score:
        print("🏆 You win the match!")
    elif comp_score > player_score:
        print("🤖 Computer wins the match!")
    else:
        print("🤝 Match drawn.")

if __name__ == "__main__":
    main()
    
# --- IGNORE ---