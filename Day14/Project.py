# Higer or Lower
# url = https://appbrewery.github.io/python-day14-demo/
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
def compare(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1
    
print("You're right! Current score: 1")
print("Compare A: Shakira, a Musician, from Colombia")
print("Against B: Zendaya, a Actress and musician, from USA")
print("Sorry, that's wrong. Final score: 0")

