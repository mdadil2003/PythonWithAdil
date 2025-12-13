# import the randum mudule 
from email import generator
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

places_and_things = [  # list of places and things
    "new planet",
    "groundbreaking technology",
    " controversial policy",
    "viral trend",
    "historic event",
    " medical breakthrough",
    "an environmental initiative",
    " social movement",
    "a sports championship",
    "cultural festival",
    "new movie",
    "a music album",
    " fashion line",
    "video game",
    "scientific study",
    "red fort",
    "india gate",
    "plate of samosas",
    "cup of chai"
]

# function to generate a fake headline 

while True:
    subjects_choice = random.choice(subjects) # select a random subject from the subjects
    action_choice = random.choice(action)
    places_and_things_choice = random.choice(places_and_things) # select a random place or thing from the places_and_things
      
    headline = f"BREAKING NEWS: {subjects_choice} {action_choice} {places_and_things_choice}!"
    print("\n" + headline)
    
    # user input to generate another headline or exit
    user_input = input("\nDo you want to another headline?? (Yes/No)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake Headline Generator. Have a fun day")

# function to generate a fake headline 
generator
def generate_fake_headline():
    subjects_choice = random.choice(subjects)
    action_choice = random.choice(action)
    places_and_things_choice = random.choice(places_and_things)
      
    headline = f"BREAKING NEWS: {subjects_choice} {action_choice} {places_and_things_choice}!"
    return headline # return the generated headline
