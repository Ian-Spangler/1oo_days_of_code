game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)

# print(new_enemy) # Error

def create_enemy():
    new_enemy = "" # It is better to initialize it out side of if statement
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)


# Modifying Global Scope

enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants (constants that you never want to change)

PI = 3.14159
URL = "https://www.google.com"
