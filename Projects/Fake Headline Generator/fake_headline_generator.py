# import the randum mudule 
import random

# create subjects
subjects = [ 
    "Scientists",
    "Politicians",
    "Celebrities",
    "Tech Companies",
    "Athletes",
    "sharukh khan",
    "Elon Musk",
    "NASA",
    "Doctors",
    "Teachers",
    "Prime Ministers modi",
    "Engineers",
    "auto rikshaw drivers",
    "mumbai local train drivers",
    "software developers"
]

action = [
    "discover",
    "announce",
    "launch",
    "investigate",
    "criticize",
    "support",
    "oppose",
    "celebrate",
    "revolutionize",
    "transform",
    "ban",
    "promote",
    "debate",
    "eat eith",
    "dance with",
    "sing to"
]

places_and_things = [
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
    "red fort",
    "india gate",
    "plate of samosas",
    "cup of chai"
]


# function to generate a fake headline

while True:
    subjects_choice = random.choice(subjects)
    action_choice = random.choice(action)
    places_and_things_choice = random.choice(places_and_things)
      
    headline = f"BREAKING NEWS: {subjects_choice} {action_choice} {places_and_things_choice}!"
    print("\n" + headline)
    
    
    user_input = input("\nDo you want to another headline?? (Yes/No)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake Headline Generator. Have a fun day")
