# Higer or Lower
# url = https://appbrewery.github.io/python-day14-demo/
import random
import game_data

higher_lower_logo = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/                                 
'''
vs_logo = '''
____   ____      
\   \ /   /_____ 
 \   Y   /  ___/ 
  \     /\___ \  
   \___//____  > 
             \/  
'''

data_center = game_data.data
score = 0
play = True

def selecter(dic):
    choice = random.choice(dic)
    return choice

def format(block, str):
    print(f"Compare {str}: {block["name"]}, a {block["description"]}, from {block["country"]}.")

def compare(a, b):
    a_follower = a["follower_count"]
    b_follower = b["follower_count"]
    if a_follower == b_follower:
        return 0
    elif a_follower > b_follower:
        return "A"
    else:
        return "B"

choice_1 = selecter(data_center)
print(higher_lower_logo)

while play:
    choice_2 = selecter(data_center)
    if choice_1 == choice_2:
        choice_2 = selecter(data_center)
    format(choice_1, "A")
    print(vs_logo)
    format(choice_2, "B")
    result = compare(choice_1, choice_2)
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if result == user_choice:
        score += 1
        print("\n" *20)
        print(higher_lower_logo)
        print(f"You're right! Current score: {score}")
        if result == 'B':
            choice_1 = choice_2
    else:
        print("\n" *20)
        print(higher_lower_logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False

